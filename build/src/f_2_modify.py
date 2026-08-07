import pandas as pd

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

if __name__ == "__main__":

    test_set_data_av_flags()