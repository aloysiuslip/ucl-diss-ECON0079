import pandas as pd
from f_2_check import drop_duplicate_columns, rename_df_with_years

# INGEST
# Worker function to process a single Excel file in an isolated CPU process.
# Takes a single tuple of arguments to easily map over an iterable.
def ingest_single_excel_file(args):
    file_name, file_path, property_name, col_map, start_year, end_year, ind, exact_cols, yearly_cols = args
    
    try:
        # LOAD
        df_raw = pd.read_excel(file_path, engine='calamine', sheet_name='Results', header=0, dtype={
            "Registered number": str            # "Leading Zeros" Trap
        })
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
        print(f"⚠️ Worker Error on file {file_name}: {e}")
        return None  # Return None on failure to filter out later