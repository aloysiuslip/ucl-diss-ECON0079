from typing import Any, Union
import pandas as pd
from pygments.unistring import So
from sqlglot import case

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

# For every column in the df dataframe
# The schema dataframe has column 'key' which is the column name
# And a 'may_mix' column which is a boolean
# If 'may_mix' is False, ignore the column
# otherwise, check the column in the df, and ensure that it is the value specified in the 'type' column of the schema
def handle_mixed_types(schema: pd.DataFrame, df: pd.DataFrame, ref: str = "") -> pd.DataFrame:

    # Filter the rows of the schema dataframe where 'may_mix' is True and the 'key' is in the df columns
    rows_mixed_types = schema[
        (schema["may_mix"] == True) &
        (schema["key"].isin(df.columns))
    ]

    for _, row in rows_mixed_types.iterrows():
        col_name = row["key"]
        expected_type = row["type"]

        actual_type = df[col_name].dtype
        if actual_type == expected_type:
            continue
        if actual_type == "str" and expected_type == "string":
            continue

        # print(f"--- Matching column '{col_name}' in file '{ref}' with actual type '{actual_type}' to expected type '{expected_type}'")

        match expected_type:
            case 'int64':
                match actual_type:
                    case 'int64':
                        continue
                    case 'float64':
                        df[col_name] = df[col_name].astype('Int64')
                    case 'str':
                        df[col_name] = pd.to_numeric(df[col_name], errors='coerce').astype('Int64')
                    case 'object':
                        df[col_name] = pd.to_numeric(df[col_name], errors='coerce').astype('Int64')
                    case _:
                        raise ValueError(f"❌ Column '{col_name}' in file '{ref}' has an unrecognized actual type '{actual_type}' for expected type 'int64'")

            case 'float64':
                match actual_type:
                    case 'float64':
                        continue
                    case 'int64':
                        df[col_name] = df[col_name].astype('float64')
                    case 'str':
                        df[col_name] = pd.to_numeric(df[col_name], errors='coerce').astype('float64')
                    case 'object':
                        df[col_name] = pd.to_numeric(df[col_name], errors='coerce').astype('float64')
                    case _:
                        raise ValueError(f"❌ Column '{col_name}' in file '{ref}' has an unrecognized actual type '{actual_type}' for expected type 'float64'")

            case 'boolean':
                match actual_type:
                    case 'string':
                        df[col_name] = df[col_name].str.lower().str.strip().map({
                            'consolidated': True,
                            'unconsolidated': False
                        }).astype('boolean')
                    case 'bool':
                        df[col_name] = df[col_name].astype('boolean')
                    case 'object':
                        # String methods has no attribute 'trim'
                        df[col_name] = df[col_name].astype(str).str.lower().str.strip().map({
                            'consolidated': True,
                            'unconsolidated': False
                        }).astype('boolean')
                    case 'float64':
                        # column is 1, 0, or NaN. Convert to boolean
                        df[col_name] = df[col_name].map({
                            1.0: True,
                            0.0: False
                        }).astype('boolean')
                    case _:
                        raise ValueError(f"❌ Column '{col_name}' in file '{ref}' has an unrecognized actual type '{actual_type}' for expected type 'boolean'")

            case 'string':
                df[col_name] = df[col_name].astype("string").str.replace(r'\.0$', '', regex=True)   

            case _:
                raise ValueError(f"❌ Column '{col_name}' in file '{ref}' has an unrecognized expected type '{expected_type}'")

    return df

# Rename columns of raw df to standardise it
# We've modified this to make the fuzzy_map as comprehensive as possible
# To reduce computations in this loop
def rename_df_with_years(df: pd.DataFrame, fuzzy_map: dict[str, str], property: str, start_year: int, end_year: int, delimiter: str="@", ref: str = "") -> pd.DataFrame:

    unrecognised_columns = df.columns[~df.columns.isin(fuzzy_map.keys())]
    if len(unrecognised_columns) > 0:
        print(f"⚠️ Unrecognised columns in file '{ref}': {unrecognised_columns}")
        print(f"Fuzzy map keys: {list(fuzzy_map.keys())}")
    df.rename(columns=fuzzy_map, inplace=True)                 # Rename according to our mapping
    if property in ["a1_ID", "a5_misc"]:
        return df

    if property not in ["a2_key_finance", "a3_assets", "a4_profits"]:
        raise ValueError(f"❌ Error: Unknown property '{property}'. Ref: {ref}")
    
    # For yearly properties, we need to take each column name
    # If it matches a fuzzy mapping in the schema (no modifications)
    # Then just do a simple rename with shcmea_raw_fuzzy_col_map
    # If it doesn't match, we need to check if it has a year in the name
    # If it does, extract the year (last 4 digits), trim whitespace off the remainder
    # Then check if the remainder matches a fuzzy mapping in the schema
    # If it does, rename the column to the schema name using schema_raw_fuzzy_col_map
    # And reappend _[year] to the schema name, ex: consolidated_2019
    # We will process the years later via pivots


    build_new_col_map = {}
    for col in unrecognised_columns:

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

        new_col_name = f"{fuzzy_map[base_col_name]}{delimiter}{year}"
        build_new_col_map[col] = new_col_name

    print(f"--- Created column mapping for file {ref} which are: {build_new_col_map}")
    df.rename(columns=build_new_col_map, inplace=True)
    return df

if __name__ == "__main__":
    # filter_df_entry(df=pd.DataFrame(), ind="01", property="a1_ID", file_ref="18_01 1")
    test_drop_duplicate_columns()
    # test_handle_excel_dates()
    # test_check_df_matches_schema()