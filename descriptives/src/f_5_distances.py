import ibis
from ibis import _
import pandas as pd
import folium

# ==========================================
# 1. Distance calculations
# ==========================================
# This produces a symmetric nxn sparse matrix of all distance pairs. Each distance appears twice.
def compute_distance_matrix(
    db_con: ibis.DuckDBConnection,
    table_in: str | ibis.Table,

    # Optional parameters
    table_out_name: str | None = None,         # If specified, write the result to a con.table. Otherwise, return the ibis.table expression.
    prop_col: str | None = None,              # Filter the possible joins based on string match of a property.
    max_distance: int | None = None,   # Filter the possible joins based on max distance. This helps memory usage.
    bind_by_box: bool = False,          # If true, calculates averages among rich dataset across several properties: ttwa, pc4, pc8.
    origin_id: str | None = None          # Rather than all-to-all distances, this specifices one-to-all distances.
) -> ibis.Table:

    if origin_id is not None and bind_by_box and max_distance is not None:
        raise ValueError("Cannot use origin_id with bind_by_box and max_distance. Please choose one method of filtering.")
    
    # Install spatial, load spatial
    db_con.raw_sql("INSTALL spatial; LOAD spatial;")
    t: ibis.Table = db_con.table(table_in) if isinstance(table_in, str) else table_in
    t_clean = t.filter([
        t.lon_dec.notnull() & (t.lon_dec != 0),
        t.lat_dec.notnull() & (t.lat_dec != 0)
    ])

    select_cols = ["registered_number", "lon_dec", "lat_dec"]
    if bind_by_box:
        t_clean = t.filter([
            t.ttwa.notnull(),
            t.pc4.notnull(),
            t.pc8.notnull()
        ])
        select_cols.extend(["pc4", "ttwa", "pc8"])
    if prop_col and prop_col not in select_cols:
        select_cols.append(prop_col)
    t_clean = t_clean.select(select_cols)

    # -------------------------------------------------------------
    # STEP 1: HIERARCHICAL BOUNDING BOXES (TTWA -> PC4)
    # -------------------------------------------------------------
    if bind_by_box and max_distance is not None:

        db_con.create_view("view_t_clean", t_clean, overwrite=True)
        
        # --- 1A. TTWA Bounding Boxes ---
        # Ibis ORM: Calculate TTWA centroids
        centroids_ttwa = t_clean.group_by('ttwa').aggregate(
            c_lon = _.lon_dec.mean(),
            c_lat = _.lat_dec.mean()
        )
        db_con.create_view("view_centroids_ttwa", centroids_ttwa, overwrite=True)
        radii_ttwa = db_con.sql(f"""
            SELECT 
                f.ttwa, 
                c.c_lon, 
                c.c_lat, 
                MAX(ST_Distance_Sphere(ST_Point(f.lon_dec, f.lat_dec), ST_Point(c.c_lon, c.c_lat))) AS radius
            FROM view_t_clean f
            JOIN view_centroids_ttwa c ON f.ttwa = c.ttwa 
            GROUP BY f.ttwa, c.c_lon, c.c_lat
        """)
        db_con.create_view("view_radii_ttwa", radii_ttwa, overwrite=True)
        valid_ttwa_pairs = db_con.sql(f"""
            SELECT 
                a.ttwa AS ttwa_a, 
                b.ttwa AS ttwa_b
            FROM view_radii_ttwa a 
            CROSS JOIN view_radii_ttwa b
            WHERE ST_Distance_Sphere(ST_Point(a.c_lon, a.c_lat), ST_Point(b.c_lon, b.c_lat)) 
                <= {max_distance} + a.radius + b.radius
        """)
        db_con.create_view("view_valid_ttwa_pairs", valid_ttwa_pairs, overwrite=True)
        print(f"--- Pre-filtered {valid_ttwa_pairs.count().execute():,} valid TTWA pairs for BVH optimization.")

        # --- 1B. PC4 Bounding Boxes ---
        centroids_pc4 = t_clean.group_by('pc4').aggregate(
            ttwa = _.ttwa.max(),
            c_lon = _.lon_dec.mean(),
            c_lat = _.lat_dec.mean()
        )
        db_con.create_view("view_centroids_pc4", centroids_pc4, overwrite=True)
        radii_pc4 = db_con.sql(f"""
            SELECT 
                f.pc4, 
                c.ttwa,
                c.c_lon, 
                c.c_lat, 
                MAX(ST_Distance_Sphere(ST_Point(f.lon_dec, f.lat_dec), ST_Point(c.c_lon, c.c_lat))) AS radius
            FROM view_t_clean f
            JOIN view_centroids_pc4 c ON f.pc4 = c.pc4 
            GROUP BY f.pc4, c.ttwa, c.c_lon, c.c_lat
        """)
        db_con.create_view("view_radii_pc4", radii_pc4, overwrite=True)
        valid_pc4_pairs = db_con.sql(f"""
            SELECT 
                a.pc4 AS pc4_a, 
                b.pc4 AS pc4_b
            FROM view_radii_pc4 a 
            JOIN view_radii_pc4 b ON 1=1
            -- CORE OPTIMIZATION: Only evaluate PC4s if their parent TTWAs overlap!
            JOIN view_valid_ttwa_pairs v 
              ON a.ttwa = v.ttwa_a AND b.ttwa = v.ttwa_b
            WHERE ST_Distance_Sphere(ST_Point(a.c_lon, a.c_lat), ST_Point(b.c_lon, b.c_lat)) 
                <= {max_distance} + a.radius + b.radius
        """)
        db_con.create_view("view_valid_pc4_pairs", valid_pc4_pairs, overwrite=True)
        print(f"--- Pre-filtered {valid_pc4_pairs.count().execute():,} valid PC4 pairs for BVH optimization.")
        print(f"--- Schema of 'view_valid_pc4_pairs': {db_con.table('view_valid_pc4_pairs').schema()}")
    # -------------------------------------------------------------
    # STEP 2: FIRM-TO-FIRM SPATIAL EDGE LIST
    # -------------------------------------------------------------
    
    # Rename all columns safely to avoid namespace collisions during the join
    tf_i = t_clean.rename({f"{col}_i": col for col in t_clean.columns})
    tf_j = t_clean.rename({f"{col}_j": col for col in t_clean.columns})

    if bind_by_box and max_distance is not None:
        # Optimal BVH Join: Link Firms through the pre-validated PC4 intersections
        valid_pc4 = db_con.table("view_valid_pc4_pairs")
        joined = (
            tf_i.inner_join(valid_pc4, tf_i.pc4_i == valid_pc4.pc4_a)
                .inner_join(tf_j, valid_pc4.pc4_b == tf_j.pc4_j)
                .filter(tf_i.registered_number_i != tf_j.registered_number_j)
        )
        print(f"--- Joined maximum {joined.count().execute():,} firm pairs for distance calculation.")
    elif origin_id is not None:
        # One-to-All Join: Link Firms through the specified origin_id
        tf_i_one = tf_i.filter(tf_i.registered_number_i == origin_id)
        joined = tf_i_one.cross_join(tf_j).filter(tf_i_one.registered_number_i != tf_j.registered_number_j)
    else:
        # Fallback block-diagonal logic if Bounding Volumes are disabled
        joined = tf_i.inner_join(
            tf_j, 
            [
                tf_i[prop_col + "_i"] == tf_j[prop_col + "_j"] if prop_col else True,
                tf_i.registered_number_i != tf_j.registered_number_j
            ]
        )

    # Hybrid Handoff: Register temporary view to query natively
    db_con.create_view("temp_spatial_pairs", joined, overwrite=True)

    # SQL Wrapper: Final Distance calculation & exact firm-to-firm hard filtering
    where_clause = ""
    if max_distance is not None:
        where_clause = f"""
        WHERE ST_Distance_Sphere(
            ST_Point(lon_dec_i, lat_dec_i), 
            ST_Point(lon_dec_j, lat_dec_j)
        ) <= {max_distance}
        """

    matrix_expr = db_con.sql(f"""
        SELECT 
            registered_number_i AS firm_i,
            registered_number_j AS firm_j,
            ST_Distance_Sphere(
                ST_Point(lon_dec_i, lat_dec_i), 
                ST_Point(lon_dec_j, lat_dec_j)
            ) AS distance_meters
        FROM temp_spatial_pairs
        {where_clause}
    """)

    add_info = f" (filtered to <= {max_distance/1000}km using BVH)" if max_distance is not None else ""
    print(f"--- Materializing sparse distance matrix{add_info} out-of-core...")
    
    if table_out_name is None:
        return matrix_expr
    else:
        db_con.create_table(table_out_name, matrix_expr, overwrite=True)
        return db_con.table(table_out_name)

