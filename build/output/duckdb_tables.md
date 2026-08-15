# Tables in DuckDB database

## fame_yearly

### Number of rows: 48,764,719

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
  tangibles_fixt_fit            float64
  tangibles_plant_and_vehicles  float64
  tangibles_plant               float64
  tangibles_vehicles            float64
  fixed_other                   float64
  intangibles                   float64
  investments_other             float64
  fixed_total                   float64
  liabilities                   float64
  total_assets                  float64
  liabilites_lt                 float64
  cos                           float64
  admin_expenses                float64
  interest_paid                 float64
  profit_loss_pretax2           float64
  tax                           float64
  dividends                     float64
  depreciation                  float64
  r_and_d                       float64
  remuneration_employees        float64
  wages                         float64
  social_security_costs         float64
  pensions_costs                float64
  other_staff_costs             float64
  renumeration_directors        float64
  ebitda                        float64
}
```

### Head of table:

```
  registered_number  year  consolidated  turnover  shareholders_funds  \
0          05930391  2014         False       NaN               6.300   
1          06086182  2009         False       NaN               0.001   
2          06090468  2008         False       NaN               0.280   
3          14263317  2023         False       NaN               0.002   
4          00876306  2010         False       NaN             783.064   

   profit_loss_pretax employees  tangibles  tangibles_land_and_buildings  \
0                 NaN      None        NaN                           NaN   
1                 NaN      None        NaN                           NaN   
2                 NaN      None      1.041                           NaN   
3                 NaN      None        NaN                           NaN   
4                 NaN      None        NaN                           NaN   

   tangibles_land_freehold  tangibles_land_leasehold  tangibles_fixt_fit  \
0                      NaN                       NaN                 NaN   
1                      NaN                       NaN                 NaN   
2                      NaN                       NaN                 NaN   
3                      NaN                       NaN                 NaN   
4                      NaN                       NaN                 NaN   

   tangibles_plant_and_vehicles  tangibles_plant  tangibles_vehicles  \
0                           NaN              NaN                 NaN   
1                           NaN              NaN                 NaN   
2                           NaN              NaN                 NaN   
3                           NaN              NaN                 NaN   
4                           NaN              NaN                 NaN   

   fixed_other  intangibles  investments_other  fixed_total  liabilities  \
0          NaN          NaN                NaN          NaN          NaN   
1          NaN          NaN                NaN          NaN          NaN   
2          NaN          NaN                NaN        1.041       -2.249   
3          NaN          NaN                NaN          NaN          NaN   
4          NaN          NaN                NaN          NaN      -19.633   

   total_assets  liabilites_lt  cos  admin_expenses  interest_paid  \
0         6.300            NaN  NaN             NaN            NaN   
1         0.001            NaN  NaN             NaN            NaN   
2         2.529            NaN  NaN             NaN            NaN   
3         0.002            NaN  NaN             NaN            NaN   
4       802.697            NaN  NaN             NaN            NaN   

   profit_loss_pretax2  tax  dividends  depreciation  r_and_d  \
0                  NaN  NaN        NaN           NaN      NaN   
1                  NaN  NaN        NaN           NaN      NaN   
2                  NaN  NaN        NaN         0.334      NaN   
3                  NaN  NaN        NaN           NaN      NaN   
4                  NaN  NaN        NaN           NaN      NaN   

   remuneration_employees  wages  social_security_costs  pensions_costs  \
0                     NaN    NaN                    NaN             NaN   
1                     NaN    NaN                    NaN             NaN   
2                     NaN    NaN                    NaN             NaN   
3                     NaN    NaN                    NaN             NaN   
4                     NaN    NaN                    NaN             NaN   

   other_staff_costs  renumeration_directors  ebitda  
0                NaN                     NaN     NaN  
1                NaN                     NaN     NaN  
2                NaN                     NaN     NaN  
3                NaN                     NaN     NaN  
4                NaN                     NaN     NaN  
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

            company_name_B inactive quoted own_data woco bv_d_id_number  \
0       BLACKSTAR GROUP SE       No     No       No   No     GBH0028326   
1          SCOTTY GROUP SE       No     No       No   No     GBH0043472   
2       PETRA DIAMONDS LTD       No     No       No   No     GBH0053787   
3               HISCOX LTD       No    Yes       No   No     GBH0054897   
4  LANCASHIRE HOLDINGS LTD       No    Yes       No   No     GBH0056130   

  company_status status_date      legal_form date_of_incorporation  \
0         Active         NaN      Public AIM                   NaN   
1         Active         NaN           Other            2012-05-11   
2         Active         NaN      Public AIM            1997-03-25   
3         Active         NaN  Public, Quoted            2006-09-06   
4         Active         NaN  Public, Quoted            2005-10-12   

  accounting_reference_date registered_accounts_type  \
0                       NaN                      NaN   
1                       NaN                      NaN   
2                       NaN                      NaN   
3                       NaN                      NaN   
4                       NaN                      NaN   

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

  profit_loss_before_taxation_th_gbp number_of_employees total_assets_th_gbp  \
0                              12203                  16               75701   
1                               8168                  13               85856   
2                              18384                  15              254899   
3                             -33814                  12              200788   
4                               -200                  31                7517   

  ebitda_th_gbp current_liabilities_th_gbp long_term_liabilities_th_gbp  \
