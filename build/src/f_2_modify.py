import pandas as pd
import ibis
from typing import Union


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

    for field_name in schema.fields:
        field_type = schema.fields[field_name]
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

# --- #