# ==========================================
# 2. Table joining data FETCHING FUNCTION
# ==========================================
# Joins the fixed and distance tables
def join_fd_tables(table_fixed: ibis.Table, table_distances: ibis.Table,
                   i_name: str = "i",
                   j_name: str = "j",
                   max_peers: int = None, # type: ignore
                   filter_ids: list[str] = []
) -> ibis.Table:
    tf_i = table_fixed.alias("tf_i").rename("{name}_" + i_name)
    tf_j = table_fixed.alias("tf_j").rename("{name}_" + j_name)

    # Filter the massive distance matrix down to just our target firms
    if len(filter_ids) == 0:
        table_out = table_distances
    elif len(filter_ids) <= 40:
        table_out = table_distances.filter(table_distances.firm_i.isin(filter_ids)) # type: ignore
    else:
        # If the list is too long, we can use a memtable and inner_join
        temp_table = ibis.memtable({"firm_id": filter_ids})
        table_out = (
            table_distances
            .inner_join(temp_table, table_distances.firm_i == temp_table.firm_id) # type: ignore
            .select(table_distances.columns)
        )
    if max_peers is not None:
        w = ibis.window(
            group_by=table_out.firm_i, 
            order_by=ibis.random()
        )
        table_sampled = (
            table_out
            .mutate(rand_rank=ibis.row_number().over(w))
            .filter(ibis._.rand_rank <= max_peers)
            .drop("rand_rank")
        )
        table_out = table_sampled

    table_result = (
        table_out
        .left_join(tf_i, _.firm_i == tf_i[f"registered_number_{i_name}"]) # type: ignore
        .left_join(tf_j, _.firm_j == tf_j[f"registered_number_{j_name}"]) # type: ignore
        .rename({
            f"firm_{i_name}": "firm_i",
            f"firm_{j_name}": "firm_j"
        })
    )
    return table_result # type: ignore