0         12233                       -882                          -15   
1          8587                      -5292                           -1   
2         18730                     -24475                           -8   
3        -31522                     -21500                          -65   
4          3805                      -1684                         -159   

  research_development_th_gbp wages_salaries_th_gbp interest_paid_th_gbp  \
0                         NaN                  1674                 -223   
1                         NaN                   NaN                 -489   
2                         NaN                   NaN                 -322   
3                         NaN                   NaN                -2334   
4                         NaN                  1709                  -27   

  taxation_th_gbp depreciation_th_gbp tangible_assets_th_gbp  \
0              15                  16                     78   
1               8                  12                     66   
2              15                   6                     56   
3             -45                  16                    222   
4             287                  88                    214   

  intangible_assets_th_gbp fixed_assets_th_gbp other_fixed_assets_th_gbp  \
0                       51               67937                       NaN   
1                       49               82094                       NaN   
2                      NaN              252167                       NaN   
3                      NaN              199901                       NaN   
4                     4971                5672                       NaN   

  pension_costs_th_gbp social_security_costs_th_gbp  \
0                  NaN                          NaN   
1                  NaN                          NaN   
2                  NaN                          NaN   
3                  NaN                          NaN   
4                  NaN                          340   

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
```

## fame_fixed

### Number of rows: 8,323,347

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
  industry_codes                     string
  file_codes                         string
}
```

### Head of table:

```
                     company_name registered_number ticker_symbol  \
0   SERISABELLE (DEGANWY) LIMITED          09889640           NaN   
1       PERFECT SOLUTIONS INT LTD          09889655           NaN   
2     THE STRENGTH TEMPLE LIMITED          09889705           NaN   
3  SIMPLY HAIR EXTENSIONS LIMITED          09889730           NaN   
4   I.K ENTERPRISE LONDON LIMITED          09889745           NaN   

                                          ro_address  \
0  2nd Floor, London House, London Road South, Po...   
1  Unit 6 859A High Road, Goodmayes, Ilford, Esse...   
2  360 House 7 Cambridge Court, 210 Shepherds Bus...   
3  c/o Cheryl Taylor, 2 The Chaplin Wrotham Road,...   
4  Grand Union House, 20 Kentish Town Road, Londo...   

             ro_address_line_1           ro_address_line_2 ro_address_line_3  \
0      2nd Floor, London House           London Road South           Poynton   
1        Unit 6 859A High Road                   Goodmayes               NaN   
2  360 House 7 Cambridge Court     210 Shepherds Bush Road               NaN   
3            c/o Cheryl Taylor  2 The Chaplin Wrotham Road     Borough Green   
4            Grand Union House        20 Kentish Town Road               NaN   

  ro_address_line_4 ro_address_line_5    ro_city ro_county ro_postcode  \
0               NaN               NaN  Stockport  Cheshire        SK12   
1               NaN               NaN     Ilford     Essex        IG 3   
2               NaN               NaN     London    London        W  6   
3               NaN               NaN  Sevenoaks      Kent        TN15   
4               NaN               NaN     London    London        NW 1   

  ro_full_postcode ro_country      ro_latitude    ro_longitude  \
0         SK12 1YP    England  53° 20' 39.9" N   2° 7' 32.3" W   
1          IG3 8TG    England              NaN             NaN   
2           W6 7NJ    England              NaN             NaN   
3         TN15 8DB    England  51° 17' 44.7" N  0° 18' 31.1" E   
4          NW1 9NX    England  51° 32' 26.9" N   0° 8' 31.7" W   

         ro_nuts_region ro_postal_region  \
0  North West (England)       North West   
1                London     London Outer   
2                London     London Inner   
3  South East (England)    South Eastern   
4                London     London Inner   

                             primary_trading_address  \
0                                                NaN   
1                                                NaN   
2                                                NaN   
3  c/o Cheryl Taylor, 2 The Chaplin Wrotham Road,...   
4                                                NaN   

  primary_trading_address_latitude primary_trading_address_longitude  \
0                              NaN                               NaN   
1                              NaN                               NaN   
2                              NaN                               NaN   
3                  51° 17' 44.7" N                    0° 18' 31.1" E   
4                              NaN                               NaN   

                      branch_name  primary_uk_sic_2007_code  \
0                             NaN                     96090   
1                             NaN                     96090   
2                             NaN                     96040   
3  SIMPLY HAIR EXTENSIONS LIMITED                     96020   
4                             NaN                     96090   

            primary_uk_sic_2007_description latest_accounts_date  \
0  Other personal service activities n.e.c.           2016-11-30   
1  Other personal service activities n.e.c.           2016-11-30   
2            Physical well-being activities           2017-11-30   
3   Hairdressing and other beauty treatment           2020-11-30   
4  Other personal service activities n.e.c.           2016-11-30   

   no_of_available_years  guo  guo_nb      entity_type industry_codes  \
0                      1  NaN       0  Single location             96   
1                      1  NaN       0  Single location             96   
2                      2  NaN       0  Single location             96   
3                      5  NaN       0  Single location             96   
4                      1  NaN       0  Single location             96   

  file_codes  
0    17_37 2  
1    17_37 2  
2    17_37 2  
3    17_37 2  
4    17_37 2  
```

