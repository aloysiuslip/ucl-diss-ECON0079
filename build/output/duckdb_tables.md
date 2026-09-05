# Tables in DuckDB database

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

## fame_yearly_kp

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
  registered_number  year  consolidated      turnover  shareholders_funds  \
0          01840419  2006         False  1.336141e+06       130579.754173   
1          01372811  2006         False  3.017042e+04         5598.617602   
2          02468057  2006         False  1.216233e+04         1517.014102   
3          SC010677  2006         False  1.009202e+06       216944.461305   
4          03221027  2006         False  1.463114e+04          -99.327769   

   profit_loss_pretax  employees      tangibles  tangibles_land_and_buildings  \
0        63322.241275       4029  111371.655539                  48323.748103   
1        -1488.339909         55     190.772382                           NaN   
2            8.835442         47            NaN                           NaN   
3       105161.305008       6729  515085.432473                 160816.388467   
4        -1059.496206         26            NaN                           NaN   

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

   fixed_other   intangibles  investments_other    fixed_total    liabilities  \
0          NaN           NaN                NaN  237502.156297 -625279.344461   
1          NaN           NaN                NaN     209.691958   -9682.092564   
2          NaN           NaN                NaN       0.160816   -2862.870690   
3          NaN  12770.713202                NaN  704911.836115 -377445.523520   
4          NaN           NaN                NaN            NaN    -972.781487   

   total_assets  liabilites_lt            cos  admin_expenses  interest_paid  \
0  7.822897e+05  -26430.646434 -781255.474962             NaN            NaN   
1  1.528071e+04            NaN  -21325.514416             NaN            NaN   
2  4.379885e+03            NaN   -8574.592666             NaN            NaN   
3  1.055397e+06 -461006.980273 -512720.485584             NaN            NaN   
4  8.734537e+02            NaN  -12091.185129             NaN            NaN   

   profit_loss_pretax2  tax  dividends  depreciation  r_and_d  \
0                  NaN  NaN        NaN           NaN      NaN   
1                  NaN  NaN        NaN           NaN      NaN   
2                  NaN  NaN        NaN           NaN      NaN   
3                  NaN  NaN        NaN           NaN      NaN   
4                  NaN  NaN        NaN           NaN      NaN   

   remuneration_employees          wages  social_security_costs  \
0           165971.528256  131136.707617           11631.199017   
1             3190.253071    2331.464373             253.065111   
2             2246.147145    2026.320096             203.632515   
3           199839.803440  184492.628993           12081.818182   
4             1425.328010    1257.162162             137.144963   

   pensions_costs  other_staff_costs  renumeration_directors         ebitda  
0    23203.621622                NaN                     NaN   89171.110774  
1      605.723587                NaN                     NaN   -1642.849772  
2       16.194534                NaN                     NaN      36.669290  
3     3265.356265                NaN                     NaN  196132.928680  
4       31.020885                NaN                     NaN    -955.438543  
```

## working_fixed

### Number of rows: 152,379

### Schema:

```
ibis.Schema {
  registered_number  string
  company_name       string
  is_public          boolean
  industry_codes     string
  file_codes         string
  sic6               int64
  sic6_desc          string
  lat_dec            float64
  lon_dec            float64
  address_lvl        int64
  address_case       string
  pc8                string
  ttwa               string
  pc4                string
  lat_lon5           string
}
```

### Head of table:

```
  registered_number                                       company_name  \
0          09066969  BLESSED CHRISTOPHER WHARTON CATHOLIC ACADEMY T...   
1          02416333                                  SAVOY TIMBER LTD.   
2          06382156                          ONE IN A MILLION (SPORTS)   
3          06364892              BRADFORD CITY FC COMMUNITY FOUNDATION   
4          02837030                          MAHARAJA TEXTILES LIMITED   

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

## working_yearly

### Number of rows: 1,128,490

### Schema:

```
ibis.Schema {
  registered_number  string
  year               int64
  employees          int64
  fixed_total        float64
  total_assets       float64
  average_wage       float64
  gva1               float64
  gva2               float64
  gva1_per_worker    float64
  gva2_per_worker    float64
  tfp                float64
}
```

### Head of table:

