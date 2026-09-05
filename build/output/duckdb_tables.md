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
  (i-wg1)_y          float64
  (i-vg1)_y          float64
  (i-wg1)_k          float64
  (i-vg1)_k          float64
  (i-wg1)_l          float64
  (i-vg1)_l          float64
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
  (i-wg1)wg1_y       float64
  (i-vg1)wg1_y       float64
  (i-wg1)wg1_k       float64
  (i-vg1)wg1_k       float64
  (i-wg1)wg1_l       float64
  (i-vg1)wg1_l       float64
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
  (i-wg1)w4g1_k      float64
  (i-vg1)w4g1_k      float64
  (i-wg1)w4g1_l      float64
  (i-vg1)w4g1_l      float64
}
```

### Head of table:

```
  registered_number  year           gva  total_assets  employees         y  \
0          07762575  2015   3264.446027    908.181785        113  8.090845   
1          06511690  2015   2923.998839   7306.333142        112  7.980707   
2          04036447  2015   5985.841099   8503.500604        287  8.697152   
3          06404664  2015  10553.495857  10240.306840        356  9.264212   
4          02740383  2015   6862.055115  22484.907206        298  8.833762   

           k         l     wg1_y     wg2_y     wg3_y     wg1_k      wg2_k  \
0   6.811445  4.727388  7.940817  9.152755  8.634129  8.453090  10.176737   
1   8.896497  4.718499  7.945053  9.152755  8.634129  8.372896  10.176737   
2   9.048233  5.659482  7.917498  9.152755  8.634129  8.367060  10.176737   
3   9.234087  5.874931  7.895688  9.152755  8.634129  8.359912  10.176737   
4  10.020600  5.697093  7.912243  9.152755  8.634129  8.329661  10.176737   

      wg3_k     wg1_l     wg2_l     wg3_l  (i-wg1)_y  (i-vg1)_y  (i-wg1)_k  \
0  9.393255  4.763066  4.966422  4.672465   0.150028   0.144472  -1.641646   
1  9.393255  4.763408  4.966422  4.672465   0.035654   0.034334   0.523601   
2  9.393255  4.727216  4.966422  4.672465   0.779654   0.750778   0.681173   
3  9.393255  4.718930  4.966422  4.672465   1.368525   1.317839   0.874175   
4  9.393255  4.725769  4.966422  4.672465   0.921519   0.887389   1.690938   

   (i-vg1)_k  (i-wg1)_l  (i-vg1)_l    w2g1_k   wg2wg1_k  wg3wg1_k    w2g1_l  \
0  -1.580844  -0.035678  -0.034357  8.389950  10.195249  9.567412  4.761694   
1   0.504208  -0.044909  -0.043245  8.393035  10.195249  9.567412  4.761680   
2   0.655944   0.932266   0.897738  8.393259  10.195249  9.567412  4.763072   
3   0.841798   1.156001   1.113186  8.393534  10.195249  9.567412  4.763391   
4   1.628311   0.971324   0.935349  8.394697  10.195249  9.567412  4.763128   

   wg2wg1_l  wg3wg1_l   wg1wg2_k    w2g2_k  wg3wg2_k  wg1wg2_l    w2g2_l  \
0  5.058249  4.883686  10.176737  9.809954  9.365633  4.966422  4.914815   
1  5.058249  4.883686  10.176737  9.809954  9.365633  4.966422  4.914815   
2  5.058249  4.883686  10.176737  9.809954  9.365633  4.966422  4.914815   
3  5.058249  4.883686  10.176737  9.809954  9.365633  4.966422  4.914815   
4  5.058249  4.883686  10.176737  9.809954  9.365633  4.966422  4.914815   

   wg3wg2_l  wg1wg3_k  wg2wg3_k    w2g3_k  wg1wg3_l  wg2wg3_l    w2g3_l  \
0  4.631634  9.393255  9.393255  9.478699  4.672465  4.672465  4.721016   
1  4.631634  9.393255  9.393255  9.478699  4.672465  4.672465  4.721016   
2  4.631634  9.393255  9.393255  9.478699  4.672465  4.672465  4.721016   
3  4.631634  9.393255  9.393255  9.478699  4.672465  4.672465  4.721016   
4  4.631634  9.393255  9.393255  9.478699  4.672465  4.672465  4.721016   

   (i-wg1)wg1_y  (i-vg1)wg1_y  (i-wg1)wg1_k  (i-vg1)wg1_k  (i-wg1)wg1_l  \
