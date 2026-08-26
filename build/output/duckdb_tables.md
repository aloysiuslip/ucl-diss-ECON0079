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
0        DN20         DN20 8NQ    England   53� 33' 3.6" N  0� 29' 50.4" W   
1        GL15         GL15 5HE    England              NaN             NaN   
2        GU34         GU34 1HN    England   51� 8' 58.6" N  0� 58' 39.6" W   
3        TN13         TN13 2OB    England  51� 16' 46.4" N   0� 9' 19.9" E   
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
2                  51� 30' 51.9" N                    0� 33' 25.8" W   
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

## working_yearly_with_tfp_wave

### Number of rows: 1,096,814

### Schema:

```
ibis.Schema {
  registered_number    string
  year                 int64
  employees            int64
  fixed_total          float64
  total_assets         float64
  average_wage         float64
  gva1                 float64
  gva2                 float64
  gva1_per_worker      float64
  gva2_per_worker      float64
  tfp                  float64
  peer_tfp_pc8         float64
  peer_tfp_pc4_donut   float64
  peer_tfp_ttwa_donut  float64
  tfp_wav1             float64
  tfp_wav2             float64
  tfp_wav3             float64
  nb_peers             int64
  sim_pc1              float64
  sim_pc2              float64
  sim_pc3              float64
  sim_pc4              float64
  sim_pc5              float64
  sim_pc6              float64
}
```

### Head of table:

```
  registered_number  year  employees   fixed_total  total_assets  \
0          NI044811  2021         71    661.323500   8254.856167   
1          NI054912  2017         52   8856.693497  20497.115191   
2          SC023206  2006        327  24963.088102  48128.353038   
3          07135945  2022         16   5379.048902   6463.960544   
4          07330611  2014         93   3563.211671  11941.496122   

   average_wage          gva1          gva2  gva1_per_worker  gva2_per_worker  \
0     38.343804   3523.441699   3354.333585        49.625939        47.244135   
1     44.486593   7425.226586   7109.498435       142.792819       136.721124   
2     37.487403  16916.157981  23725.424711        51.731370        72.554816   
3     22.732035    770.234572           NaN        48.139661              NaN   
4     21.538988   3824.227804   3608.993655        41.120729        38.806383   

        tfp  peer_tfp_pc8  peer_tfp_pc4_donut  peer_tfp_ttwa_donut  tfp_wav1  \
0  2.954811           NaN            2.880356             2.953783  2.776443   
1  3.631917      2.767808            2.636775             2.903767  2.678653   
2  3.076560      2.996573            2.773346             2.922956  2.996107   
3  2.423576           NaN            2.773894             2.831035  2.816255   
4  2.764480      2.638131            2.685648             2.812639  2.638874   

   tfp_wav2  tfp_wav3  nb_peers   sim_pc1   sim_pc2   sim_pc3   sim_pc4  \
0  2.716846  2.738847        10 -0.062090  0.073961  1.882041 -0.046577   
1  2.677659  2.746761        18 -0.060159  0.076322  2.004135 -0.049690   
2  2.996572  2.918669         6 -0.046119  0.035605  2.027395 -0.078492   
3  2.739396  2.728552        11 -0.067212  0.078236  2.015701 -0.054537   
4  2.638131  2.693827        14 -0.069149  0.077660  1.918361 -0.039834   

    sim_pc5   sim_pc6  
0  0.012526  0.038465  
1  0.017989 -0.141442  
2 -0.003836 -0.296406  
3  0.017346 -0.216961  
4  0.028963 -0.194258  
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

