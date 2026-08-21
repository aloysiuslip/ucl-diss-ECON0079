# Other Tables in DuckDB database

## ibis_duckdb_table_3lupfa4t4vap7offrjesdjdzqy

### Number of rows: 0

### Schema:

```
ibis.Schema {
  firm_i           string
  firm_j           string
  pc4              string
  distance_meters  float64
}
```

### Head of table:

```
Empty DataFrame
Columns: [firm_i, firm_j, pc4, distance_meters]
Index: []
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

## ref_ons_postcode

### Number of rows: 2,726,477

### Schema:

```
ibis.Schema {
  lat       float64
  ttwa15cd  string
  long      float64
  pcds      string
}
```

### Head of table:

```
         lat   ttwa15cd      long     pcds
0  57.101459  S22000047 -2.242858  AB1 0AA
1  57.102539  S22000047 -2.246315  AB1 0AB
2  57.100541  S22000047 -2.248349  AB1 0AD
3  57.084429  S22000047 -2.255714  AB1 0AE
4  57.096641  S22000047 -2.258109  AB1 0AF
```

## temp_spatial_pairs

### Number of rows: 46,870,226

### Schema:

```
ibis.Schema {
  firm_i    string
  firm_j    string
  prop_key  string
  lon_i     float64
  lat_i     float64
  lon_j     float64
  lat_j     float64
}
```

### Head of table:

```
     firm_i    firm_j prop_key     lon_i      lat_i     lon_j      lat_j
0  04687714  02941048      WA7 -2.748511  53.322848 -2.658767  53.317319
1  00745573  02941048      WA7 -2.738472  53.323778 -2.658767  53.317319
2  01385533  02941048      WA7 -0.351528  51.434306 -2.658767  53.317319
3  03892046  02941048      WA7 -2.694468  53.325791 -2.658767  53.317319
4  07088219  02941048      WA7 -2.732899  53.324698 -2.658767  53.317319
```

## working_distance

### Number of rows: 46,870,226

### Schema:

```
ibis.Schema {
  firm_i           string
  firm_j           string
  pc4              string
  distance_meters  float64
}
```

### Head of table:

```
     firm_i    firm_j   pc4  distance_meters
