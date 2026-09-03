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
  wd1_y              float64
  wd2_y              float64
  wd3_y              float64
  wd1_k              float64
  wd2_k              float64
  wd3_k              float64
  wd1_l              float64
  wd2_l              float64
  wd3_l              float64
  w2d1_k             float64
  w2d1_l             float64
  w2d2_k             float64
  w2d2_l             float64
  w2d3_k             float64
  w2d3_l             float64
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
}
```

### Head of table:

```
  registered_number  year           gva   total_assets  employees          y  \
0          05992798  2007  38313.828506   20779.729829       1221  10.553566   
1          01275948  2010   1289.386281   25271.701189         41   7.161922   
2          03908486  2008   1605.529890    1333.871190         11   7.381209   
3          04985278  2006   6999.125710    8124.380880        147   8.853541   
4          14172083  2023  65276.640952  591743.937098        159  11.086390   

           k         l     wd1_y     wd2_y     wd3_y      wd1_k      wd2_k  \
0   9.941733  7.107425  8.168144  8.148617  8.672878   8.934023   8.907307   
1  10.137441  3.713572  8.569092  8.365659  8.728029   9.467922   9.184170   
2   7.195841  2.397895  8.014065  7.984953  8.702532   8.988782   8.959609   
3   9.002625  4.990433  8.065894  8.046526  8.596654   8.844168   8.818249   
4  13.290829  5.068904  8.884167  8.863638  9.004505  10.227221  10.239921   

       wd3_k     wd1_l     wd2_l     wd3_l     w2d1_k    w2d1_l     w2d2_k  \
0   9.628465  4.254327  4.246418  4.466514   8.971744  4.293786   8.919212   
1   9.678304  4.196893  3.933996  4.428999   9.688039  4.332729   9.422390   
2   9.672914  4.152142  4.139045  4.469689   8.996131  4.144583   8.936424   
3   9.554636  4.088192  4.076548  4.409398   8.872208  4.110096   8.820314   
4  10.125360  4.957739  5.007930  4.661777  10.288308  4.915532  10.322191   

     w2d2_l     w2d3_k    w2d3_l     w3d1_k    w3d1_l  (i-wd1)w2d1_k  \
0  4.279306   9.733132  4.480359   8.997057  4.301213      -0.025313   
1  3.879604   9.766736  4.454486   9.745937  4.419307      -0.057898   
2  4.116145   9.762371  4.488208   9.025257  4.159326      -0.029126   
3  4.086710   9.660749  4.440607   8.897457  4.122070      -0.025249   
4  5.001982  10.202704  4.670231  10.281273  4.885404       0.007034   

   (i-wd1)w2d1_l  (i-vd1)w2d1_k  (i-vd1)w2d1_l     w4d1_k    w4d1_l  \
0      -0.007427      -0.794353      -0.240661   9.021587  4.308887   
1      -0.086578      -0.190557      -0.181701   9.785629  4.464173   
2      -0.014743      -0.812695      -0.405222   9.053064  4.173464   
3      -0.011974      -0.821420      -0.392340   8.921787  4.133928   
4       0.030128      -0.019766       0.214537  10.278621  4.859801   

   (i-wd1)w3d1_k  (i-wd1)w3d1_l  (i-vd1)w3d1_k  (i-vd1)w3d1_l  
0      -0.024530      -0.007674      -0.762667      -0.238173  
1      -0.039693      -0.044866      -0.133582      -0.103601  
2      -0.027807      -0.014138      -0.780713      -0.396979  
3      -0.024330      -0.011858      -0.788244      -0.385919  
4       0.002652       0.025603      -0.033532       0.180808  
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

