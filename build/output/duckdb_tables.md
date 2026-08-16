# Tables in DuckDB database

## fame_fixed

### Number of rows: 9,283,479

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
  primary_uk_sic_2007_code           float64
  primary_uk_sic_2007_description    string
  latest_accounts_date               timestamp(6)
  no_of_available_years              int64
  guo                                string
  guo_nb                             float64
  entity_type                        string
  industry_codes                     string
  file_codes                         string
}
```

### Head of table:

```
                    company_name registered_number ticker_symbol  \
0              RUM COMMITTEE LTD          10682986           NaN   
1         THE DRAMA ROOM LIMITED          10683009           NaN   
2                NO DOOR THEATRE          10683173           NaN   
3  WEST COUNTRY CREATIVE LIMITED          10683266           NaN   
4              AVO MUSIC LIMITED          10683268           NaN   

                                          ro_address  \
0  15 - 17 (Werks Central, Middle Street, Brighto...   
1  Unit A - 82 James Carter Road, Mildenhall Indu...   
2  7 Winterbrook Lane, Wallingford, Oxfordshire, ...   
3  Plowden Park, Newton Down, Lifton, Devon, PL16...   
4  Malverleys, East End, Newbury, Berkshire, RG20...   

               ro_address_line_1             ro_address_line_2  \
0        15 - 17 (Werks Central)                 Middle Street   
1  Unit A - 82 James Carter Road  Mildenhall Industrial Estate   
2             7 Winterbrook Lane                           NaN   
3                   Plowden Park                   Newton Down   
4                     Malverleys                      East End   

  ro_address_line_3 ro_address_line_4 ro_address_line_5          ro_city  \
0               NaN               NaN               NaN         Brighton   
1               NaN               NaN               NaN  Bury St Edmunds   
2               NaN               NaN               NaN      Wallingford   
3               NaN               NaN               NaN           Lifton   
4               NaN               NaN               NaN          Newbury   

     ro_county ro_postcode ro_full_postcode ro_country      ro_latitude  \
0  East Sussex        BN 1          BN1 1AL    England  50° 49' 18.1" N   
1      Suffolk        IP28         IP28 7DE    England  52° 21' 13.2" N   
2  Oxfordshire        OX10         OX10 9EH    England  51° 35' 30.0" N   
3        Devon        PL16         PL16 0AS    England              NaN   
4    Berkshire        RG20         RG20 0AA    England              NaN   

    ro_longitude        ro_nuts_region ro_postal_region  \
0  0° 8' 35.1" W  South East (England)    South Eastern   
1  0° 30' 3.2" E       East of England          Eastern   
2  1° 7' 47.9" W  South East (England)         Southern   
3            NaN  South West (England)    South Western   
4            NaN  South East (England)         Southern   

                             primary_trading_address  \
0                                                NaN   
1                                                NaN   
2  7 Winterbrook Lane, Wallingford, Oxfordshire, ...   
3  Plowden Park, Newton Down, Lifton, Devon, PL16...   
4                                                NaN   

  primary_trading_address_latitude primary_trading_address_longitude  \
0                              NaN                               NaN   
1                              NaN                               NaN   
2                  51° 35' 30.0" N                     1° 7' 47.9" W   
3                              NaN                               NaN   
4                              NaN                               NaN   

                     branch_name  primary_uk_sic_2007_code  \
0                            NaN                   59200.0   
1         THE DRAMA ROOM LIMITED                   90010.0   
2                NO DOOR THEATRE                   90010.0   
3  WEST COUNTRY CREATIVE LIMITED                   90030.0   
4              AVO MUSIC LIMITED                   90020.0   

                   primary_uk_sic_2007_description latest_accounts_date  \
0  Sound recording and music publishing activities           2024-03-31   
1                                  Performing arts           2019-03-26   
2                                  Performing arts           2024-03-31   
3                                Artistic creation           2023-03-31   
4            Support activities to performing arts           2023-12-31   

   no_of_available_years                         guo  guo_nb  \
0                      7                         NaN     0.0   
1                      2                         NaN     0.0   
2                      7                         NaN     0.0   
3                      6                         NaN     0.0   
4                      7  MS ALLEGRA SOPHIA VON OPEL     2.0   

        entity_type industry_codes       file_codes  
0    Independent co          59,90  18_18 3,17_03 3  
1   Single location             90          17_03 3  
2   Single location             90          17_03 3  
3   Single location             90          17_03 3  
4  Controlled subs.             90          17_03 3  
```

## fame_yearly

### Number of rows: 44,865,127

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
0          03767701  2006         False       NaN               0.031   
1          04863460  2006         False      0.25               0.001   
2          02776047  2006         False       NaN           -7691.182   
3          SC235667  2006         False       NaN             -19.739   
4          04655770  2006         False       NaN              14.801   

   profit_loss_pretax employees  tangibles  tangibles_land_and_buildings  \
0                 NaN      None      8.425                           NaN   
1              -0.059      None        NaN                           NaN   
2            -967.394      None        NaN                           NaN   
3                 NaN      None        NaN                           NaN   
4                 NaN      None      0.775                           NaN   

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
0          NaN          NaN                NaN        8.425      -45.716   
1          NaN          NaN                NaN          NaN       -0.255   
2          NaN          NaN           2903.297     2903.297   -10594.480   
3          NaN         20.0                NaN       20.000      -39.739   
4          NaN         10.5                NaN       11.275          NaN   

   total_assets  liabilites_lt  cos  admin_expenses  interest_paid  \
0        46.465         -0.718  NaN             NaN            NaN   
1         0.256            NaN  NaN          -0.309            NaN   
2      2903.298            NaN  NaN        -708.992       -258.402   
3        20.000            NaN  NaN             NaN            NaN   
4        14.801            NaN  NaN             NaN            NaN   

   profit_loss_pretax2    tax  dividends  depreciation  r_and_d  \
0                  NaN    NaN        NaN         1.877      NaN   
1               -0.059  0.059        NaN           NaN      NaN   
2             -967.394    NaN        NaN           NaN      NaN   
3                  NaN    NaN        NaN           NaN      NaN   
4                  NaN    NaN        NaN         0.257      NaN   

   remuneration_employees  wages  social_security_costs  pensions_costs  \
0                     NaN    NaN                    NaN             NaN   
1                     NaN    NaN                    NaN             NaN   
2                     NaN    NaN                    NaN             NaN   
3                     NaN    NaN                    NaN             NaN   
4                     NaN    NaN                    NaN             NaN   

   other_staff_costs  renumeration_directors   ebitda  
0                NaN                     NaN      NaN  
1                NaN                     NaN   -0.059  
2                NaN                     NaN -708.992  
3                NaN                     NaN      NaN  
4                NaN                     NaN      NaN  
```

## fame_fixed_filtered

### Number of rows: 152,379

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
0              AUSTIN HAIR DESIGN LIMITED          04904074           NaN   
1                 PURELY CREATIVE LIMITED          05191793           NaN   
2      KINGSTON (T2) HAIRDRESSING LIMITED          05198559           NaN   
3          GROUP DIRECT MARKETING LIMITED          05602909           NaN   
4  COMMISSION FOR THE NEW ECONOMY LIMITED          05678007           NaN   

                                          ro_address  \
0  The Poplars, Bridge Street, Brigg, South Humbe...   
1  Kings Buildings, Lydney, Gloucestershire, GL15...   
2  Berkeley House, Amery Street, Alton, Hampshire...   
3  Markerstudy House, 45 Westerham Road, Sevenoak...   
4  Frp Advisory Trading Lmited, 4th Floor Abbey H...   

             ro_address_line_1     ro_address_line_2 ro_address_line_3  \
0   The Poplars, Bridge Street                   NaN               NaN   
1              Kings Buildings                   NaN               NaN   
2               Berkeley House          Amery Street               NaN   
3            Markerstudy House     45 Westerham Road               NaN   
4  Frp Advisory Trading Lmited  4th Floor Abbey Houe               NaN   

  ro_address_line_4 ro_address_line_5     ro_city         ro_county  \
0               NaN               NaN       Brigg  South Humberside   
1               NaN               NaN      Lydney   Gloucestershire   
2               NaN               NaN       Alton         Hampshire   
3               NaN               NaN   Sevenoaks              Kent   
4               NaN               NaN  Manchester        Lancashire   

  ro_postcode ro_full_postcode ro_country      ro_latitude    ro_longitude  \
0        DN20         DN20 8NQ    England   53° 33' 3.6" N  0° 29' 50.4" W   
1        GL15         GL15 5HE    England              NaN             NaN   
2        GU34         GU34 1HN    England   51° 8' 58.6" N  0° 58' 39.6" W   
3        TN13         TN13 2OB    England  51° 16' 46.4" N   0° 9' 19.9" E   
4        M  2           M2 4AB    England              NaN             NaN   

             ro_nuts_region    ro_postal_region  \
0  Yorkshire and The Humber  Yorks & Humberside   
1      South West (England)       South Western   
2      South East (England)            Southern   
3                       NaN       South Eastern   
4      North West (England)          North West   

                             primary_trading_address  \
0                                                NaN   
1                                                NaN   
2  Berkeley House, Amery Street, Alton, Hampshire...   
3                                                NaN   
4                                                NaN   

  primary_trading_address_latitude primary_trading_address_longitude  \
0                              NaN                               NaN   
1                              NaN                               NaN   
2                  51° 30' 51.9" N                    0° 33' 25.8" W   
3                              NaN                               NaN   
4                              NaN                               NaN   

                              branch_name  primary_uk_sic_2007_code  \
0              AUSTIN HAIR DESIGN LIMITED                     96020   
1                 PURELY CREATIVE LIMITED                     96090   
2      KINGSTON (T2) HAIRDRESSING LIMITED                     96020   
3          GROUP DIRECT MARKETING LIMITED                     96090   
4  COMMISSION FOR THE NEW ECONOMY LIMITED                     96090   

            primary_uk_sic_2007_description latest_accounts_date  \
0   Hairdressing and other beauty treatment           2019-09-30   
1  Other personal service activities n.e.c.           2017-12-31   
2   Hairdressing and other beauty treatment           2023-08-31   
3  Other personal service activities n.e.c.           2023-12-31   
4  Other personal service activities n.e.c.           2020-03-31   

   no_of_available_years                                                guo  \
0                     16                                                NaN   
1                     13                                                NaN   
2                     19                                  MR COLIN CAMPBELL   
3                     18                                VENUS TOPCO LIMITED   
4                     14  ASSOCIATION OF GREATER MANCHESTER AUTHORITIES THE   

   guo_nb       entity_type industry_codes file_codes  
0       0   Single location             96    17_35 2  
1       0   Single location             96    17_35 2  
2       2  Controlled subs.             96    17_35 2  
3      31  Controlled subs.             96    17_35 2  
4       2  Controlled subs.             96    17_35 2  
```

## fame_yearly_filtered

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
  registered_number  year  consolidated     turnover  shareholders_funds  \
0          00449956  2024          True     9147.162            3799.237   
1          05195191  2024          True  1103700.000           -3300.000   
2          04724733  2024         False    20173.497             329.829   
3          00040000  2024         False    17729.000           13302.000   
4          01468061  2024         False    20515.353            9423.725   

   profit_loss_pretax  employees  tangibles  tangibles_land_and_buildings  \
0             394.044         64   5327.099                      4759.984   
1           34100.000       1431   9700.000                      3300.000   
2           -1039.167        186   1372.443                       576.119   
3             270.000        291   4530.000                      1389.000   
4             547.198        133    414.028                       150.728   

   tangibles_land_freehold  tangibles_land_leasehold  tangibles_fixt_fit  \
0                 4759.984                       NaN                 NaN   
1                      NaN                  3300.000              1600.0   
2                      NaN                   576.119                 NaN   
3                 1389.000                       NaN                 NaN   
4                      NaN                   150.728                 NaN   

   tangibles_plant_and_vehicles  tangibles_plant  tangibles_vehicles  \
0                       567.115          493.685               73.43   
1                      4800.000              NaN                 NaN   
2                           NaN              NaN                 NaN   
3                      2911.000         2911.000                 NaN   
4                           NaN              NaN                 NaN   

   fixed_other  intangibles  investments_other  fixed_total  liabilities  \
0          NaN      620.785                NaN     5947.884    -5924.989   
1          NaN    31900.000           5900.000    47500.000  -135300.000   
2      796.324          NaN              0.001     1372.444    -5955.585   
3      230.000          NaN            730.000     5260.000    -1751.000   
4       69.026      153.816                NaN      568.044    -3478.640   

   total_assets  liabilites_lt          cos  admin_expenses  interest_paid  \
0     12926.217      -3201.991    -4286.532       -4224.588       -273.822   
1    179600.000     -47600.000 -1030500.000      -34100.000      -6300.000   
2      6532.487       -247.073   -10337.511       -7062.094         -4.619   
3     16145.000      -1092.000    -9437.000       -8363.000            NaN   
4     12902.365            NaN   -10199.462             NaN            NaN   

   profit_loss_pretax2       tax  dividends  depreciation  r_and_d  \
0              394.044  -158.456        NaN       348.489      NaN   
1            34100.000 -8600.000   -10800.0      2200.000      NaN   
2            -1039.167  -340.374        NaN       403.942      NaN   
3              270.000  -245.000      -94.0       632.000      NaN   
4                  NaN       NaN        NaN           NaN  699.426   

   remuneration_employees      wages  social_security_costs  pensions_costs  \
0                2175.147   1945.015                190.813          39.319   
1               45000.000  39400.000               3600.000        1100.000   
2                7510.733   6233.949               1209.128          67.656   
3                8109.000   7127.000                355.000         627.000   
4                6215.228   5463.645                584.866         166.717   

   other_staff_costs  renumeration_directors     ebitda  
0                NaN                 271.946   1133.982  
1              900.0                2884.000  48500.000  
2                NaN                2186.252   3177.834  
3                NaN                 520.000    561.000  
4                NaN                     NaN    626.124  
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

