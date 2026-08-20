# Other Tables in DuckDB database

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

