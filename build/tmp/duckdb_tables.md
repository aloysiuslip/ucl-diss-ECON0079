# Tables in DuckDB database

## fame_fixed

### Number of rows: 2,530,879

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
0        W.& R. BARNETT, LIMITED          NI000166           NaN   
1   FRONTIER AGRICULTURE LIMITED          05288567           NaN   
2         HOOK 2 SISTERS LIMITED          05969169           NaN   
3  OPENFIELD AGRICULTURE LIMITED          03548572           NaN   
4    MCCAIN FOODS (G.B.) LIMITED          00733218           NaN   

                                          ro_address  \
0  Clarendon House, 23 Clarendon Road, Belfast, C...   
1  Group Secretarial Department, 10 Grosvenor Str...   
2               Cote, Bampton, Oxfordshire, OX18 2EG   
3  Honey Pot Lane, Colsterworth, Grantham, Lincol...   
4  Havers Hill, Eastfield, Scarborough, North Yor...   

              ro_address_line_1    ro_address_line_2 ro_address_line_3  \
0               Clarendon House    23 Clarendon Road               NaN   
1  Group Secretarial Department  10 Grosvenor Street               NaN   
2                          Cote                  NaN               NaN   
3                Honey Pot Lane         Colsterworth               NaN   
4                   Havers Hill            Eastfield               NaN   

  ro_address_line_4 ro_address_line_5      ro_city  ...  \
0               NaN               NaN      Belfast  ...   
1               NaN               NaN       London  ...   
2               NaN               NaN      Bampton  ...   
3               NaN               NaN     Grantham  ...   
4               NaN               NaN  Scarborough  ...   

  primary_trading_address_latitude primary_trading_address_longitude  \
0                  54° 36' 24.3" N                    5° 55' 13.8" W   
1                              NaN                               NaN   
2                              NaN                               NaN   
3                  52° 47' 16.0" N                    0° 35' 25.2" W   
4                  54° 14' 19.3" N                    0° 23' 26.7" W   

                     branch_name primary_uk_sic_2007_code  \
0        W.& R. BARNETT, LIMITED                     1430   
1   FRONTIER AGRICULTURE LIMITED                     1610   
2         HOOK 2 SISTERS LIMITED                     1470   
3  OPENFIELD AGRICULTURE LIMITED                     1630   
4    MCCAIN FOODS (G.B.) LIMITED                    10390   

                     primary_uk_sic_2007_description latest_accounts_date  \
0                Raising of horses and other equines           2023-07-31   
1             Support activities for crop production           2024-06-26   
2                                 Raising of poultry           2023-07-31   
3                       Post-harvest crop activities           2023-06-30   
4  Other processing and preserving of fruit and v...           2023-06-30   

  no_of_available_years                           guo guo_nb       entity_type  
0                    20  W&R BARNETT HOLDINGS LIMITED     62  Controlled subs.  
1                    20  FRONTIER AGRICULTURE LIMITED     20               GUO  
2                    17                           NaN      0    Independent co  
3                    20       OPENFIELD GROUP LIMITED      7  Controlled subs.  
4                    20       MCCAIN FOODS GROUP INC.    176  Controlled subs.  

[5 rows x 29 columns]
```

## fame_derived

### Number of rows: 2,530,879

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
0          NI000166           True                   True      False   
1          05288567          False                  False      False   
2          05969169           True                  False      False   
3          03548572           True                   True      False   
4          00733218           True                   True      False   

   has_company_branch_mismatch industry_codes file_codes  
0                        False             01      12_31  
1                        False             01      12_31  
2                        False             01      12_31  
3                        False             01      12_31  
4                        False             01      12_31  
```

## fame_yearly

### Number of rows: 31,568,718

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
  registered_number  year consolidated  turnover  shareholders_funds  \
0          03386933  2023         None       NaN                 NaN   
1          03386933  2015         None       NaN                 NaN   
2          03386933  2010         None       NaN                 NaN   
3          03404547  2014         None       NaN                 NaN   
4          03404547  2018         None       NaN                 NaN   

   profit_loss_pretax employees  tangibles  tangibles_land_and_buildings  \
0                 NaN      None        NaN                           NaN   
1                 NaN      None        NaN                           NaN   
2                 NaN      None        NaN                           NaN   
3                 NaN      None        NaN                           NaN   
4                 NaN      None        NaN                           NaN   

   tangibles_land_freehold  ...  total_assets  liabilites_lt      cos  \
0                      NaN  ...           NaN            NaN      NaN   
1                      NaN  ...           NaN            NaN      NaN   
2                      NaN  ...           NaN            NaN      NaN   
3                      NaN  ...           NaN            NaN -150.632   
4                      NaN  ...           NaN            NaN      NaN   

   dividends  r_and_d  remuneration_employees  wages  social_security_costs  \
0        NaN      NaN                     NaN    NaN                    NaN   
1        NaN      NaN                     NaN    NaN                    NaN   
2        NaN      NaN                     NaN    NaN                    NaN   
3        NaN      NaN                     NaN    NaN                    NaN   
4        NaN      NaN                     NaN    NaN                    NaN   

   pensions_costs  ebitda  
0             NaN   0.073  
1             NaN   0.043  
2             NaN  -0.075  
3             NaN  45.770  
4             NaN  40.944  

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