0     -0.005770     -0.005557      0.063140      0.060802      0.001372   
1     -0.001371     -0.001321     -0.020138     -0.019393      0.001727   
2     -0.029987     -0.028876     -0.026199     -0.025229     -0.035856   
3     -0.052636     -0.050686     -0.033622     -0.032377     -0.044462   
4     -0.035443     -0.034130     -0.065036     -0.062627     -0.037359   

   (i-vg1)wg1_l    w3g1_k    w3g1_l  (i-wg1)w2g1_k  (i-vg1)w2g1_k  \
0      0.001321  8.392379  4.761746      -0.002428      -0.002339   
1      0.001663  8.392260  4.761747       0.000775       0.000746   
2     -0.034528  8.392251  4.761693       0.001008       0.000970   
3     -0.042815  8.392241  4.761681       0.001293       0.001245   
4     -0.035975  8.392196  4.761691       0.002501       0.002409   

   (i-wg1)w2g1_l  (i-vg1)w2g1_l    w4g1_k    w4g1_l  (i-wg1)w3g1_k  \
0      -0.000053      -0.000051  8.392285  4.761744       0.000093   
1      -0.000066      -0.000064  8.392290  4.761744      -0.000030   
2       0.001379       0.001328  8.392290  4.761746      -0.000039   
3       0.001710       0.001647  8.392291  4.761747      -0.000050   
4       0.001437       0.001384  8.392292  4.761746      -0.000096   

   (i-vg1)w3g1_k  (i-wg1)w3g1_l  (i-vg1)w3g1_l  (i-wg1)w4g1_k  (i-vg1)w4g1_k  \
0       0.000090       0.000002       0.000002      -0.000004      -0.000003   
1      -0.000029       0.000003       0.000002       0.000001       0.000001   
2      -0.000037      -0.000053      -0.000051       0.000001       0.000001   
3      -0.000048      -0.000066      -0.000063       0.000002       0.000002   
4      -0.000093      -0.000055      -0.000053       0.000004       0.000004   

   (i-wg1)w4g1_l  (i-vg1)w4g1_l  
0  -7.807403e-08  -7.518240e-08  
1  -9.827384e-08  -9.463407e-08  
2   2.040077e-06   1.964519e-06  
3   2.529676e-06   2.435984e-06  
4   2.125547e-06   2.046823e-06  
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
  w2d1_k             float64
  w2d1_l             float64
  w2d2_k             float64
  w2d2_l             float64
  w2d3_k             float64
  w2d3_l             float64
  (i-wd1)wd1_k       float64
  (i-wd1)wd1_l       float64
  w3d1_k             float64
  w3d1_l             float64
  (i-wd1)w2d1_k      float64
  (i-wd1)w2d1_l      float64
  w4d1_k             float64
  w4d1_l             float64
  (i-wd1)w3d1_k      float64
  (i-wd1)w3d1_l      float64
  (i-wd1)wd1_y       float64
  (i-vd1)_y          float64
  (i-vd1)_k          float64
  (i-vd1)_l          float64
  (i-vd1)wd1_y       float64
  (i-vd1)wd1_k       float64
  (i-vd1)wd1_l       float64
  (i-vd1)w2d1_k      float64
  (i-vd1)w2d1_l      float64
  (i-vd1)w3d1_k      float64
  (i-vd1)w3d1_l      float64
  (i-vd1)w4d1_k      float64
  (i-vd1)w4d1_l      float64
}
```

### Head of table:

```
  registered_number  year           gva  total_assets  employees          y  \
0          00526923  2010  3.890745e+05  1.294746e+06       5878  12.871526   
1          01152332  2010  1.315647e+04  1.869476e+04        341   9.484669   
2          03927018  2010  9.736595e+02  2.835098e+03         11   6.881062   
3          02485577  2010  7.430439e+03  2.271329e+04         42   8.913340   
4          02711006  2010  1.103953e+06  2.717398e+08         93  13.914408   

           k         l     wd1_y     wd2_y     wd3_y     wd1_k      wd2_k  \
0  14.073825  8.678972  8.289941  8.005815  8.908402  9.364887   9.065354   
1   9.835999  5.831882  8.903543  8.921577  8.782020  9.390277   9.312130   
2   7.949832  2.397895  9.117631  9.162707  8.883433  9.996450  10.021405   
3  10.030706  3.737670  8.908739  9.325575  8.834888  9.914749  10.331060   
4  19.420355  4.532599  8.595630  8.583317  9.090178  9.787587   9.775238   

       wd3_k     wd1_l     wd2_l     wd3_l  (i-wd1)_y  (i-wd1)_k  (i-wd1)_l  \