```
  registered_number  year  employees    fixed_total   total_assets  \
0          07404078  2023         30       4.264056      31.001682   
1          NI031527  2023         62    7659.501766   10463.721206   
2          14771570  2023         61   19009.842193   26071.303871   
3          13264637  2023       2269  189051.245000  614721.233000   
4          13355740  2023         55    4553.341653   28223.947709   

   average_wage           gva1           gva2  gva1_per_worker  \
0     12.917756     440.659867     452.404906        14.688662   
1     14.636052    1020.697635            NaN        16.462865   
2     45.575182    3980.371124    2376.708514        65.251986   
3     96.326896  281906.284838  334707.946978       124.242523   
4     48.856937    5019.654347    3257.513342        91.266443   

   gva2_per_worker       tfp  
0        15.080164  3.006648  
1              NaN  1.731571  
2        38.962435  2.841045  
3       147.513419  3.965358  
4        59.227515  3.114184  
```

## working_yearly_g

### Number of rows: 1,045,164

### Schema:

```
ibis.Schema {
  registered_number  string
  year               int64
  gva                float64
  total_assets       float64
  employees          int64
  y                  float64
  k                  float64
  l                  float64
  wg1_y              float64
  wg2_y              float64
  wg3_y              float64
  wg1_k              float64
  wg2_k              float64
  wg3_k              float64
  wg1_l              float64
  wg2_l              float64
  wg3_l              float64
  w2g1_k             float64
  wg2wg1_k           float64
  wg3wg1_k           float64
  w2g1_l             float64
  wg2wg1_l           float64
  wg3wg1_l           float64
  wg1wg2_k           float64
  w2g2_k             float64
  wg3wg2_k           float64
  wg1wg2_l           float64
  w2g2_l             float64
  wg3wg2_l           float64
  wg1wg3_k           float64
  wg2wg3_k           float64
  w2g3_k             float64
  wg1wg3_l           float64
  wg2wg3_l           float64
  w2g3_l             float64
  w3g1_k             float64
  w3g1_l             float64
  (i-wg1)w2g1_k      float64
  (i-vg1)w2g1_k      float64
  (i-wg1)w2g1_l      float64
  (i-vg1)w2g1_l      float64
  w4g1_k             float64
  w4g1_l             float64
  (i-wg1)w3g1_k      float64
  (i-vg1)w3g1_k      float64
  (i-wg1)w3g1_l      float64
  (i-vg1)w3g1_l      float64
}
```

### Head of table:

```
  registered_number  year          gva  total_assets  employees         y  \
0          04464220  2009  5062.719843   5996.177443        134  8.529659   
1          11425513  2020  2563.924112   9709.478507         70  7.849294   
2          02132170  2011   927.324632    249.451760         13  6.832304   
3          00598760  2008  2923.641856   2940.254888         54  7.980585   
4          06228171  2011    97.563919    113.939902         10  4.580508   

          k         l  wg1_y     wg2_y     wg3_y  wg1_k     wg2_k     wg3_k  \
0  8.698877  4.897840    NaN  8.806353  8.644076    NaN  9.726249  9.621400   
1  9.180858  4.248495    NaN  8.771786  8.717907    NaN  9.874888  9.883188   
2  5.519266  2.564949    NaN  8.743566  8.600413    NaN  9.671209  9.578997   
3  7.986252  3.988984    NaN  8.844523  8.676434    NaN  9.781589  9.631945   
4  4.735671  2.302585    NaN  8.745740  8.600413    NaN  9.671966  9.578997   

   wg1_l     wg2_l     wg3_l  w2g1_k  wg2wg1_k   wg3wg1_k  w2g1_l  wg2wg1_l  \
0    NaN  4.617051  4.407547     NaN  9.797386   9.732889     NaN  4.686718   
1    NaN  4.609478  4.504358     NaN  9.961879  10.094414     NaN  4.642845   
2    NaN  4.525574  4.376065     NaN  9.763684   9.796128     NaN  4.581315   
3    NaN  4.613205  4.416353     NaN  9.842030   9.748205     NaN  4.673524   
4    NaN  4.525827  4.376065     NaN  9.763684   9.796128     NaN  4.581315   

   wg3wg1_l  wg1wg2_k    w2g2_k  wg3wg2_k  wg1wg2_l    w2g2_l  wg3wg2_l  \
0  4.482258       NaN  9.688349  9.628955       NaN  4.586073  4.410200   
1  4.591536       NaN  9.869978  9.884324       NaN  4.604035  4.494659   
2  4.487582       NaN  9.636055  9.585559       NaN  4.499455  4.367343   
3  4.500632       NaN  9.746237  9.640743       NaN  4.591992  4.407841   
4  4.487582       NaN  9.636055  9.585559       NaN  4.499454  4.367343   

   wg1wg3_k  wg2wg3_k    w2g3_k  wg1wg3_l  wg2wg3_l    w2g3_l  w3g1_k  w3g1_l  \
0       NaN  9.621400  9.627349       NaN  4.407547  4.422360     NaN     NaN   
1       NaN  9.883188  9.880245       NaN  4.504358  4.510094     NaN     NaN   
2       NaN  9.578997  9.582256       NaN  4.376065  4.385427     NaN     NaN   
3       NaN  9.631945  9.640936       NaN  4.416353  4.429923     NaN     NaN   
4       NaN  9.578997  9.582256       NaN  4.376065  4.385427     NaN     NaN   

   (i-wg1)w2g1_k  (i-vg1)w2g1_k  (i-wg1)w2g1_l  (i-vg1)w2g1_l  w4g1_k  w4g1_l  \
0            NaN            NaN            NaN            NaN     NaN     NaN   
1            NaN            NaN            NaN            NaN     NaN     NaN   
2            NaN            NaN            NaN            NaN     NaN     NaN   
3            NaN            NaN            NaN            NaN     NaN     NaN   
4            NaN            NaN            NaN            NaN     NaN     NaN   

   (i-wg1)w3g1_k  (i-vg1)w3g1_k  (i-wg1)w3g1_l  (i-vg1)w3g1_l  
0            NaN            NaN            NaN            NaN  
1            NaN            NaN            NaN            NaN  
2            NaN            NaN            NaN            NaN  
3            NaN            NaN            NaN            NaN  
4            NaN            NaN            NaN            NaN  
```

