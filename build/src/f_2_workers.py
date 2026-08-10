import pandas as pd
from f_0_dirs import get_data_dirs
from f_2_check import drop_duplicate_columns, rename_df_with_years

dirs = get_data_dirs()

# INGEST
# Worker function to process a single Excel file in an isolated CPU process.
# Takes a single tuple of arguments to easily map over an iterable.
def ingest_single_excel_file(args):
    file_name, file_path, property_name, col_map, start_year, end_year, ind, exact_cols, yearly_cols = args
    
    try:
        # LOAD
        fame_na_strings = ["n.a.", "n.a", "N.A.", "N.A", "n/a", "N/A", "-", ""]
        df_raw = pd.read_excel(file_path, engine='calamine', sheet_name='Results', header=0, dtype={
            "Registered number": str            # "Leading Zeros" Trap
        }, na_values=fame_na_strings, keep_default_na=True)
        df_raw.drop(df_raw.columns[0], axis=1, inplace=True)
        df_raw = drop_duplicate_columns(df_raw)
        
        # RENAME
        df_raw = rename_df_with_years(
            df_raw, col_map, property_name, start_year, end_year,
            delimiter="@", ref=f"{ind}/{property_name}/{file_name}"
        )
        
        # 1. SHRINK ROWS
        df_raw = df_raw[df_raw['registered_number'].notna()]
        
        # 2. SHRINK COLUMNS
        df_raw_cols = [
            col for col in df_raw.columns 
            if col == 'registered_number' or col in exact_cols or any(col.startswith(yc) for yc in yearly_cols)
        ]
        df_raw2 = df_raw[df_raw_cols].copy()

        df_raw2['file_codes'] = " ".join(file_name.split()[2:]).replace(".xlsx", "")
        
        return df_raw2
        
    except Exception as e:
        # This is run as a worker so we need better error logging than just printing the exception.
        # Write to outdir errors.log file
        with open(dirs.output_dir / "errors.log", "a") as f:
            # Encode the error to avoid 'charmap' codec can't encode issues
            f.write(f"Error processing file {file_name} for property {property_name}")
            f.write(f"{str(e).encode('utf-8', 'replace').decode('utf-8')}\n")
        return None  # Return None on failure to filter out later