# ==========================================
# 3. Folium PLOTTING FUNCTION
# ==========================================
# Generates a Folium map plotting multiple firm networks in unique colors.
# Need columns: distance_meters, { firm, lat_dec, lon_dec, pc8 } for both '_target' and '_peer'.
import folium
import pandas as pd

def plot_folium_network(
    df_networks: pd.DataFrame, 
    ordered_targets: list[list[str]] | None = None, 
    descent: bool = False
) -> folium.Map:
    
    if df_networks.empty:
        print("No network data found to plot.")
        return None # type: ignore

    center_lat = df_networks['lat_dec_target'].mean()
    center_lon = df_networks['lon_dec_target'].mean()
    m = folium.Map(location=[center_lat, center_lon], zoom_start=11, tiles="CartoDB positron")

    # ✅ FIX 1: Use the perfectly ordered list from the generator if provided
    if ordered_targets is None:
        ordered_targets = [df_networks['firm_target'].unique().tolist()]
    all_target_ids = [id for sublist in ordered_targets for id in sublist]
    normal_colours = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'cadetblue', 'darkgreen', 'darkpurple', 'black']
    descent_colors = ['blue', 'darkred', 'red', 'lightred', 'pink']
    colours = descent_colors if descent else normal_colours

    node_id = 0
    for depth, arr in enumerate(ordered_targets):
        for idx, target_id in enumerate(arr):
            
            # Protect against targets that might have been filtered out
            target_data = df_networks[df_networks['firm_target'] == target_id]
            if target_data.empty:
                continue

            t_lat = target_data['lat_dec_target'].iloc[0]
            t_lon = target_data['lon_dec_target'].iloc[0]
            t_pc8 = target_data['pc8_target'].iloc[0]
            
            colour = colours[depth % len(colours)] if (descent) else colours[idx % len(colours)]

            target_obj = { "ID": target_id, "Postcode": t_pc8 }
            if descent:
                target_obj['Depth'] = depth
                target_obj['Network'] = node_id
            folium.Marker(
                location=[t_lat, t_lon],
                tooltip="<b>TARGET FIRM</b><br>" + "<br>".join(": ".join([k, str(v)]) for k, v in target_obj.items()),
                icon=folium.Icon(color=colour, icon="star")
            ).add_to(m)

            max_dist = target_data['distance_meters'].max() or 1 

            for _, row in target_data.iterrows():
                p_lat, p_lon = row['lat_dec_peer'], row['lon_dec_peer']
                dist, peer_id = row['distance_meters'], row['firm_peer']
                
                peer_obj = { "Peer": peer_id, "Postcode": row['pc8_peer'], "Distance": f"{dist:,.1f} m" }
                folium.CircleMarker(
                    location=[p_lat, p_lon], radius=4, color=colour, fill=True, fill_color=colour,
                    fill_opacity=0.6, tooltip="<br>".join(": ".join([k, str(v)]) for k, v in peer_obj.items())
                ).add_to(m)
                
                opacity = max(0.1, 1.0 - (dist / max_dist))
                folium.PolyLine(
                    locations=[(t_lat, t_lon), (p_lat, p_lon)], color=colour, weight=1.5,
                    opacity=opacity, dash_array="5, 5"
                ).add_to(m)
            node_id += 1
    return m