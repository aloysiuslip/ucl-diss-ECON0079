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
  pc8                string
  pc4                string
  ttwa               string
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
  registered_number  year          gva  total_assets  employees       pc8  \
0          07433621  2015   716.712815    462.619739         37  MK40 2QT   
1          07433621  2023   813.859830    514.439031         38  MK40 2QT   
2          01702871  2008  3978.988412   4587.171545        122  MK40 2RU   
3          04749130  2024   260.330000    458.283000         12  MK40 3HD   
4          01270747  2014  1908.323624   2561.469729         43  MK40 3JJ   

    pc4       ttwa  wg1_y        wg2_y        wg3_y  wg1_k         wg2_k  \
0  MK40  E30000166    NaN  2281.877435  6892.553648    NaN   4755.011504   
1  MK40  E30000166    NaN  2865.080106  9144.556605    NaN   8593.948235   
2  MK40  E30000166    NaN  4852.254853  8349.959437    NaN  14084.552692   
3  MK40  E30000166    NaN  2456.193909  7938.729718    NaN   6732.103818   
4  MK40  E30000166    NaN  3197.469028  7165.813173    NaN   5909.054386   

          wg3_k  wg1_l       wg2_l       wg3_l  w2g1_k      wg2wg1_k  \
0  24599.793029    NaN   49.700000  127.923077     NaN   7232.663031   
1  35145.498416    NaN   49.166667  170.362745     NaN   5497.568749   
2  24619.379339    NaN  185.666667  146.927273     NaN  29545.114627   
3  30545.259634    NaN   60.727273  152.183099     NaN   8665.523750   
4  22491.508253    NaN   73.166667  125.280702     NaN  13009.818416   

       wg3wg1_k  w2g1_l    wg2wg1_l    wg3wg1_l  wg1wg2_k        w2g2_k  \
0  31550.843548     NaN   43.166667  135.351852       NaN   4495.926331   
1  44474.098329     NaN   41.625000  181.307087       NaN   8188.823557   
2  30884.717836     NaN  448.000000  148.468750       NaN  11193.641227   
3  52776.155424     NaN   18.000000  173.909091       NaN   5796.365645   
4  29166.051512     NaN  103.666667  116.062500       NaN   5572.465150   

       wg3wg2_k  wg1wg2_l      w2g2_l    wg3wg2_l  wg1wg3_k      wg2wg3_k  \
0  24291.042573       NaN   49.163289  127.678290       NaN  24599.793029   
1  34257.526110       NaN   49.701162  167.114640       NaN  35145.498416   
2  25027.189668       NaN  153.944444  151.065255       NaN  24619.379339   
3  29485.436917       NaN   62.049587  146.429378       NaN  30545.259634   
4  22276.786984       NaN   70.826616  126.902540       NaN  22491.508253   

         w2g3_k  wg1wg3_l    wg2wg3_l      w2g3_l  w3g1_k  w3g1_l  \
0  21844.220326       NaN  127.923077  117.121086     NaN     NaN   
1  31867.445974       NaN  170.362745  156.759936     NaN     NaN   
2  23787.130301       NaN  146.927273  146.312563     NaN     NaN   
3  26570.999396       NaN  152.183099  135.997393     NaN     NaN   
4  20283.405789       NaN  125.280702  117.439060     NaN     NaN   

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
  registered_number  year           gva   total_assets  employees  \
0          14172083  2022  28364.492116  528581.217018        132   
1          12481595  2023   1156.863472   19678.503111         59   
2          02425634  2012   4340.412570    6417.752783        100   
3          02863356  2012    284.375457    7680.100229         16   
4          02796201  2007   2113.558249    2063.751960         34   

           wd1_y         wd2_y          wd3_y         wd1_k          wd2_k  \
0   35218.041366  19237.940354  119801.090514  2.503386e+05   57595.578605   
1   81823.324184  78200.479574  114637.427340  3.185941e+05  192066.614734   
2  112436.254716   6968.982694  156467.542858  1.145691e+06   57317.681511   
3   69663.379359   1600.583733  102480.934062  9.803319e+05    7387.445263   
4   11467.501273   8092.738834  105133.705103  4.410169e+04   17181.405295   

          wd3_k        wd1_l        wd2_l        wd3_l        w2d1_k  \
0  1.177067e+06   541.231832   478.056246   894.584977  4.274595e+05   
1  1.088138e+06  1281.147531  1344.817308   923.859700  4.328494e+05   
2  1.331286e+06   877.208994    35.851964  1118.720581  1.404325e+06   
3  1.271436e+06   673.834432    55.734257   962.193987  1.326670e+06   
4  6.539416e+05   218.947503   190.291955   945.475960  6.693554e+04   

        w2d1_l         w2d2_k       w2d2_l        w2d3_k       w2d3_l  \
0   593.879156   75877.877065   464.783775  1.370346e+06   940.831231   
1  1206.944845  187771.889460  1308.332734  1.293302e+06   973.534047   
2  1097.147983   14699.663765   107.081488  1.519380e+06  1224.587964   
3   898.073843   10851.800519    38.677085  1.692346e+06  1042.848431   
4   244.823600   17020.940244   188.511208  8.446735e+05  1104.232798   

         w3d1_k       w3d1_l  (i-wd1)w2d1_k  (i-wd1)w2d1_l  (i-vd1)w2d1_k  \
0  5.632555e+05   650.431656 -135796.014937     -56.552500 -842189.534928   
1  5.378725e+05  1174.154790 -105023.126894      32.790054 -921695.628736   
2  1.467504e+06  1162.838025  -63179.633822     -65.690042 -235900.255185   
3  1.441415e+06   987.383152 -114745.014341     -89.309309 -417132.364677   
4  8.722434e+04   271.421124  -20288.806915     -26.597524 -626478.727559   

   (i-vd1)w2d1_l        w4d1_k       w4d1_l  (i-wd1)w3d1_k  (i-wd1)w3d1_l  \
0    -309.447636  6.760943e+05   697.697822 -112838.758338     -47.266165   
1     251.994884  6.298813e+05  1146.230491  -92008.802348      27.924299   
2     -59.824854  1.474539e+06  1179.015340   -7034.542101     -16.177315   
3    -199.153246  1.487953e+06  1021.819596  -46537.642819     -34.436445   
4    -814.244279  1.051914e+05   296.476412  -17967.024082     -25.055288   

   (i-vd1)w3d1_k  (i-vd1)w3d1_l  
0 -697273.209633    -256.916623  
1 -805006.205116     214.201229  
2 -145604.636818       9.210586  
3 -271887.527329    -111.418310  
4 -541806.757621    -760.834175  
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

