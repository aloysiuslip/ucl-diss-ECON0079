# Other Tables in DuckDB database

## spatial_groups

### Number of rows: 1,171,378

### Schema:

```
ibis.Schema {
  registered_number        string
  year                     int64
  employees                int64
  average_wage             float64
  gva1                     float64
  gva2                     float64
  gva1_per_worker          float64
  gva2_per_worker          float64
  registered_number_right  string
  company_name             string
  is_public                boolean
  industry_codes           string
  file_codes               string
  sic6                     int64
  sic6_desc                string
  lat_dec                  float64
  lon_dec                  float64
  address_lvl              int64
  address_case             string
  ttwa                     string
  pc4                      string
  lat_lon5                 string
}
```

### Head of table:

```
  registered_number  year  employees  average_wage           gva1  gva2  \
0          01840419  2006       4029     32.548202  220307.818391   NaN   
1          01372811  2006         55     42.390261     688.614601   NaN   
2          02468057  2006         47     43.113194    2062.989386   NaN   
3          SC010677  2006       6729     27.417540  380625.557672   NaN   
4          03221027  2006         26     48.352391     301.723619   NaN   

   gva1_per_worker  gva2_per_worker registered_number_right  \
0        54.680521              NaN                01840419   
1        12.520265              NaN                01372811   
2        43.893391              NaN                02468057   
3        56.564951              NaN                SC010677   
4        11.604755              NaN                03221027   

                       company_name  is_public industry_codes file_codes  \
0  WICKES BUILDING SUPPLIES LIMITED      False             47      22_16   
1           MAPA SPONTEX UK LIMITED      False             47      22_16   
2                NISBETS RETAIL LTD      False             47      22_16   
3    HF STORES REALISATIONS LIMITED      False             47      22_16   
4             GAMEPLAY (GB) LIMITED      False             47      22_16   

    sic6                                          sic6_desc    lat_dec  \
0  47789  Other retail sale of new goods in specialised ...  52.261361   
1  47190        Other retail sale in non-specialised stores  52.213889   
2  47789  Other retail sale of new goods in specialised ...  51.504472   
3  47190        Other retail sale in non-specialised stores  55.946083   
4  47540  Retail sale of electrical household appliances...  51.504581   

    lon_dec  address_lvl address_case       ttwa   pc4           lat_lon5  
0 -0.943639            1          pta  E30000237  WD24  52.26136,-0.94364  
1 -2.173194            1          pta  E30000288  WS13  52.21389,-2.17319  
2 -2.538472            1           ro  E30000180  BS16  51.50447,-2.53847  
3 -3.211278            1           ro  S22000059   EH3  55.94608,-3.21128  
4 -0.081286            2           ro  E30000234   SE1  51.50458,-0.08129  
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

## spatial_panel_view

### Number of rows: 1,087,683

### Schema:

```
ibis.Schema {
  registered_number        string
  year                     int64
  employees                int64
  average_wage             float64
  gva1                     float64
  gva2                     float64
  gva1_per_worker          float64
  gva2_per_worker          float64
  registered_number_right  string
  company_name             string
  is_public                boolean
  industry_codes           string
  file_codes               string
  sic6                     int64
  sic6_desc                string
  lat_dec                  float64
  lon_dec                  float64
  address_lvl              int64
  address_case             string
  pc8                      string
  ttwa                     string
  pc4                      string
  lat_lon5                 string
}
```

### Head of table:

```
  registered_number  year  employees  average_wage          gva1  \
0          04050764  2011         28     17.554484    609.255814   
1          04110724  2007         35    111.963202   3200.937508   
2          01180742  2007        155     41.481763   6830.273395   
3          07728211  2019       2471     19.836178  52623.965344   
4          02492078  2006         24     43.487334   1359.578830   

           gva2  gva1_per_worker  gva2_per_worker registered_number_right  \
0           NaN        21.759136              NaN                04050764   
1   3171.282562        91.455357        90.608073                04110724   
2           NaN        44.066280              NaN                01180742   
3  55642.790463        21.296627        22.518329                07728211   
4   1615.757014        56.649118        67.323209                02492078   

                                        company_name  is_public  \
0  IPSWICH AND DISTRICT COUNCIL FOR VOLUNTARY SER...      False   
1                                PSYTECHNICS LIMITED      False   
2                      SUFFOLK LIFE PENSIONS LIMITED      False   
3                               VERTAS GROUP LIMITED      False   
4           WOODWARD MARKWELL FINANCIAL ADVISERS LTD      False   

  industry_codes     file_codes   sic6  \
0          94,63    19_21,19_10  63990   
1          72,62    19_27,18_29  72190   
2             65          16_34  65300   
3             81          14_50  81100   
4          64,65  12_47 1,16_34  65110   

                                           sic6_desc    lat_dec   lon_dec  \
0        Other information service activities n.e.c.  52.057711  1.152499   
1  Other research and experimental development on...  52.056583  1.151000   
2                                    Pension funding  52.054528  1.147472   
3             Combined facilities support activities  52.080500  1.118139   
4                                     Life insurance  52.056083  1.153194   

   address_lvl address_case      pc8       ttwa  pc4          lat_lon5  
0            2          pta  IP1 1DD  E30000222  IP1   52.05771,1.1525  
1            1          pta  IP1 1HN  E30000222  IP1    52.05658,1.151  
2            1          pta  IP1 1QJ  E30000222  IP1  52.05453,1.14747  
3            1          pta  IP1 1RR  E30000222  IP1   52.0805,1.11814  
4            1          pta  IP1 1SL  E30000222  IP1  52.05608,1.15319  
```

## ref_ons_postcode

### Number of rows: 2,726,477

### Schema:

```
ibis.Schema {
  pcds      string
  ttwa15cd  string
  lat       float64
  long      float64
}
```

### Head of table:

```
      pcds   ttwa15cd        lat      long
0  AB1 0AA  S22000047  57.101459 -2.242858
1  AB1 0AB  S22000047  57.102539 -2.246315
2  AB1 0AD  S22000047  57.100541 -2.248349
3  AB1 0AE  S22000047  57.084429 -2.255714
4  AB1 0AF  S22000047  57.096641 -2.258109
```

