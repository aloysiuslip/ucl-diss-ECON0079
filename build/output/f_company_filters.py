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

if __name__ == "__main__":
    filter_df_entry(df=pd.DataFrame(), ind="01", property="a1_ID", file_ref="18_01 1")