## working_yearly_n

### Number of rows: 1,085,633

### Schema:

```
ibis.Schema {
  registered_number  string
  year               int64
  gva                float64
  total_assets       float64
  employees          int64
  y                  float64
  k                  float64
  l                  float64
  wd1_y              float64
  wd2_y              float64
  wd3_y              float64
  wd1_k              float64
  wd2_k              float64
  wd3_k              float64
  wd1_l              float64
  wd2_l              float64
  wd3_l              float64
  (i-wd1)_y          float64
  (i-wd1)_k          float64
  (i-wd1)_l          float64
  (i-vd1)_y          float64
  (i-vd1)_k          float64
  (i-vd1)_l          float64
  w2d1_k             float64
  w2d1_l             float64
  w2d2_k             float64
  w2d2_l             float64
  w2d3_k             float64
  w2d3_l             float64
  (i-wd1)wd1_k       float64
  (i-wd1)wd1_l       float64
  (i-wd1)wd2_k       float64
  (i-wd1)wd2_l       float64
  (i-wd1)wd3_k       float64
  (i-wd1)wd3_l       float64
  (i-vd1)wd1_k       float64
  (i-vd1)wd1_l       float64
  (i-vd1)wd2_k       float64
  (i-vd1)wd2_l       float64
  (i-vd1)wd3_k       float64
  (i-vd1)wd3_l       float64
  w3d1_k             float64
  w3d1_l             float64
  (i-wd1)w2d1_k      float64
  (i-wd1)w2d1_l      float64
  (i-vd1)w2d1_k      float64
  (i-vd1)w2d1_l      float64
  w4d1_k             float64
  w4d1_l             float64
  (i-wd1)w3d1_k      float64
  (i-wd1)w3d1_l      float64
  (i-vd1)w3d1_k      float64
  (i-vd1)w3d1_l      float64
  (i-wd1)wd1_y       float64
  (i-vd1)wd1_y       float64
  ttwa               string
}
```

### Head of table:

