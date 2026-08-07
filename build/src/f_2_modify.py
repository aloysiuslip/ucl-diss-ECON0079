import pandas as pd
import ibis
from typing import Union

# Set flags in the DataFrame to indicate whether data was available for certain columns.
def set_data_av_flags(raw: pd.DataFrame, derived: pd.DataFrame
    = pd.DataFrame(columns=["has_ptaddress", "has_ptaddress_latlong", "is_public"])
) -> pd.DataFrame:

    # Create a whole new column in the dataframe which has a value based on the other columns
    # If there is no primary trading address, then the value is False
    # If there is a primary trading adress and it is notna, then the value is True
    if 'primary_trading_address' not in raw.columns:
        derived['has_ptaddress'] = False
    else:
        derived['has_ptaddress'] = raw['primary_trading_address'].notna()
    if 'primary_trading_address_latitude' not in raw.columns or 'primary_trading_address_longitude' not in raw.columns:
        derived['has_ptaddress_latlong'] = False
    else:
        derived['has_ptaddress_latlong'] = raw['primary_trading_address_latitude'].notna() & raw['primary_trading_address_longitude'].notna()

    # If raw data has 'ticker_symbol' as a column and that value is a string
    # Set 'is_public' property in derived to True, else False
    if 'ticker_symbol' in raw.columns:
        if raw['ticker_symbol'].notna().any():
            derived['is_public'] = True
        else:
            derived['is_public'] = False
    else:
        derived['is_public'] = False

    return derived

def test_set_data_av_flags():
    test_df1 = pd.DataFrame({
        "primary_trading_address": ["123 Main St", None, "456 Elm St"],
        "primary_trading_address_latitude": [51.5074, None, 40.7128],
        "primary_trading_address_longitude": [-0.1278, None , -74.0060]
    })
    result_df1 = set_data_av_flags(test_df1)
    assert result_df1['has_ptaddress'].tolist() == [True, False, True], "Test failed for has_ptaddress flag"
    test_df2 = pd.DataFrame({
        "primary_trading_address": [None, None, None],
        "primary_trading_address_latitude": [None, None, None],
        "primary_trading_address_longitude": [None, None, None]
    })
    result_df2 = set_data_av_flags(test_df2)
    assert result_df2['has_ptaddress'].tolist() == [False, False, False], "Test failed for has_ptaddress flag with all None"
    assert result_df2['has_ptaddress_latlong'].tolist() == [False, False, False], "Test failed for has_ptaddress_latlong flag with all None"
    test_df3 = pd.DataFrame({
        "primary_trading_address": ["123 Main St", "456 Elm St", "789 Oak St"]
    })
    result_df3 = set_data_av_flags(test_df3)
    assert result_df3['has_ptaddress'].tolist() == [True, True, True], "Test failed for has_ptaddress flag with only primary_trading_address column"
    assert result_df3['has_ptaddress_latlong'].tolist() == [False, False, False], "Test failed for has_ptaddress_latlong flag with only primary_trading_address column"
    test_df4 = pd.DataFrame({
        "primary_trading_address_latitude": [51.5074, 40.7128, 34.0522],
        "primary_trading_address_longitude": [-0.1278, -74.0060, -118.2437]
    })
    result_df4 = set_data_av_flags(test_df4)
    assert result_df4['has_ptaddress'].tolist() == [False, False, False], "Test failed for has_ptaddress flag with only latitude and longitude columns"
    assert result_df4['has_ptaddress_latlong'].tolist() == [True, True, True], "Test failed for has_ptaddress_latlong flag with only latitude and longitude columns"
    print("✅ All tests passed for set_data_av_flags function.")

# --- Date processing #

# Inspects an Ibis Schema (or dict mapping col->type), finds all date/timestamp fields,
# and automatically converts numeric Excel serials (e.g. 43616.0) or string dates
# in the DataFrame into proper Python date objects.
def coerce_df_dates_from_schema(schema: ibis.Schema, df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    for f in schema.fields:
        if f.col_name not in df.columns:
            continue

        if not isinstance(f.type, ibis.expr.datatypes.Date):
            continue

        series = df[f.col_name]

        # Case A: Column contains numeric Excel serials (floats/ints like 43616.0)
        if pd.api.types.is_numeric_dtype(series):
            df[f.col_name] = pd.to_datetime(
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
                fallback_dates = pd.to_datetime(series, errors="coerce").dt.date
                df[f.col_name] = converted_dates.fillna(fallback_dates)
            else:
                # Standard string date parsing
                df[f.col_name] = pd.to_datetime(series, errors="coerce").dt.date#

        # Case C: column is already a pandas datetime or date type, no action needed
        elif pd.api.types.is_datetime64_any_dtype(series):
            continue
        elif pd.api.types.is_datetime64_dtype(series):
            continue
        elif pd.api.types.is_datetime64_ns_dtype(series):
            continue

        else:
            continue

        print(f"⚠️ Coerced column '{f.col_name}' to datetime based on schema type '{f.type}'")

    return df

# --- #

if __name__ == "__main__":

    test_set_data_av_flags()