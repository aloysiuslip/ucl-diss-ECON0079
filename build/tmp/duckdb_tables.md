# Tables in DuckDB database

## fame_derived

### Number of rows: 0

### Schema:

```
ibis.Schema {
  registered_number            string
  has_ptaddress                boolean
  has_ptaddress_latlong        boolean
  is_public                    boolean
  has_company_branch_mismatch  boolean
  industry_codes               string
  file_codes                   string
}
```

### Head of table:

```
Empty DataFrame
Columns: [registered_number, has_ptaddress, has_ptaddress_latlong, is_public, has_company_branch_mismatch, industry_codes, file_codes]
Index: []
```

## fame_fixed

### Number of rows: 0

### Schema:

```
ibis.Schema {
  company_name                       string
  registered_number                  string
  ticker_symbol                      string
  primary_trading_address            string
  primary_trading_address_latitude   string
  primary_trading_address_longitude  string
  branch_name                        string
  primary_uk_sic_2007_code           int64
  primary_uk_sic_2007_description    string
  latest_accounts_date               date
  no_of_available_years              int64
  guo                                string
  guo_nb                             int64
  entity_type                        string
}
```

### Head of table:

```
Empty DataFrame
Columns: [company_name, registered_number, ticker_symbol, primary_trading_address, primary_trading_address_latitude, primary_trading_address_longitude, branch_name, primary_uk_sic_2007_code, primary_uk_sic_2007_description, latest_accounts_date, no_of_available_years, guo, guo_nb, entity_type]
Index: []
```

## fame_yearly

### Number of rows: 1,649,675

### Schema:

```
ibis.Schema {
  registered_number             string
  fame_key                      string
  year                          int64
  consolidated                  boolean
  turnover                      float64
  shareholders_funds            float64
  profit_loss_pretax            float64
  employees                     int64
  tangibles                     float64
  tangibles_land_and_buildings  float64
  tangibles_land_freehold       float64
  tangibles_land_leasehold      float64
  fixed_other                   float64
  intangibles                   float64
  fixed_total                   float64
  liabilities                   float64
  total_assets                  float64
  liabilites_lt                 float64
  cos                           float64
  dividends                     float64
  r_and_d                       float64
  remuneration_employees        float64
  wages                         float64
  social_security_costs         float64
  pensions_costs                float64
  ebitda                        float64
}
```

### Head of table:

```
  registered_number fame_key  year consolidated  turnover  shareholders_funds  \
0          13168354      NaN  2024         None       NaN             113.833   
1          13195278      NaN  2024         None       NaN              45.255   
2          13231843      NaN  2024         None       NaN             -15.870   
3          13895539      NaN  2024         None       NaN               2.351   
4          14206512      NaN  2024         None       NaN              -7.628   

   profit_loss_pretax  employees  tangibles  tangibles_land_and_buildings  \
0                 NaN        3.0      2.777                         2.777   
1                 NaN        2.0     58.463                           NaN   
2                 NaN        1.0     40.094                           NaN   
3                 NaN        NaN      3.049                           NaN   
4                 NaN        NaN        NaN                           NaN   

   ...  total_assets  liabilites_lt  cos  dividends  r_and_d  \
0  ...       147.416            NaN  NaN        NaN      NaN   
1  ...        59.303        -11.108  NaN        NaN      NaN   
2  ...        44.589         -0.420  NaN        NaN      NaN   
3  ...        18.063            NaN  NaN        NaN      NaN   
4  ...         1.217         -0.979  NaN        NaN      NaN   

   remuneration_employees  wages  social_security_costs  pensions_costs  \
0                     NaN    NaN                    NaN             NaN   
1                     NaN    NaN                    NaN             NaN   
2                     NaN    NaN                    NaN             NaN   
3                     NaN    NaN                    NaN             NaN   
4                     NaN    NaN                    NaN             NaN   

   ebitda  
0     NaN  
1     NaN  
2     NaN  
3     NaN  
4     NaN  

[5 rows x 26 columns]
```

