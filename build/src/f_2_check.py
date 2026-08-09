from typing import Any, Union
import pandas as pd

def filter_df_entry(
    df: pd.DataFrame,       # raw pandas dataframe based on the 
    ind: str,               # 2-digit SIC code of the industry
    property: str,          # sections of files, ex: a1_ID, a2_key_finance, etc.
    file_ref: str           # tail of the filename, ex: "18_01 1", "18_04"
) -> pd.DataFrame:
    
    print("hello world")

    # Filter out rows from the dataframe where the property 'no_of_available_years' is zero
    df1 = df[df['no_of_available_years'] > 0]


    return df1

#---- Columns ---#

def drop_duplicate_columns(df: pd.DataFrame) -> pd.DataFrame:

    # Check for duplicate columns and print them
    duplicate_columns = df.columns[df.columns.duplicated()].unique()
    if len(duplicate_columns) > 0:
        print(f"Duplicate columns found: {duplicate_columns}") 

    # Drop Excel duplicate columns, meaning any ending in .1, .2, etc. and keep the first one
    df = df.loc[:, ~df.columns.str.match(r'.*\.\d+$')]

    return df

def test_drop_duplicate_columns():
    test_df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": [4, 5, 6],
        "A.1": [7, 8, 9],
        "C": [10, 11, 12],
        "B.1": [13, 14, 15]
    })
    result_df = drop_duplicate_columns(test_df)
    expected_columns = ["A", "B", "C"]
    assert list(result_df.columns) == expected_columns, f"Test failed for drop_duplicate_columns. Expected columns: {expected_columns}, but got: {list(result_df.columns)}"
    print("✅ All tests passed for drop_duplicate_columns function.")

#--- Schema matching ---#

from ibis import Schema

# Given a schema and a DataFrame, check if the DataFrame matches the schema
def check_df_matches_schema(mapping: Union[Schema, pd.DataFrame], df: pd.DataFrame, test_mode: bool = False) -> bool:

    schema_names = set()
    if isinstance(mapping, Schema):
        schema_names = set(mapping.keys())
    elif isinstance(mapping, pd.DataFrame):
        schema_names = set(mapping["key"].tolist())
    else:
        raise ValueError("Mapping must be an ibis Schema or a dictionary.")
    df_names = set(df.columns)
    missing_columns = schema_names - df_names
    extra_columns = df_names - schema_names

    # Check for missing or extra columns
    if missing_columns:
        if not test_mode:
            raise ValueError(f"❌ Missing columns in DataFrame: {missing_columns}")
        return False

    if extra_columns:
        if not test_mode:
            raise ValueError(f"❌ Extra columns in DataFrame: {extra_columns}")
        return False

    # Check if the number of columns matches
    if len(schema_names) != len(df_names):
        if not test_mode:
            raise ValueError(f"❌ Column count mismatch: Expected {len(schema_names)} columns, but got {len(df_names)}")
        return False

    # Check if the registered_number column is missing or has any NaN values
    # as this is our primary key
    if 'registered_number' not in df.columns:
        if not test_mode:
            raise ValueError("❌ Missing primary key column: registered_number")
        return False
    
    if df['registered_number'].isnull().any():
        if not test_mode:
            raise ValueError("❌ Primary key column 'registered_number' contains NaN values")
        return False

    # Check if the registered_number column has any duplicate values
    if df['registered_number'].duplicated().any():
        if not test_mode:
            raise ValueError("❌ Primary key column 'registered_number' contains duplicate values")
        return False

    return True

# Given a list of column names and a DataFrame, add any missing columns to the DataFrame with NaN values
def set_na_columns(columns: list[str] | set[str], df: pd.DataFrame) -> pd.DataFrame:
    if isinstance(columns, set):
        columns = list(columns)
    for col in columns:
        if col not in df.columns:
            df[col] = pd.NA
    return df

# Excel date serials for years 2000-2030 fall roughly between 36526 and 47482
# This is a fairly dangerous function that could distort my data
# We apply lots of safeguards and flag any changes
def handle_excel_dates(df: pd.DataFrame, ref: str = "") -> pd.DataFrame:

    for col in df.columns:
        if not "date" in col.lower():
            continue

        if col.lower().startswith("consolidated"):
            continue

        if pd.api.types.is_datetime64_any_dtype(df[col]):
            continue

        if not (pd.api.types.is_numeric_dtype(df[col]) or pd.api.types.is_string_dtype(df[col])):
            continue

        numeric_col = pd.to_numeric(df[col], errors='coerce')

        # If it's completely empty after coercion, but wasn't empty before, 
        # it might be standard date strings (e.g., "2023-01-01"). Parse them normally.
        if numeric_col.isna().all() and not df[col].isna().all():
             df[col] = pd.to_datetime(df[col], errors="coerce")
             continue
        
        if not pd.api.types.is_numeric_dtype(numeric_col):
            continue

        # Keeping it as datetime64[ns] (removing .dt.date) for Ibis/DuckDB compatibility
        df[col] = pd.to_datetime(numeric_col, unit="D", origin="1899-12-30", errors="coerce")
        print(f"⚠️ Converted Excel date serials to datetime for column '{col}'{' in file ' + ref if ref else ''}")

    return df

def rename_df_with_years(df: pd.DataFrame, fuzzy_map: dict[str, str], property: str, start_year: int, end_year: int, ref: str = "") -> pd.DataFrame:

    if property in ["a1_ID", "a5_misc"]:
        df.rename(columns=fuzzy_map, inplace=True)           # Rename according to our mapping
        return df
    
    # For yearly properties, we need to take each column name
    # If it matches a fuzzy mapping in the schema (no modifications)
    # Then just do a simple rename with shcmea_raw_fuzzy_col_map
    # If it doesn't match, we need to check if it has a year in the name
    # If it does, extract the year (last 4 digits), trim whitespace off the remainder
    # Then check if the remainder matches a fuzzy mapping in the schema
    # If it does, rename the column to the schema name using schema_raw_fuzzy_col_map
    # And reappend _[year] to the schema name, ex: consolidated_2019
    # We will process the years later via pivots
    elif property in ["a2_key_finance", "a3_assets", "a4_profits"]:
        
        df_raw_renamed = {}
        for col in df.columns:

            if col in fuzzy_map:
                df_raw_renamed[col] = fuzzy_map[col]
                continue
            if len(col) < 4:
                continue
            if not col[-4:].isdigit():
                continue

            year = int(col[-4:])
            if year < start_year or year > end_year:
                raise ValueError(f"❌ Error: Column name '{col}' has year {year} outside of range {start_year}-{end_year}")
            base_col_name = col[:-4].strip().replace('\n', '')  # Remove the year and trim whitespace
            if base_col_name not in fuzzy_map:
                raise ValueError(f"❌ Error: Column name '{col}' base name '{base_col_name}' not found in schema mapping")

            new_col_name = f"{fuzzy_map[base_col_name]}_{year}"
            df_raw_renamed[col] = new_col_name
        # print(f"--- Created column mapping for file {ref} which are: {df_raw_renamed}")
        df.rename(columns=df_raw_renamed, inplace=True)
        return df

    else:
        raise ValueError(f"❌ Error: Property '{property}' not recognized for renaming columns. Ref: {ref}")

if __name__ == "__main__":
    # filter_df_entry(df=pd.DataFrame(), ind="01", property="a1_ID", file_ref="18_01 1")
    test_drop_duplicate_columns()
    # test_handle_excel_dates()
    # test_check_df_matches_schema()