import pandas as pd

# Set flags in the DataFrame to indicate whether data was available for certain columns.
def set_derived_flags(raw: pd.DataFrame, derived: pd.DataFrame = pd.DataFrame(columns=[
    "registered_number", "has_ptaddress", "has_ptaddress_latlong", "is_public", "has_company_branch_mismatch"
])) -> pd.DataFrame:

    # We need the row to exist in derived for every row in raw
    # If the registered_number in raw is not in derived, we need to add it
    for reg_num in raw['registered_number']:
        if reg_num not in derived['registered_number'].values:
            derived = pd.concat([derived, pd.DataFrame({"registered_number": [reg_num]})], ignore_index=True)

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

    # If raw data has a different non.na values for company_name and branch_name
    # And they are different (different string match)
    # Then set 'has_company_branch_mismatch' property in derived to True, else False
    if 'company_name' in raw.columns and 'branch_name' in raw.columns:
        if raw['company_name'].notna().any() and raw['branch_name'].notna().any():
            derived['has_company_branch_mismatch'] = raw['company_name'] != raw['branch_name']
        else:
            derived['has_company_branch_mismatch'] = False
    else:
        derived['has_company_branch_mismatch'] = False

    return derived

def test_set_derived_flags():
    test_df1 = pd.DataFrame({
        "registered_number": [2, 6, 8],
        "primary_trading_address": ["123 Main St", None, "456 Elm St"],
        "primary_trading_address_latitude": [51.5074, None, 40.7128],
        "primary_trading_address_longitude": [-0.1278, None , -74.0060]
    })
    result_df1 = set_derived_flags(test_df1)
    assert result_df1['registered_number'].tolist() == [2, 6, 8], "Test failed for registered_number column"
    assert result_df1['has_ptaddress'].tolist() == [True, False, True], "Test failed for has_ptaddress flag"

    test_df2 = pd.DataFrame({
        "registered_number": [2, 6, 8],
        "primary_trading_address": [None, None, None],
        "primary_trading_address_latitude": [None, None, None],
        "primary_trading_address_longitude": [None, None, None],
        "ticker_symbol": [None, "APPL", None],
        "company_name": ["Company A", "Company B", "Company C"],
        "branch_name": ["Company A", "Company B", "Company D"]
    })
    input_df2 = pd.DataFrame({
        "registered_number": [2, 6, 8],
        "has_ptaddress": [False, False, False],
        "has_ptaddress_latlong": [False, False, False],
        "is_public": [False, False, False],
        "has_company_branch_mismatch": [False, False, False]
    })
    result_df2 = set_derived_flags(test_df2, input_df2)
    assert result_df2['has_ptaddress'].tolist() == [False, False, False], "Test failed for has_ptaddress flag with all None"
    assert result_df2['has_ptaddress_latlong'].tolist() == [False, False, False], "Test failed for has_ptaddress_latlong flag with all None"
    assert result_df2['is_public'].tolist() == [False, True, False], "Test failed for is_public flag with one ticker_symbol"
    assert result_df2['has_company_branch_mismatch'].tolist() == [False, False, True], "Test failed for has_company_branch_mismatch flag with one mismatch"

    test_df3 = pd.DataFrame({
        "registered_number": [2, 6, 8],
        "primary_trading_address": [None, "456 Elm St", "789 Oak St"],
        "primary_trading_address_latitude": [51.5074, 40.7128, 34.0522],
        "primary_trading_address_longitude": [-0.1278, -74.0060, -118.2437],
        "ticker_symbol": ["AAPL", "GOOGL", None],
        "company_name": ["Company A", "Company B", "Company E"],
        "branch_name": ["Company A", "Company D", "Company F"]
    })
    input_df3 = pd.DataFrame({
        "registered_number": [1, 2, 3]
    }, columns=["registered_number", "has_ptaddress", "has_ptaddress_latlong", "is_public", "has_company_branch_mismatch"])
    result_df3 = set_derived_flags(test_df3, input_df3)
    assert result_df3['registered_number'].tolist() == [1, 2, 3, 6, 8], "Test failed for registered_number column"
    assert result_df3['has_ptaddress'].tolist() == [False, False, False, True, True], "Test failed for has_ptaddress flag with mixed values"
    assert result_df3['has_ptaddress_latlong'].tolist() == [False, False, False, True, True], "Test failed for has_ptaddress_latlong flag with mixed values"
    assert result_df3['is_public'].tolist() == [False, True, False, True, False], "Test failed for is_public flag with mixed values"
    assert result_df3['has_company_branch_mismatch'].tolist() == [False, False, False, True, True], "Test failed for has_company_branch_mismatch flag with mixed values"

    print("✅ All tests passed for set_derived_flags function.")
