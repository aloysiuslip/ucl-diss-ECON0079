import pandas as pd
import numpy as np
import re

def parse_excel_or_iso_date(s):
    if pd.isna(s):
        return pd.NaT
    s = str(s).strip()
    if not s:
        return pd.NaT
    # Try numeric excel date first
    try:
        num = float(s)
        return pd.to_datetime(num, unit='D', origin='1899-12-30')
    except ValueError:
        pass
    # Try standard string parse (infer_datetime_format)
    try:
        return pd.to_datetime(s, dayfirst=True)
    except Exception:
        return pd.NaT

def parse_accounting_reference_md_str(s):
    d = parse_excel_or_iso_date(s)
    if pd.isna(d):
        # check if it's just a dd/mm or mm/dd format (like '31/12')
        s_str = str(s).strip()
        if re.match(r'^\d{1,2}/\d{1,2}$', s_str):
            try:
                d_test = pd.to_datetime(s_str + '/2000', dayfirst=True)
                return d_test.strftime('%m-%d')
            except Exception:
                pass
        return np.nan
    return d.strftime('%m-%d')

def fix_date_vars(df):
    if 'status_date' in df.columns:
        df['status_date'] = df['status_date'].apply(parse_excel_or_iso_date)
    if 'date_of_incorporation' in df.columns:
        df['date_of_incorporation'] = df['date_of_incorporation'].apply(parse_excel_or_iso_date)
    if 'accounting_reference_date' in df.columns:
        df['accounting_reference_date'] = df['accounting_reference_date'].apply(parse_accounting_reference_md_str)
    return df

# Write tests for the functions above

def test_parse_excel_or_iso_date():
    assert parse_excel_or_iso_date('2023-01-01') == pd.Timestamp('2023-01-01')
    assert parse_excel_or_iso_date('01/01/2023') == pd.Timestamp('2023-01-01')
    assert parse_excel_or_iso_date(44927) == pd.Timestamp('2023-01-01')  # Excel date
    assert pd.isna(parse_excel_or_iso_date(None))
    assert pd.isna(parse_excel_or_iso_date(''))

def test_parse_accounting_reference_md_str():
    assert parse_accounting_reference_md_str('2023-01-01') == '01-01'
    assert parse_accounting_reference_md_str('01/01/2023') == '01-01'
    assert parse_accounting_reference_md_str(44927) == '01-01'  # Excel date
    assert parse_accounting_reference_md_str('31/12') == '12-31'
    assert pd.isna(parse_accounting_reference_md_str(None))
    assert pd.isna(parse_accounting_reference_md_str(''))

def test_fix_date_vars():
    df = pd.DataFrame({
        'status_date': ['2023-01-01', '01/01/2023', 44927, '2025-01-05', None],
        'date_of_incorporation': ['2023-01-01', '01/01/2023', 44927, '2025-01-05', None],
        'accounting_reference_date': ['2023-01-01', '01/01/2023', 44927, '31/12', None]
    })
    df_fixed = fix_date_vars(df)
    
    assert df_fixed['status_date'].iloc[0] == pd.Timestamp('2023-01-01')
    assert df_fixed['status_date'].iloc[1] == pd.Timestamp('2023-01-01')
    assert df_fixed['status_date'].iloc[2] == pd.Timestamp('2023-01-01')
    assert pd.isna(df_fixed['status_date'].iloc[4])
    
    assert df_fixed['date_of_incorporation'].iloc[0] == pd.Timestamp('2023-01-01')
    assert df_fixed['date_of_incorporation'].iloc[1] == pd.Timestamp('2023-01-01')
    assert df_fixed['date_of_incorporation'].iloc[2] == pd.Timestamp('2023-01-01')
    assert pd.isna(df_fixed['date_of_incorporation'].iloc[4])
    
    assert df_fixed['accounting_reference_date'].iloc[0] == '01-01'
    assert df_fixed['accounting_reference_date'].iloc[1] == '01-01'
    assert df_fixed['accounting_reference_date'].iloc[2] == '01-01'
    assert df_fixed['accounting_reference_date'].iloc[3] == '12-31'
    assert pd.isna(df_fixed['accounting_reference_date'].iloc[4])

test_parse_excel_or_iso_date()
test_parse_accounting_reference_md_str()
test_fix_date_vars()