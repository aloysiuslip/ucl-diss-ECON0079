import pandas as pd
import ibis
from typing import Any

# def set_address with raw and derived dataframes parameters
# dataframe has columns address_raw (str) and address_level (int)
def set_address(raw: pd.DataFrame, derived: pd.DataFrame = pd.DataFrame(columns=[
    "registered_number", "address_raw", "address_level"
])) -> pd.DataFrame:

    # Create a column in derived which corresponds to the column in raw
    # i.e. finds the matching registered_number if it exists as an entry in derived
    # or creates the row if it doesn't exist
    # and then sets address_raw as 'primary_trading_address_longitude' if it exists in raw and is notna
    # and then sets address_level as 1
    if 'primary_trading_address' in raw.columns:
        derived['address_raw'] = raw['primary_trading_address']
        derived['address_level'] = 1
    else:
        derived['address_raw'] = None
        derived['address_level'] = None

    return derived

# --- Date processing #

# Inspects an Ibis Schema (or dict mapping col->type), finds all date/timestamp fields,
# and automatically converts numeric Excel serials (e.g. 43616.0) or string dates
# in the DataFrame into proper Python date objects.
def coerce_df_dates_from_schema(schema: ibis.Schema, df: pd.DataFrame) -> pd.DataFrame:

    for field_name, field_type in schema.fields.items():

        if field_name not in df.columns:
            continue

        if not isinstance(field_type, ibis.expr.datatypes.Date):
            continue

        series = df[field_name]

        # Case A: Column contains numeric Excel serials (floats/ints like 43616.0)
        if pd.api.types.is_numeric_dtype(series):
            df[field_name] = pd.to_datetime(
                series, 
                unit="D", 
                origin="1899-12-30", 
                errors="coerce"
            ).dt.date

        # Case B: Column contains string representations (e.g. "2019-06-01" or "43616.0")
        elif pd.api.types.is_object_dtype(series) or pd.api.types.is_string_dtype(series):
            # Try numeric conversion first in case serials were read as strings (e.g., "43616.0")
            numeric_series = pd.to_numeric(series, errors="coerce")
            
            if numeric_series.notna().any():
                # Has numeric serials as strings
                converted_dates = pd.to_datetime(
                    numeric_series, 
                    unit="D", 
                    origin="1899-12-30", 
                    errors="coerce"
                ).dt.date   
                
                # Fill any non-numeric string dates (fallback parsing)
                fallback_dates = pd.to_datetime(series, errors="coerce")
                df[field_name] = converted_dates.fillna(fallback_dates)
            else:
                # Standard string date parsing
                df[field_name] = pd.to_datetime(series, errors="coerce")

        # Case C: column is already a pandas datetime or date type, no action needed
        elif pd.api.types.is_datetime64_any_dtype(series):
            continue

        print(f"⚠️ Coerced column '{field_name}' to datetime based on schema type '{field_type}'")

    return df

# Finds date fields in the schema and attempts to parse them natively in Ibis.
# Handles both standard date strings and Excel numeric serials.
def coerce_ibis_dates_from_schema(schema: ibis.Schema, table: ibis.expr.types.Table) -> ibis.expr.types.Table:

    mutations = {}
    
    for field_name, field_type in schema.items():
        if field_name not in table.columns:
            continue
            
        if not isinstance(field_type, ibis.expr.datatypes.Date):
            continue
            
        col = table[field_name]
        
        # 1. Standard Cast: Tries to parse strings (e.g., '2019-06-01') or existing datetimes
        standard_cast = col.try_cast(field_type)
        
        # 2. Excel Math: Tries to cast to integer and add to the 1899-12-30 epoch
        # (If the data is a standard string, try_cast('int32') gracefully returns NULL)
        excel_math = (
            ibis.date('1899-12-30') + (ibis.interval(days=1) * col.try_cast('int32'))
        ).cast(field_type)
        
        # 3. Coalesce: Take the standard cast. If it failed, take the Excel math.
        mutations[field_name] = ibis.coalesce(standard_cast, excel_math)
        
    # Apply the date conversions (if any) and return the table
    if mutations:
        return table.mutate(**mutations)
    return table


# Mimics pd.DataFrame.reindex(). 
# Filters to schema columns, adds missing columns as typed NULLs, and sets the order.
# .select() accepts a dictionary, applying our rules and ordering simultaneously
def reindex_ibis_table(schema: ibis.Schema, table: ibis.expr.types.Table, fill_value: Any = ibis.null()) -> ibis.expr.types.Table:
   
    projection: dict[str, ibis.expr.types.Value] = {}
    for col_name, col_type in schema.items():
        if col_name in table.columns:
            # Column exists, just pass it through
            projection[col_name] = table[col_name]
        else:
            # Column is missing, generate a virtual NULL with the exact DuckDB type
            projection[col_name] = fill_value.cast(col_type) # type: ignore   
    
    return table.select(**projection)

# --- #