## ibis_pandas_memtable_noln3fqpsvcphe7yqwd3x2a6jq

### Number of rows: 452,638

### Schema:

```
ibis.Schema {
  registered_number                string
  company_name_A                   string
  primary_uk_sic_2007_code         string
  primary_uk_sic_2007_description  string
  full_overview                    string
  primary_business_line            string
  no_of_available_years            string
  latest_accounts_date             string
  company_name_B                   string
  inactive                         string
  quoted                           string
  own_data                         string
  woco                             string
  bv_d_id_number                   string
  company_status                   string
  status_date                      string
  legal_form                       string
  date_of_incorporation            string
  accounting_reference_date        string
  registered_accounts_type         string
  jordans_company_classification   string
  account_currency                 string
  guo_name                         string
  guo_bv_d_id_number               string
  duo_name                         string
  duo_bv_d_id_number               string
}
```

### Head of table:

```
  registered_number           company_name_A primary_uk_sic_2007_code  \
0           0028326       BLACKSTAR GROUP SE                    66120   
1           0043472          SCOTTY GROUP SE                    26309   
2           0053787       PETRA DIAMONDS LTD                    08990   
3           0054897               HISCOX LTD                    65120   
4           0056130  LANCASHIRE HOLDINGS LTD                    65120   

                     primary_uk_sic_2007_description full_overview  \
0         Security and commodity contracts brokerage           NaN   
1  Manufacture of communication equipment (other ...           NaN   
2                  Other mining and quarrying n.e.c.           NaN   
3                                 Non-life insurance           NaN   
4                                 Non-life insurance           NaN   

  primary_business_line no_of_available_years latest_accounts_date  \
0                   NaN                     6           2016-06-30   
1                   NaN                     1           2011-12-31   
2                   NaN                     7           2017-06-30   
3                   NaN                     8           2023-12-31   
4                   NaN                     8           2023-12-31   

            company_name_B inactive  ...      legal_form  \
0       BLACKSTAR GROUP SE       No  ...      Public AIM   
1          SCOTTY GROUP SE       No  ...           Other   
2       PETRA DIAMONDS LTD       No  ...      Public AIM   
3               HISCOX LTD       No  ...  Public, Quoted   
4  LANCASHIRE HOLDINGS LTD       No  ...  Public, Quoted   

  date_of_incorporation accounting_reference_date registered_accounts_type  \
0                   NaN                       NaN                      NaN   
1            2012-05-11                       NaN                      NaN   
2            1997-03-25                       NaN                      NaN   
3            2006-09-06                       NaN                      NaN   
4            2005-10-12                       NaN                      NaN   

  jordans_company_classification account_currency guo_name guo_bv_d_id_number  \
0               Fame A, full a/c              GBP      NaN                NaN   
1               Fame A, full a/c              GBP      NaN                NaN   
2               Fame A, full a/c              GBP      NaN                NaN   
3               Fame A, full a/c              GBP      NaN                NaN   
4               Fame A, full a/c              GBP      NaN                NaN   

  duo_name duo_bv_d_id_number  
0      NaN                NaN  
1      NaN                NaN  
2      NaN                NaN  
3      NaN                NaN  
4      NaN                NaN  

[5 rows x 26 columns]
```

## ibis_pandas_memtable_psswfiperjaofoly3zph76qs3q

### Number of rows: 25,589,852

### Schema:

```
ibis.Schema {
  registered_number  string
  raw_key            string
  value              float64
}
```

### Head of table:

```
  registered_number            raw_key  value
0          13883823  consolidated@2025    NaN
1          14578152  consolidated@2025    NaN
2          14605628  consolidated@2025    NaN
3          11791537  consolidated@2025    NaN
4          12547173  consolidated@2025    NaN
```

## ibis_pandas_memtable_sijkp7sjyrhhxgsfoh35gvmyom