```
  registered_number  year           gva   total_assets  employees          y  \
0          05639474  2019   2521.636554    9580.692950         27   7.832663   
1          01661776  2008  88639.674014  260494.492086        370  11.392335   
2          03846990  2018  12652.888943   24052.220533         63   9.445641   
3          04175679  2013  74700.502755  153333.522936        309  11.221242   
4          02656798  2008   4784.977716   10458.768345         13   8.473237   

           k         l     wd1_y      wd2_y     wd3_y      wd1_k      wd2_k  \
0   9.167505  3.295837  9.000620   8.999856  9.039924  10.036881  10.025291   
1  12.470337  5.913503  8.984585   9.316138  8.847578  10.212514  11.339225   
2  10.087983  4.143135  9.008898   8.931370  9.053620  10.488468  10.661715   
3  11.940371  5.733341  9.338900  10.993326  8.863856   9.991809  10.260829   
4   9.255196  2.564949  8.771710   8.761974  8.849700   9.805396   9.801750   

       wd3_k     wd1_l     wd2_l     wd3_l  (i-wd1)_y  (i-wd1)_k  (i-wd1)_l  \
0  10.167517  4.616057  4.623011  4.585180  -1.167957  -0.869376  -1.320220   
1   9.794168  4.364340  3.924449  4.506326   2.407750   2.257823   1.549163   
2  10.224912  4.273400  3.964150  4.600369   0.436743  -0.400486  -0.130266   
3   9.929607  4.798371  5.841068  4.510860   1.882342   1.948562   0.934970   
4   9.795544  4.637369  4.653650  4.502306  -0.298474  -0.550200  -2.072419   

   (i-vd1)_y  (i-vd1)_k  (i-vd1)_l     w2d1_k    w2d1_l     w2d2_k    w2d2_l  \
0  -1.139417  -0.920869  -1.263681  10.038523  4.591204  10.006639  4.594143   
1   2.585540   2.717598   1.424140   9.951994  4.569345  11.886788  4.913512   
2   0.525863   0.055741  -0.399731  10.353668  4.462528  10.565008  4.000014   
3   2.431603   2.126417   1.258635   9.992652  4.590383  11.081344  5.768120   
4  -0.329108  -0.488585  -1.919657   9.791510  4.592235   9.785644  4.612104   

      w2d3_k    w2d3_l  (i-wd1)wd1_k  (i-wd1)wd1_l  (i-wd1)wd2_k  \
0  10.186513  4.585887     -0.001642      0.024853      0.000750   
1   9.770539  4.503560      0.260520     -0.205005      0.974386   
2  10.176021  4.585721      0.134800     -0.189128      0.221417   
3   9.913256  4.508665     -0.000842      0.207989      0.065109   
4   9.775016  4.500939      0.013886      0.045133      0.011776   

   (i-wd1)wd2_l  (i-wd1)wd3_k  (i-wd1)wd3_l  (i-vd1)wd1_k  (i-vd1)wd1_l  \
0      0.029747     -0.001274      0.000845     -0.139540      0.021928   
1     -0.711164      0.013813      0.002573      0.425060     -0.162227   
2     -0.335358      0.021566      0.006492      0.358176     -0.313105   
3      1.048018      0.013243      0.002530      0.088918      0.273159   
4      0.051031      0.002247      0.001491      0.029052      0.115008   

   (i-vd1)wd2_k  (i-vd1)wd2_l  (i-vd1)wd3_k  (i-vd1)wd3_l     w3d1_k  \
0     -0.130470      0.037108     -0.006921      0.007477  10.057070   
1      1.560750     -0.583111      0.017220      0.008265   9.840533   
2      0.554369     -0.611984      0.091604      0.029199  10.308803   
3      0.386989      1.338298      0.030466      0.008812   9.954631   
4      0.034276      0.150864      0.025071      0.005052   9.792344   

     w3d1_l  (i-wd1)w2d1_k  (i-wd1)w2d1_l  (i-vd1)w2d1_k  (i-vd1)w2d1_l  \
0  4.593874      -0.018547      -0.002669      -0.158755      -0.014577   
1  4.557269       0.111460       0.012076       0.155545       0.026298   
2  4.558266       0.044865      -0.095738       0.198815      -0.139488   
3  4.564832       0.038020       0.025551       0.064563       0.045023   
4  4.587369      -0.000834       0.004866       0.005230       0.052749   

      w4d1_k    w4d1_l  (i-wd1)w3d1_k  (i-wd1)w3d1_l  (i-vd1)w3d1_k  \
0  10.074282  4.596721      -0.017212      -0.002847      -0.148808   
1   9.816486  4.569071       0.024047      -0.011802       0.040589   
2  10.278959  4.613151       0.029844      -0.054885       0.142051   
3   9.957867  4.569474      -0.003236      -0.004642       0.013513   
4   9.792959  4.583485      -0.000615       0.003885       0.001297   

   (i-vd1)w3d1_l  (i-wd1)wd1_y  (i-vd1)wd1_y       ttwa  
0      -0.018294      0.014454     -0.040637  E30000234  
1       0.004471      0.023608      0.155539  E30000234  
2      -0.053102     -0.058833      0.012640  E30000234  
3       0.006954      0.357375      0.483467  E30000234  
4       0.037488      0.001414     -0.051189  E30000234  
```