0  10.002010  4.144012  4.007348  4.505656   4.581585   4.708938   4.534960   
1   9.719936  4.866627  4.946472  4.472737   0.581126   0.445722   0.965256   
2   9.878013  4.614447  4.636656  4.473443  -2.236569  -2.046618  -2.216552   
3   9.829620  4.404521  4.143326  4.457027   0.004602   0.115957  -0.666852   
4  10.309190  4.307545  4.298698  4.626361   5.318777   9.632768   0.225054   

      w2d1_k    w2d1_l     w2d2_k    w2d2_l     w2d3_k    w2d3_l  \
0   9.912370  4.583007   9.780619  4.671219   9.962259  4.487640   
1   9.469448  4.822670   9.325586  4.972490   9.766164  4.459063   
2   9.932858  4.552382   9.961175  4.569772   9.845792  4.459976   
3   9.854572  4.469783  10.016821  3.752217   9.812691  4.457105   
4  10.016153  4.321432   9.999569  4.304198  10.378111  4.644361   

   (i-wd1)wd1_k  (i-wd1)wd1_l     w3d1_k    w3d1_l  (i-wd1)w2d1_k  \
0     -0.547483     -0.438995   9.904937  4.541623       0.007433   
1     -0.079171      0.043956   9.528079  4.769501      -0.058631   
2      0.063592      0.062065   9.923366  4.550676       0.009493   
3      0.060177     -0.065261   9.852128  4.500669       0.002444   
4     -0.228566     -0.013886  10.019081  4.329350      -0.002927   

   (i-wd1)w2d1_l     w4d1_k    w4d1_l  (i-wd1)w3d1_k  (i-wd1)w3d1_l  \
0       0.041384   9.931624  4.552510      -0.026686      -0.010886   
1       0.053169   9.578173  4.726588      -0.050094       0.042913   
2       0.001707   9.914385  4.549005       0.008980       0.001670   
3      -0.030886   9.851885  4.512191       0.000243      -0.011523   
4      -0.007918  10.026720  4.336958      -0.007639      -0.007608   

   (i-wd1)wd1_y  (i-vd1)_y  (i-vd1)_k  (i-vd1)_l  (i-vd1)wd1_y  (i-vd1)wd1_k  \
0     -0.538644   4.223327   4.465089   4.281666     -0.447848     -0.364853   
1     -0.000529   0.836470   0.227262   1.434577      0.165754     -0.339463   
2      0.084764  -1.767138  -1.658905  -1.999410      0.379841      0.266710   
3      0.056996   0.265141   0.421969  -0.659636      0.170949      0.185009   
4     -0.131584   5.266208   9.811619   0.135294     -0.142159      0.057847   

   (i-vd1)wd1_l  (i-vd1)w2d1_k  (i-vd1)w2d1_l  (i-vd1)w3d1_k  (i-vd1)w3d1_l  \
0     -0.325441       0.152073       0.089529       0.130955       0.035780   
1      0.397173      -0.290849       0.329192      -0.245904       0.263658   
2      0.144994       0.172561       0.058904       0.149383       0.044832   
3     -0.064932       0.094274      -0.023696       0.078145      -0.005174   
4     -0.161908       0.255856      -0.172047       0.245098      -0.176493   

   (i-vd1)w4d1_k  (i-vd1)w4d1_l  
0       0.152992       0.039052  
1      -0.200458       0.213131  
2       0.135754       0.035548  
3       0.073253      -0.001266  
4       0.248088      -0.176500  
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
  w2d1_k             float64
  w2d1_l             float64
  w2d2_k             float64
  w2d2_l             float64
  w2d3_k             float64
  w2d3_l             float64
  (i-wd1)wd1_k       float64
  (i-wd1)wd1_l       float64
  w3d1_k             float64
  w3d1_l             float64
  (i-wd1)w2d1_k      float64
  (i-wd1)w2d1_l      float64
  w4d1_k             float64
  w4d1_l             float64
  (i-wd1)w3d1_k      float64
  (i-wd1)w3d1_l      float64
  (i-wd1)wd1_y       float64
  (i-vd1)_y          float64
  (i-vd1)_k          float64
  (i-vd1)_l          float64
  (i-vd1)wd1_y       float64
  (i-vd1)wd1_k       float64
  (i-vd1)wd1_l       float64
  (i-vd1)w2d1_k      float64
  (i-vd1)w2d1_l      float64
  (i-vd1)w3d1_k      float64
  (i-vd1)w3d1_l      float64
  (i-vd1)w4d1_k      float64
  (i-vd1)w4d1_l      float64
}
```

### Head of table:

```
  registered_number  year            gva  total_assets  employees          y  \