### Number of rows: 2,378,089

### Schema:

```
ibis.Schema {
  registered_number                         string
  company_name                              string
  year                                      string
  consolidated                              string
  employees                                 string
  systemA_industry                          string
  cons_uncons                               string
  turnover_th_gbp                           string
  shareholders_funds_th_gbp                 string
  profit_loss_before_taxation_th_gbp        string
  number_of_employees                       string
  total_assets_th_gbp                       string
  ebitda_th_gbp                             string
  current_liabilities_th_gbp                string
  long_term_liabilities_th_gbp              string
  research_development_th_gbp               string
  wages_salaries_th_gbp                     string
  interest_paid_th_gbp                      string
  taxation_th_gbp                           string
  depreciation_th_gbp                       string
  tangible_assets_th_gbp                    string
  intangible_assets_th_gbp                  string
  fixed_assets_th_gbp                       string
  other_fixed_assets_th_gbp                 string
  pension_costs_th_gbp                      string
  social_security_costs_th_gbp              string
  dividends_distributable_profit_th_gbp     string
  systemB_group                             string
  cost_of_sales_th_gbp                      string
  exceptional_items_pre_gp_th_gbp           string
  cash_out_in_flow_investing_activ_th_gbp   string
  capital_expenditure_financ_invest_th_gbp  string
  acquisition_disposal_th_gbp               string
  equity_dividends_paid_th_gbp              string
  company_name_raw                          string
}
```

### Head of table:

```
  registered_number        company_name  year consolidated employees  \
0           0028326  BLACKSTAR GROUP SE  2013            1        16   
1           0028326  BLACKSTAR GROUP SE  2014            1        13   
2           0028326  BLACKSTAR GROUP SE  2015            1        15   
3           0028326  BLACKSTAR GROUP SE  2016            1        12   
4           0043472     SCOTTY GROUP SE  2011            1        31   

  systemA_industry   cons_uncons turnover_th_gbp shareholders_funds_th_gbp  \
0               58  Consolidated             NaN                     74804   
1               58  Consolidated           13737                     80563   
2               58  Consolidated           22316                    230416   
3               58  Consolidated           19696                    179223   
4               26  Consolidated            5002                      5673   

  profit_loss_before_taxation_th_gbp  ... social_security_costs_th_gbp  \
0                              12203  ...                          NaN   
1                               8168  ...                          NaN   
2                              18384  ...                          NaN   
3                             -33814  ...                          NaN   
4                               -200  ...                          340   

  dividends_distributable_profit_th_gbp   systemB_group cost_of_sales_th_gbp  \
0                                 -1382  58_59_60_61_63                  NaN   
1                                 -1034  58_59_60_61_63                  NaN   
2                                  -647  58_59_60_61_63                  NaN   
3                                  -466  58_59_60_61_63                  NaN   
4                                   NaN           22_30                -2072   

  exceptional_items_pre_gp_th_gbp cash_out_in_flow_investing_activ_th_gbp  \
0                             NaN                                     -37   
1                             NaN                                     -10   
2                             NaN                                      -3   
3                             NaN                                    -171   
4                             NaN                                    -145   

  capital_expenditure_financ_invest_th_gbp acquisition_disposal_th_gbp  \
0                                      NaN                         NaN   
1                                      NaN                         NaN   
2                                      NaN                         NaN   
3                                      NaN                         NaN   
4                                      NaN                         NaN   

  equity_dividends_paid_th_gbp    company_name_raw  
0                        -1382  BLACKSTAR GROUP SE  
1                        -1034  BLACKSTAR GROUP SE  
2                         -647  BLACKSTAR GROUP SE  
3                         -466  BLACKSTAR GROUP SE  
4                          NaN     SCOTTY GROUP SE  

[5 rows x 35 columns]
```

## ibis_pandas_memtable_zd7pe536mzag5omxsul3yets7m

### Number of rows: 3,747,139

### Schema:

```
ibis.Schema {
  registered_number  string
  raw_key            string
  value              float64
}
```

### Head of table:

```
  registered_number            raw_key  value
0          SC651293  consolidated@2025    NaN
1          11152158  consolidated@2025    NaN
2          SC557929  consolidated@2024    NaN
3          SC558215  consolidated@2024    NaN
4          SC558898  consolidated@2024    NaN
```

## ibis_pandas_memtable_zyitpvnt6jabbebskgc3ssjbgm

### Number of rows: 4,510,418

### Schema:

```
ibis.Schema {
  registered_number  string
  raw_key            string
  value              float64
}
```

### Head of table:

```
  registered_number            raw_key  value
0          15121553  consolidated@2025    NaN
1          IE049139  consolidated@2024    NaN
2          IE115954  consolidated@2024    NaN
3          IE118233  consolidated@2024    NaN
4          IE135555  consolidated@2024    NaN
```

## lars_fixed

### Number of rows: 452,638

### Schema:

```
ibis.Schema {
  registered_number                string
  company_name_A                   string
  primary_uk_sic_2007_code         string
  primary_uk_sic_2007_description  string
  full_overview                    string
  primary_business_line            string
  no_of_available_years            string
  latest_accounts_date             string
  company_name_B                   string
  inactive                         string
  quoted                           string
  own_data                         string
  woco                             string
  bv_d_id_number                   string
  company_status                   string
  status_date                      string
  legal_form                       string
  date_of_incorporation            string
  accounting_reference_date        string
  registered_accounts_type         string
  jordans_company_classification   string
  account_currency                 string
  guo_name                         string
  guo_bv_d_id_number               string
  duo_name                         string
  duo_bv_d_id_number               string
}
```

### Head of table:

```
  registered_number           company_name_A primary_uk_sic_2007_code  \
0           0028326       BLACKSTAR GROUP SE                    66120   
1           0043472          SCOTTY GROUP SE                    26309   
2           0053787       PETRA DIAMONDS LTD                    08990   
3           0054897               HISCOX LTD                    65120   
4           0056130  LANCASHIRE HOLDINGS LTD                    65120   

                     primary_uk_sic_2007_description full_overview  \
0         Security and commodity contracts brokerage           NaN   
1  Manufacture of communication equipment (other ...           NaN   
2                  Other mining and quarrying n.e.c.           NaN   
3                                 Non-life insurance           NaN   
4                                 Non-life insurance           NaN   

  primary_business_line no_of_available_years latest_accounts_date  \
0                   NaN                     6           2016-06-30   
1                   NaN                     1           2011-12-31   
2                   NaN                     7           2017-06-30   
3                   NaN                     8           2023-12-31   
4                   NaN                     8           2023-12-31   

            company_name_B inactive  ...      legal_form  \
0       BLACKSTAR GROUP SE       No  ...      Public AIM   
1          SCOTTY GROUP SE       No  ...           Other   
2       PETRA DIAMONDS LTD       No  ...      Public AIM   
3               HISCOX LTD       No  ...  Public, Quoted   
4  LANCASHIRE HOLDINGS LTD       No  ...  Public, Quoted   

  date_of_incorporation accounting_reference_date registered_accounts_type  \
0                   NaN                       NaN                      NaN   
1            2012-05-11                       NaN                      NaN   
2            1997-03-25                       NaN                      NaN   
3            2006-09-06                       NaN                      NaN   
4            2005-10-12                       NaN                      NaN   

  jordans_company_classification account_currency guo_name guo_bv_d_id_number  \
0               Fame A, full a/c              GBP      NaN                NaN   
1               Fame A, full a/c              GBP      NaN                NaN   
2               Fame A, full a/c              GBP      NaN                NaN   
3               Fame A, full a/c              GBP      NaN                NaN   
4               Fame A, full a/c              GBP      NaN                NaN   

  duo_name duo_bv_d_id_number  
0      NaN                NaN  
1      NaN                NaN  
2      NaN                NaN  
3      NaN                NaN  
4      NaN                NaN  

[5 rows x 26 columns]
```

