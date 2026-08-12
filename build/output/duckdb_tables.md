# Tables in DuckDB database

## fame_fixed

### Number of rows: 2,419,878

### Schema:

```
ibis.Schema {
  company_name                       string
  registered_number                  string
  ticker_symbol                      string
  ro_address                         string
  ro_address_line_1                  string
  ro_address_line_2                  string
  ro_address_line_3                  string
  ro_address_line_4                  string
  ro_address_line_5                  string
  ro_city                            string
  ro_county                          string
  ro_postcode                        string
  ro_full_postcode                   string
  ro_country                         string
  ro_latitude                        string
  ro_longitude                       string
  ro_nuts_region                     string
  ro_postal_region                   string
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
                          company_name registered_number ticker_symbol  \
0                     NKS SOFTWARE LTD          10323124           NaN   
1  PIVOTAL CONSULTING SERVICES LIMITED          10323176           NaN   
2           SIDETONE TELECOMMS LIMITED          10323183           NaN   
3           TURQUOISE SOFTWARE LIMITED          10323222           NaN   
4                      CLOUD 8 LIMITED          10323223           NaN   

                                          ro_address  \
0  10 Brassie Close, Basingstoke, Hampshire, RG24...   
1  7 Rutland Road, Westwood, Nottingham, Nottingh...   
2  Premier Suite 4 Churchill Court, 58 Station Ro...   
3  Plaza 8 Kd Tower, Cotterells, Hemel Hempstead,...   
4         Kemp House 160 City Road, London, EC1V 2NX   

                 ro_address_line_1 ro_address_line_2 ro_address_line_3  \
0                 10 Brassie Close               NaN               NaN   
1                   7 Rutland Road          Westwood               NaN   
2  Premier Suite 4 Churchill Court   58 Station Road             North   
3                 Plaza 8 Kd Tower        Cotterells               NaN   
4         Kemp House 160 City Road               NaN               NaN   

  ro_address_line_4 ro_address_line_5          ro_city  ...  \
0               NaN               NaN      Basingstoke  ...   
1               NaN               NaN       Nottingham  ...   
2               NaN               NaN           Harrow  ...   
3               NaN               NaN  Hemel Hempstead  ...   
4               NaN               NaN           London  ...   

  primary_trading_address_latitude primary_trading_address_longitude  \
0                              NaN                               NaN   
1                   53° 3' 36.5" N                    1° 19' 32.8" W   
2                              NaN                               NaN   
3                              NaN                               NaN   
4                              NaN                               NaN   

                           branch_name primary_uk_sic_2007_code  \
0                     NKS SOFTWARE LTD                    62020   
1  PIVOTAL CONSULTING SERVICES LIMITED                    62090   
2                                  NaN                    62090   
3           TURQUOISE SOFTWARE LIMITED                    62020   
4                                  NaN                    62020   

                     primary_uk_sic_2007_description latest_accounts_date  \
0                    Computer consultancy activities           2024-08-31   
1  Other information technology and computer serv...           2024-08-31   
2  Other information technology and computer serv...           2021-08-31   
3                    Computer consultancy activities           2018-08-31   
4                    Computer consultancy activities           2017-08-31   

  no_of_available_years  guo guo_nb      entity_type  
0                     8  NaN      0   Independent co  
1                     8  NaN      0   Independent co  
2                     5  NaN      0  Single location  
3                     2  NaN      0  Single location  
4                     1  NaN      0  Single location  

[5 rows x 29 columns]
```

## fame_derived

### Number of rows: 2,491,459

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
  registered_number  has_ptaddress  has_ptaddress_latlong  is_public  \
0          10523260           True                   True      False   
1          10523294          False                  False      False   
2          10523302           True                   True      False   
3          10523398          False                  False      False   
4          10523406          False                  False      False   

  has_company_branch_mismatch industry_codes file_codes  
0                       False             62    18_37 1  
1                        None             62    18_37 1  
2                       False             62    18_37 1  
3                       False             62    18_37 1  
4                       False             62    18_37 1  
```

## fame_yearly

### Number of rows: 14,009,970

### Schema:

```
ibis.Schema {
  registered_number             string
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
  registered_number  year  consolidated  turnover  shareholders_funds  \
0          09324129  2019         False       NaN               5.030   
1          09326979  2016         False       NaN               0.178   
2          09368629  2016         False       NaN               0.001   
3          SC621085  2022         False       NaN              -2.100   
4          SC631312  2021         False       NaN               8.197   

   profit_loss_pretax  employees  tangibles  tangibles_land_and_buildings  \
0                 NaN        NaN        NaN                           NaN   
1                 NaN        NaN        NaN                           NaN   
2                 NaN        NaN        NaN                           NaN   
3                 NaN        1.0        NaN                           NaN   
4                 NaN        1.0      3.974                           NaN   

   tangibles_land_freehold  ...  total_assets  liabilites_lt  cos  dividends  \
0                      NaN  ...         5.030            NaN  NaN        NaN   
1                      NaN  ...         5.810            NaN  NaN        NaN   
2                      NaN  ...         1.013            NaN  NaN        NaN   
3                      NaN  ...         0.082            NaN  NaN        NaN   
4                      NaN  ...        10.462            NaN  NaN        NaN   

   r_and_d  remuneration_employees  wages  social_security_costs  \
0      NaN                     NaN    NaN                    NaN   
1      NaN                     NaN    NaN                    NaN   
2      NaN                     NaN    NaN                    NaN   
3      NaN                     NaN    NaN                    NaN   
4      NaN                     NaN    NaN                    NaN   

   pensions_costs  ebitda  
0             NaN     NaN  
1             NaN     NaN  
2             NaN     NaN  
3             NaN     NaN  
4             NaN     NaN  

[5 rows x 25 columns]
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

