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

    
if __name__ == "__main__":
    # filter_df_entry(df=pd.DataFrame(), ind="01", property="a1_ID", file_ref="18_01 1")
    test_drop_duplicate_columns()