## lars_yearly

### Number of rows: 2,378,089

### Schema:

```
ibis.Schema {
  registered_number                         string
  company_name                              string
  year                                      string
  consolidated                              string
  employees                                 string
  systemA_industry                          string
  cons_uncons                               string
  turnover_th_gbp                           string
  shareholders_funds_th_gbp                 string
  profit_loss_before_taxation_th_gbp        string
  number_of_employees                       string
  total_assets_th_gbp                       string
  ebitda_th_gbp                             string
  current_liabilities_th_gbp                string
  long_term_liabilities_th_gbp              string
  research_development_th_gbp               string
  wages_salaries_th_gbp                     string
  interest_paid_th_gbp                      string
  taxation_th_gbp                           string
  depreciation_th_gbp                       string
  tangible_assets_th_gbp                    string
  intangible_assets_th_gbp                  string
  fixed_assets_th_gbp                       string
  other_fixed_assets_th_gbp                 string
  pension_costs_th_gbp                      string
  social_security_costs_th_gbp              string
  dividends_distributable_profit_th_gbp     string
  systemB_group                             string
  cost_of_sales_th_gbp                      string
  exceptional_items_pre_gp_th_gbp           string
  cash_out_in_flow_investing_activ_th_gbp   string
  capital_expenditure_financ_invest_th_gbp  string
  acquisition_disposal_th_gbp               string
  equity_dividends_paid_th_gbp              string
  company_name_raw                          string
}
```

### Head of table:

```
  registered_number        company_name  year consolidated employees  \
0           0028326  BLACKSTAR GROUP SE  2013            1        16   
1           0028326  BLACKSTAR GROUP SE  2014            1        13   
2           0028326  BLACKSTAR GROUP SE  2015            1        15   
3           0028326  BLACKSTAR GROUP SE  2016            1        12   
4           0043472     SCOTTY GROUP SE  2011            1        31   

  systemA_industry   cons_uncons turnover_th_gbp shareholders_funds_th_gbp  \
0               58  Consolidated             NaN                     74804   
1               58  Consolidated           13737                     80563   
2               58  Consolidated           22316                    230416   
3               58  Consolidated           19696                    179223   
4               26  Consolidated            5002                      5673   

  profit_loss_before_taxation_th_gbp  ... social_security_costs_th_gbp  \
0                              12203  ...                          NaN   
1                               8168  ...                          NaN   
2                              18384  ...                          NaN   
3                             -33814  ...                          NaN   
4                               -200  ...                          340   

  dividends_distributable_profit_th_gbp   systemB_group cost_of_sales_th_gbp  \
0                                 -1382  58_59_60_61_63                  NaN   
1                                 -1034  58_59_60_61_63                  NaN   
2                                  -647  58_59_60_61_63                  NaN   
3                                  -466  58_59_60_61_63                  NaN   
4                                   NaN           22_30                -2072   

  exceptional_items_pre_gp_th_gbp cash_out_in_flow_investing_activ_th_gbp  \
0                             NaN                                     -37   
1                             NaN                                     -10   
2                             NaN                                      -3   
3                             NaN                                    -171   
4                             NaN                                    -145   

  capital_expenditure_financ_invest_th_gbp acquisition_disposal_th_gbp  \
0                                      NaN                         NaN   
1                                      NaN                         NaN   
2                                      NaN                         NaN   
3                                      NaN                         NaN   
4                                      NaN                         NaN   

  equity_dividends_paid_th_gbp    company_name_raw  
0                        -1382  BLACKSTAR GROUP SE  
1                        -1034  BLACKSTAR GROUP SE  
2                         -647  BLACKSTAR GROUP SE  
3                         -466  BLACKSTAR GROUP SE  
4                          NaN     SCOTTY GROUP SE  

[5 rows x 35 columns]
```

