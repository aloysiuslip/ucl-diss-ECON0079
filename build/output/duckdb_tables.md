# Tables in DuckDB database

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

### Number of rows: 155,170

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
0              BREEDON TRADING LIMITED          00156531           NaN   
1                    MOUCHEL GROUP PLC          00095369          MCHL   
2  FERROVIAL CONSTRUCTION (UK) LIMITED          05779755           NaN   
3                    FP MCCANN LIMITED          NI013563           NaN   
4                CLANCY DOCWRA LIMITED          00432242           NaN   

                                          ro_address     ro_address_line_1  \
0   Breedon-On-The-Hill, Derby, Derbyshire, DE73 8AP   Breedon-On-The-Hill   
1  c/o Kpmg Llp, 8 Salisbury Square, London, EC4Y...          c/o Kpmg Llp   
2  3rd Floor Building 5, Chiswick Business Park, ...  3rd Floor Building 5   
3  Knockloughrim Quarry, 3 Drumard Road, Magheraf...  Knockloughrim Quarry   
4  Clare House, Coppermill Lane, Harefield, Uxbri...           Clare House   

        ro_address_line_2 ro_address_line_3 ro_address_line_4  \
0                     NaN               NaN               NaN   
1      8 Salisbury Square               NaN               NaN   
2  Chiswick Business Park               NaN               NaN   
3          3 Drumard Road               NaN               NaN   
4         Coppermill Lane         Harefield               NaN   

  ro_address_line_5      ro_city           ro_county ro_postcode  \
0               NaN        Derby          Derbyshire        DE73   
1               NaN       London              London        EC4Y   
2               NaN       London              London        W  4   
3               NaN  Magherafelt  County Londonderry        BT45   
4               NaN     Uxbridge           Middlesex        UB 9   

  ro_full_postcode        ro_country      ro_latitude    ro_longitude  \
0         DE73 8AP           England              NaN             NaN   
1         EC4Y 8BB           England              NaN             NaN   
2           W4 5YF           England              NaN             NaN   
3         BT45 8QA  Northern Ireland  54° 49' 28.3" N  6° 35' 14.9" W   
4          UB9 6HZ           England  51° 36' 39.6" N   0° 30' 0.9" W   

            ro_nuts_region  ro_postal_region primary_trading_address  \
0  East Midlands (England)     East Midlands                     NaN   
1                   London      London Inner                     NaN   
2                   London      London Inner                     NaN   
3         Northern Ireland  Northern Ireland                     NaN   
4          East of England      London Outer                     NaN   

  primary_trading_address_latitude primary_trading_address_longitude  \
0                              NaN                               NaN   
1                              NaN                               NaN   
2                  51° 29' 32.6" N                    0° 16' 30.1" W   
3                  54° 49' 28.3" N                    6° 35' 14.9" W   
4                  51° 36' 39.6" N                     0° 30' 0.9" W   

                           branch_name  primary_uk_sic_2007_code  \
0              BREEDON TRADING LIMITED                      8110   
1                                  NaN                     42110   
2  FERROVIAL CONSTRUCTION (UK) LIMITED                     42110   
3                    FP MCCANN LIMITED                      8110   
4                CLANCY DOCWRA LIMITED                     42910   

                     primary_uk_sic_2007_description latest_accounts_date  \
0  Quarrying of ornamental and building stone, li...           2023-12-31   
1                Construction of roads and motorways           2011-07-31   
2                Construction of roads and motorways           2023-12-31   
3  Quarrying of ornamental and building stone, li...           2023-12-31   
4                     Construction of water projects           2024-03-31   

   no_of_available_years                            guo  guo_nb  \
0                     20              BREEDON GROUP PLC      70   
1                     20                            NaN       0   
2                     18                   FERROVIAL SE     411   
3                     20        FP MCCANN GROUP LIMITED       3   
4                     20  CLANCY GROUP HOLDINGS LIMITED       9   

        entity_type industry_codes         file_codes  
0  Controlled subs.          08,42        12_44,11_53  
1   Single location             42              11_53  
2  Controlled subs.             42              11_53  
3  Controlled subs.       08,23,42  12_44,22_17,11_53  
4  Controlled subs.             42              11_53  
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

## fame_yearly

### Number of rows: 1,128,490

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
  registered_number  year  consolidated   turnover  shareholders_funds  \
0          02363341  2006          True  12660.069             101.130   
1          00950699  2006         False   5456.697            2648.863   
2          03118893  2006          True  14709.910             162.534   
3          03026300  2006         False  28928.515            7206.625   
4          SC060639  2006         False        NaN            1045.717   

   profit_loss_pretax  employees  tangibles  tangibles_land_and_buildings  \
0              37.832         72     63.857                           NaN   
1              23.111         37     92.091                           NaN   
2            -177.649         15     53.624                           NaN   
3             808.949         52   2156.315                       1870.25   
4             151.178         64    418.020                           NaN   

   tangibles_land_freehold  tangibles_land_leasehold  tangibles_fixt_fit  \
0                      NaN                       NaN                 NaN   
1                      NaN                       NaN                 NaN   
2                      NaN                       NaN               8.937   
3                      NaN                       NaN              31.950   
4                      NaN                       NaN              20.449   

   tangibles_plant_and_vehicles  tangibles_plant  tangibles_vehicles  \
0                           NaN              NaN                 NaN   
1                           NaN              NaN                 NaN   
2                        44.687              NaN                 NaN   
3                       254.115              NaN                 NaN   
4                       397.571              NaN                 NaN   

   fixed_other  intangibles  investments_other  fixed_total  liabilities  \
0          NaN          NaN                NaN       63.857    -5406.286   
1          NaN          NaN                NaN       92.092    -2295.513   
2          NaN          NaN                4.1       57.724    -1947.226   
3          NaN        0.001                NaN     2156.316    -6017.700   
4          NaN          NaN                NaN      418.020    -2897.758   

   total_assets  liabilites_lt        cos  admin_expenses  interest_paid  \
0      5664.607       -157.191 -10587.042             NaN            NaN   
1      4944.376            NaN        NaN             NaN            NaN   
2      2109.760            NaN -13387.445       -1579.087        -63.764   
3     13224.325            NaN -25192.719       -2983.502            NaN   
4      3993.700        -50.225        NaN       -1545.316        -51.188   

   profit_loss_pretax2      tax  dividends  depreciation  r_and_d  \
0                  NaN      NaN        NaN           NaN      NaN   
1                  NaN      NaN        NaN           NaN      NaN   
2             -177.649   17.647        NaN           NaN      NaN   
3              808.949 -229.190        NaN       172.979      NaN   
4              151.178  -22.991        NaN        79.220      NaN   

   remuneration_employees     wages  social_security_costs  pensions_costs  \
0               10336.112  8672.321                937.947         725.844   
1                1002.630   917.443                 85.187             NaN   
2                 418.627   382.495                 36.132             NaN   
3                1936.019  1655.821                181.738          98.460   
4                2154.140  1727.193                182.815         244.132   

   other_staff_costs  renumeration_directors   ebitda  
0                NaN                     NaN   -9.903  
1                NaN                     NaN   65.791  
2                NaN                     NaN -256.622  
3                NaN                 428.642  925.273  
4                NaN                 807.377  264.045  
```