0          08441256  2018    4560.020968  5.763913e+03         93   8.425083   
1          09176675  2018  562025.019084  2.137062e+06      22397  13.239302   
2          07059696  2018   15915.614286  4.270770e+04        325   9.675056   
3          07328996  2018   10532.080021  1.450050e+04         61   9.262181   
4          01910791  2018    8664.222451  7.807738e+04         58   9.066957   

           k          l     wd1_y     wd2_y     wd3_y      wd1_k      wd2_k  \
0   8.659372   4.532599  8.964143  8.721983  9.025291  10.098198   9.785827   
1  14.574943  10.016682  9.081245  9.171757  9.144700  10.273329  10.389009   
2  10.662135   5.783825  8.931426  8.793776  8.855549  10.098739  10.098455   
3   9.581938   4.110874  9.448346  9.421810  9.450717  10.750233  10.628318   
4  11.265456   4.060443  9.173026  9.358637  9.316488  10.383954  10.585157   

       wd3_k     wd1_l     wd2_l     wd3_l  (i-wd1)_y  (i-wd1)_k  (i-wd1)_l  \
0  10.179605  4.587008  4.495160  4.594739  -0.539060  -1.438826  -0.054409   
1  10.355088  4.566078  4.569986  4.552277   4.158056   4.301614   5.450604   
2  10.012211  4.501544  4.187290  4.445708   0.743630   0.563395   1.282281   
3  10.782042  4.887112  5.016382  4.848000  -0.186165  -1.168295  -0.776238   
4  10.544503  4.853466  4.950125  4.950165  -0.106068   0.881502  -0.793023   

      w2d1_k    w2d1_l     w2d2_k    w2d2_l     w2d3_k    w2d3_l  \
0  10.156944  4.578867   9.999835  4.579762  10.199633  4.575325   
1  10.209891  4.569777  10.365810  4.558641  10.270611  4.563095   
2  10.145977  4.568442  10.033878  4.414006  10.137141  4.549875   
3  10.620730  4.812505  10.695602  4.832911  10.598368  4.804471   
4  10.177694  4.750003  10.360947  4.897415  10.304278  4.861072   

   (i-wd1)wd1_k  (i-wd1)wd1_l     w3d1_k    w3d1_l  (i-wd1)w2d1_k  \
0     -0.058746      0.008142  10.163798  4.576507      -0.006853   
1      0.063438     -0.003699  10.183494  4.573540       0.026397   
2     -0.047237     -0.066897  10.156487  4.574922      -0.010510   
3      0.129503      0.074607  10.635225  4.827619      -0.014494   
4      0.206260      0.103463  10.163618  4.709305       0.014076   

   (i-wd1)w2d1_l     w4d1_k    w4d1_l  (i-wd1)w3d1_k  (i-wd1)w3d1_l  \
0       0.002360  10.163879  4.576365      -0.000081       0.000141   
1      -0.003763  10.172109  4.575334       0.011385      -0.001794   
2      -0.006480  10.158863  4.576360      -0.002377      -0.001438   
3      -0.015114  10.606160  4.817630       0.029065       0.009989   
4       0.040698  10.101227  4.680587       0.062391       0.028718   

   (i-wd1)wd1_y  (i-vd1)_y  (i-vd1)_k  (i-vd1)_l  (i-vd1)wd1_y  (i-vd1)wd1_k  \
0     -0.044299  -0.367347  -1.234307   0.003529      0.116377      0.137297   
1      0.039157   4.446872   4.681263   5.487612      0.233480      0.312428   
2     -0.068339   0.882626   0.768455   1.254755      0.083660      0.137838   
3      0.123570   0.469752  -0.311741  -0.418196      0.600581      0.789332   
4      0.188653   0.274528   1.371776  -0.468627      0.325260      0.423053   

   (i-vd1)wd1_l  (i-vd1)w2d1_k  (i-vd1)w2d1_l  (i-vd1)w3d1_k  (i-vd1)w3d1_l  \
0      0.031385       0.170532       0.014912       0.164371       0.008797   
1      0.010455       0.223479       0.005822       0.184068       0.005830   
2     -0.054079       0.159565       0.004487       0.157060       0.007212   
3      0.331489       0.634319       0.248551       0.635799       0.259910   
4      0.297843       0.191282       0.186048       0.164192       0.141596   

   (i-vd1)w4d1_k  (i-vd1)w4d1_l  
0       0.159352       0.007111  
1       0.167582       0.006080  
2       0.154336       0.007106  
3       0.601633       0.248376  
4       0.096700       0.111333  
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