0  04706935  02710265  EC1V       376.079585
1  06873977  02710265  EC1V       930.287073
2  03283581  02710265  EC1V       826.365636
3  04330100  02710265  EC1V       812.058728
4  04944709  02710265  EC1V       726.387891
```

## ibis_duckdb_table_pchjoy34tzerrl2h7r6q7zkrru

### Number of rows: 0

### Schema:

```
ibis.Schema {
  firm_i           string
  firm_j           string
  ttwa             string
  distance_meters  float64
}
```

### Head of table:

```
Empty DataFrame
Columns: [firm_i, firm_j, ttwa, distance_meters]
Index: []
```

## spatial_panel_view

### Number of rows: 1,081,520

### Schema:

```
ibis.Schema {
  registered_number        string
  year                     int64
  employees                int64
  fixed_total              float64
  total_assets             float64
  average_wage             float64
  gva1                     float64
  gva2                     float64
  gva1_per_worker          float64
  gva2_per_worker          float64
  tfp                      float64
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
  registered_number  year  employees  fixed_total  total_assets  average_wage  \
0          09066969  2017        282  2360.953046   4577.750314     21.588899   
1          02416333  2015         60   169.588480   4813.901186     41.167791   
2          06382156  2017         16     2.868515    245.648182     21.476627   
3          06364892  2018         25    36.423144    311.092021     28.973805   
4          02837030  2007         42  1775.541388   9514.831620     28.129892   

          gva1         gva2  gva1_per_worker  gva2_per_worker       tfp  \
0  5677.361906          NaN        20.132489              NaN  2.749876   
1  2703.167954          NaN        45.052799              NaN  2.948087   
2   349.731286          NaN        21.858205              NaN  2.570549   
3   737.323773          NaN        29.492951              NaN  2.973460   
4  2422.219084  1915.910371        57.671883        45.616914  2.863251   

  registered_number_right                                       company_name  \
0                09066969  BLESSED CHRISTOPHER WHARTON CATHOLIC ACADEMY T...   
1                02416333                                  SAVOY TIMBER LTD.   
2                06382156                          ONE IN A MILLION (SPORTS)   
3                06364892              BRADFORD CITY FC COMMUNITY FOUNDATION   
4                02837030                          MAHARAJA TEXTILES LIMITED   

   is_public industry_codes file_codes   sic6  \
0      False             85      17_31  85200   
1      False             46      14_55  46130   
2      False             93      17_15  93199   
3      False             93    17_15 2  93199   
4      False             46    14_56 2  46410   

                                           sic6_desc    lat_dec   lon_dec  \
0                                  Primary education  53.857667 -1.915417   
1  Agents involved in the sale of timber and buil...  53.805861 -1.759056   
2  Other sports activities (not including activit...  53.804818 -1.761027   
3  Other sports activities (not including activit...  53.803593 -1.759486   
4                              Wholesale of textiles  53.803568 -1.760412   

   address_lvl address_case      pc8       ttwa  pc4           lat_lon5  
0            1          pta  BD8 7AP  E30000018  BD8  53.85767,-1.91542  
1            1           ro  BD8 7DQ  E30000018  BD8  53.80586,-1.75906  
2            2          pta  BD8 7DX  E30000018  BD8  53.80482,-1.76103  
3            2          pta  BD8 7DY  E30000018  BD8  53.80359,-1.75949  
4            2           ro  BD8 7DZ  E30000018  BD8  53.80357,-1.76041  
```

## working_distance_filtered

### Number of rows: 43,241,404

### Schema:

```
ibis.Schema {
  firm_i           string
  firm_j           string
  pc4              string
  distance_meters  float64
}
```

### Head of table:

```
     firm_i    firm_j   pc4  distance_meters
0  04706935  02710265  EC1V       376.079585
1  06873977  02710265  EC1V       930.287073
2  03283581  02710265  EC1V       826.365636
3  04330100  02710265  EC1V       812.058728
4  04944709  02710265  EC1V       726.387891
```

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
  registered_number  year  employees  average_wage          gva1         gva2  \
0          01996684  2012         12    134.399740    209.381882          NaN   
1          NI004331  2012         51     32.297089   2189.021320  1610.507470   
2          01944332  2012         19     49.763327   1287.745912  1386.628353   
3          05754830  2012         57     16.047869   1891.701502   849.429037   
4          01227970  2012       1210     32.614044  39240.450243          NaN   

   gva1_per_worker  gva2_per_worker registered_number_right  \
0        17.448490              NaN                01996684   
1        42.921987        31.578578                NI004331   
2        67.776101        72.980440                01944332   
3        33.187746        14.902264                05754830   
4        32.430124              NaN                01227970   

                         company_name  is_public industry_codes  \
0  SUMITOMO MITSUI TRUST (UK) LIMITED      False             64   
1              DESMOND MOTORS LIMITED      False             45   
2     MARSON FABRICS (LONDON) LIMITED      False             46   
3                  SBAW GROUP LIMITED      False    55,68,70,56   
4              RETHINK MENTAL ILLNESS      False             86   

                file_codes   sic6  \
0                    12_47  64999   
1                    14_37  45111   
2                    14_55  46410   
3  19_14,13_18,16_55,17_22  55100   
4                    17_50  86900   

                                           sic6_desc    lat_dec   lon_dec  \
0  Other financial service activities, except ins...  53.407611 -2.988611   
1          Sale of new cars and light motor vehicles  55.011389 -7.316556   
2                              Wholesale of textiles  51.522111 -0.135778   
3                   Hotels and similar accommodation  51.213000 -2.646444   
4                      Other human health activities  51.490917 -0.122361   

   address_lvl address_case       ttwa   pc4           lat_lon5  
0            1           ro  E30000233    L2  53.40761,-2.98861  
1            1          pta  N12000006  BT48  55.01139,-7.31656  
2            1          pta  E30000234   E14  51.52211,-0.13578  
3            1           ro  E30000274   BA5    51.213,-2.64644  
4            1          pta  E30000234   SE1  51.49092,-0.12236  
```

## spatial_distance_matrix

### Number of rows: 46,871,260

### Schema:

```
ibis.Schema {
  firm_i           string
  firm_j           string
  pc4              string
  distance_meters  float64
}
```

### Head of table:

```
     firm_i    firm_j  pc4  distance_meters
0  08802529  06701937  E1W       230.666289
1  04375903  06701937  E1W       431.416883
2  01190238  06701937  E1W       431.692974
3  04319685  06701937  E1W       486.857618
4  03107229  06701937  E1W       360.974044
```