## working_yearly_no

### Number of rows: 1,085,633

### Schema:

```
ibis.Schema {
  registered_number  string
  year               int64
  gva                float64
  total_assets       float64
  employees          int64
  y                  float64
  k                  float64
  l                  float64
  wd1_y              float64
  wd2_y              float64
  wd3_y              float64
  wd1_k              float64
  wd2_k              float64
  wd3_k              float64
  wd1_l              float64
  wd2_l              float64
  wd3_l              float64
  (i-wd1)_y          float64
  (i-wd1)_k          float64
  (i-wd1)_l          float64
  (i-vd1)_y          float64
  (i-vd1)_k          float64
  (i-vd1)_l          float64
  w2d1_k             float64
  w2d1_l             float64
  w2d2_k             float64
  w2d2_l             float64
  w2d3_k             float64
  w2d3_l             float64
  (i-wd1)wd1_k       float64
  (i-wd1)wd1_l       float64
  (i-wd1)wd2_k       float64
  (i-wd1)wd2_l       float64
  (i-wd1)wd3_k       float64
  (i-wd1)wd3_l       float64
  (i-vd1)wd1_k       float64
  (i-vd1)wd1_l       float64
  (i-vd1)wd2_k       float64
  (i-vd1)wd2_l       float64
  (i-vd1)wd3_k       float64
  (i-vd1)wd3_l       float64
  w3d1_k             float64
  w3d1_l             float64
  (i-wd1)w2d1_k      float64
  (i-wd1)w2d1_l      float64
  (i-vd1)w2d1_k      float64
  (i-vd1)w2d1_l      float64
  w4d1_k             float64
  w4d1_l             float64
  (i-wd1)w3d1_k      float64
  (i-wd1)w3d1_l      float64
  (i-vd1)w3d1_k      float64
  (i-vd1)w3d1_l      float64
  (i-wd1)wd1_y       float64
  (i-vd1)wd1_y       float64
  ttwa               string
}
```

### Head of table:

```
  registered_number  year          gva  total_assets  employees         y  \
0          04635359  2020  4900.694848  23567.253839        117  8.497132   
1          00679901  2012   186.057966   7677.934602         41  5.226058   
2          06542012  2011  4826.946156  51192.430655         92  8.481969   
3          03652736  2011  9334.909021  23079.291471        179  9.141516   
4          02957012  2013  1119.310317   1510.158585         37  7.020468   

           k         l     wd1_y     wd2_y     wd3_y     wd1_k     wd2_k  \
0  10.067613  4.762174  8.203281  8.380483  8.293159  8.955016  9.033629   
1   8.946106  3.713572  8.292550  8.175684  8.473404  8.803722  8.637764   
2  10.843347  4.521789  8.581812  8.578433  8.638774  9.323870  8.916131   
3  10.046691  5.187386  7.521923  7.242619  8.755914  8.190512  7.894072   
4   7.319970  3.610918  8.486574  8.351259  8.547053  9.518755  9.579718   

      wd3_k     wd1_l     wd2_l     wd3_l  (i-wd1)_y  (i-wd1)_k  (i-wd1)_l  \
0  9.064769  4.688260  4.669777  4.722513   0.293851   1.112598   0.073914   
1  9.040450  5.313631  5.288800  5.338427  -3.066491   0.142384  -1.600059   
2  9.450669  4.716120  4.961039  4.697141  -0.099843   1.519477  -0.194331   
3  9.657270  4.078841  3.845359  4.950747   1.619593   1.856179   1.108545   
4  9.533043  4.744567  4.803656  4.774068  -1.466106  -2.198785  -1.133649   

   (i-vd1)_y  (i-vd1)_k  (i-vd1)_l    w2d1_k    w2d1_l    w2d2_k    w2d2_l  \
0   0.466988   1.208340   0.111996  9.247663  4.832037  9.496362  4.913604   
1  -3.726792  -1.252281  -1.670473  9.081426  3.880777  8.950223  3.718361   
2   0.005410   1.399985  -0.062930  9.408195  4.580971  9.658542  4.482574   
3   0.661544   0.623873   0.586365  9.667585  4.700112  9.649967  4.644776   
4  -1.465949  -2.138355  -1.021484  9.324084  4.576074  9.078866  4.495844   

     w2d3_k    w2d3_l  (i-wd1)wd1_k  (i-wd1)wd1_l  (i-wd1)wd2_k  (i-wd1)wd2_l  \
0  9.253551  4.824571     -0.292648     -0.143777     -0.433157     -0.268701   
1  9.327984  4.168340     -0.277704      1.432854     -0.395702      1.463044   
2  9.581367  4.740095     -0.084325      0.135149     -0.489779      0.527396   
3  9.660124  4.786200     -1.477073     -0.621271     -1.758493     -0.809428   
4  9.559837  4.783383      0.194671      0.168493      0.436485      0.386442   

   (i-wd1)wd3_k  (i-wd1)wd3_l  (i-vd1)wd1_k  (i-vd1)wd1_l  (i-vd1)wd2_k  \
0     -0.161026     -0.097398     -0.243353     -0.133947     -0.341317   
1     -0.149446      1.336504     -0.681017      0.653127     -0.948492   
2     -0.111085     -0.012998      0.022630      0.167666     -0.254092   
3     -0.219576     -0.002393     -1.279381     -0.534474     -1.462249   
4      0.000185      0.018472      0.226206      0.200464      0.423775   

   (i-vd1)wd2_l  (i-vd1)wd3_k  (i-vd1)wd3_l    w3d1_k    w3d1_l  \
0     -0.248014     -0.087555     -0.080285  9.102981  4.779065   
1      0.523911     -0.571251      0.557070  8.909372  5.262595   
2      0.574738     -0.066209      0.017518  9.317050  4.562096   
3     -0.615244      0.200392      0.350262  8.379930  4.164216   
4      0.413648      0.018472      0.051040  9.312480  4.549319   

   (i-wd1)w2d1_k  (i-wd1)w2d1_l  (i-vd1)w2d1_k  (i-vd1)w2d1_l    w4d1_k  \
0       0.144682       0.052972       0.143778       0.054111  9.153709   
1       0.172053      -1.381818      -0.386414      -0.987376  9.123030   
2       0.091145       0.018875       0.135709       0.044223  9.215463   
3       1.287655       0.535896       0.465774       0.194843  9.584178   
4       0.011604       0.026755       0.031415       0.044249  9.218193   

     w4d1_l  (i-wd1)w3d1_k  (i-wd1)w3d1_l  (i-vd1)w3d1_k  (i-vd1)w3d1_l  \
0  4.802660      -0.050727      -0.023595      -0.051224      -0.025092   
1  3.978277      -0.213658       1.284318      -0.321842       0.754514   
2  4.515999       0.101587       0.046098       0.158905       0.072919   
3  4.667351      -1.204248      -0.503135      -0.902244      -0.374563   
4  4.487855       0.094287       0.061463       0.133232       0.086733   

   (i-wd1)wd1_y  (i-vd1)wd1_y       ttwa  
0     -0.025413     -0.036277  E30000170  
1      2.650095      0.607282  K01000014  
2      0.121054      0.217381  E30000267  
3     -1.027136     -0.960301  E30000267  
4      0.072623      0.105475  E30000267  
```

## working_distance_ttwa_km

### Number of rows: 734,346,954

### Schema:

```
ibis.Schema {
  firm_i           string
  firm_j           string
  distance_meters  float64
}
```

### Head of table:

```
     firm_i    firm_j  distance_meters
0  02185448  02838541      1938.809375
1  02425634  02838541      1802.723825
2  00541295  02838541      1918.306212
3  02461547  02838541      1802.723825
4  04396922  02838541      1938.809375
```

## ref_ons_postcode

### Number of rows: 2,726,477

### Schema:

```
ibis.Schema {
  ttwa15cd  string
  lat       float64
  long      float64
  pcds      string
}
```

### Head of table:

```
    ttwa15cd        lat      long     pcds
0  S22000047  57.101459 -2.242858  AB1 0AA
1  S22000047  57.102539 -2.246315  AB1 0AB
2  S22000047  57.100541 -2.248349  AB1 0AD
3  S22000047  57.084429 -2.255714  AB1 0AE
4  S22000047  57.096641 -2.258109  AB1 0AF
```

## ref_ons_ttwa_name

### Number of rows: 230

### Schema:

```
ibis.Schema {
  TTWA11CD  string
  TTWA11NM  string
}
```

### Head of table:

```
    TTWA11CD                 TTWA11NM
0  E30000004                 Barnsley
1  E30000018                 Bradford
2  E30000029                  Halifax
3  E30000039                  Skipton
4  E30000046  Dorchester and Weymouth
```

