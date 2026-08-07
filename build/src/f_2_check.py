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
def check_df_matches_schema(mapping: Union[Schema, dict[str, Any]], df: pd.DataFrame, test_mode: bool = False) -> bool:

    schema_names = set()
    if isinstance(mapping, Schema):
        schema_names = set(mapping.keys())
    elif isinstance(mapping, dict):
        schema_names = set(mapping.keys())
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

# # Test for check_df_matches_schema based on the ibis.schema object
# # don't use the fuzzy_col_by_index object because it doesn't contain all the columns of the schema
# def test_check_df_matches_schema():

#     # Hardcode a test for all the column names in the scheme in a dataframe and check that the function returns True
#     hard_names = [
#         "company_name", "registered_number", "ticker_symbol", "ro_address", "ro_address_line_1", "ro_address_line_2", "ro_address_line_3",
#         "ro_address_line_4", "ro_address_line_5", "ro_city", "ro_county", "ro_postcode", "ro_full_postcode", "ro_country", "ro_latitude", "ro_longitude",
#         "ro_nuts_region", "ro_postal_region", "ro_phone", "ro_phone_registered_on_tps", "ro_phone_registered_on_ctps", "primary_trading_address", "primary_trading_address_latitude",
#         "primary_trading_address_longitude", "primary_trading_address_no_of_employees", "branch_name", "trade_description", "primary_uk_sic_2007_code",
#         "primary_uk_sic_2007_description", "full_overview", "history", "primary_business_line", "secondary_business_line", "main_activity", "secondary_activity",
#         "main_products_and_services", "size_estimate", "strategy_organization_and_policy", "strategic_alliances", "membership_of_a_network", "main_brand_names",
#         "main_domestic_country", "main_foreign_countries_or_regions", "main_production_sites", "main_distribution_sites", "main_sales_representation_sites", "main_customers",
#         "latest_accounts_date", "no_of_available_years"
#     ]

#     test_mapping_dict = {col: "foobar" for col in hard_names}

#     # Create a DataFrame with correct column names
#     correct_df = pd.DataFrame(columns=list(schema_fixed_ibis.keys()))
#     assert check_df_matches_schema(test_mapping_dict, correct_df) == True, "Test failed for DataFrame with correct schema"
    
#     # Create a DataFrame with missing columns
#     incorrect_df_missing = pd.DataFrame(columns=list(schema_fixed_ibis.keys())[:-1])  # Remove last column
#     assert check_df_matches_schema(incorrect_df_missing, test_mode=True) == False, "Test failed for DataFrame with missing columns"
    
#     # Create a DataFrame with extra columns
#     incorrect_df_extra = pd.DataFrame(columns=list(schema_fixed_ibis.keys()) + ["extra_column"])
#     assert check_df_matches_schema(incorrect_df_extra, test_mode=True) == False, "Test failed for DataFrame with extra columns"
    
#     # Create a DataFrame with incorrect column count (fewer columns)
#     incorrect_df_count = pd.DataFrame(columns=[col for col in list(schema_fixed_ibis.keys())[:-1]])  # Remove last column
#     assert check_df_matches_schema(incorrect_df_count, test_mode=True) == False, "Test failed for DataFrame with incorrect column count"


#     hardcoded_df = pd.DataFrame(columns=hard_names)
#     assert check_df_matches_schema(hardcoded_df) == True, "Test failed for hardcoded DataFrame with correct schema"

#     hard_names2 = hard_names + ["extra_column"]
#     hardcoded_df2 = pd.DataFrame(columns=hard_names2)
#     assert check_df_matches_schema(hardcoded_df2, test_mode=True) == False, "Test should have rejected hardcoded DataFrame with extra column"

#     hard_names3 = hard_names[:-1]
#     hardcoded_df3 = pd.DataFrame(columns=hard_names3)
#     assert check_df_matches_schema(hardcoded_df3, test_mode=True) == False, "Test failed for hardcoded DataFrame with missing column"

#     print("✅ All tests passed for check_df_matches_schema.")

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
def fix_excel_dates(df: pd.DataFrame, ref: str = "") -> pd.DataFrame:

    for col in df.columns:
        if not "date" in col.lower():
            continue
        if not pd.api.types.is_numeric_dtype(df[col]):
            continue

        valid_range = df[col].dropna().between(35000, 50000)
        if not valid_range.all():
            continue
        if len(valid_range) == 0:
            continue

        df[col] = pd.to_datetime(df[col], unit="D", origin="1899-12-30", errors="coerce").dt.date
        print(f"⚠️ Converted Excel date serials to datetime for column '{col}'{' in file ' + ref if ref else ''}")

    return df

if __name__ == "__main__":
    # filter_df_entry(df=pd.DataFrame(), ind="01", property="a1_ID", file_ref="18_01 1")
    test_drop_duplicate_columns()
    # test_fix_excel_dates()
    # test_check_df_matches_schema()