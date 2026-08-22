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
  registered_number  year  employees  average_wage           gva1  \
0          07404078  2023         30     12.917756     440.659867   
1          NI031527  2023         62     14.636052    1020.697635   
2          14771570  2023         61     45.575182    3980.371124   
3          13264637  2023       2269     96.326896  281906.284838   
4          13355740  2023         55     48.856937    5019.654347   

            gva2  gva1_per_worker  gva2_per_worker registered_number_right  \
0     452.404906        14.688662        15.080164                07404078   
1            NaN        16.462865              NaN                NI031527   
2    2376.708514        65.251986        38.962435                14771570   
3  334707.946978       124.242523       147.513419                13264637   
4    3257.513342        91.266443        59.227515                13355740   

                         company_name  is_public industry_codes  \
0                    TIPS4CHOICES CIC      False       85,88,86   
1                 DERRY THEATRE TRUST      False          93,90   
2       PROJECT CARIBOU BIDCO LIMITED      False             64   
3                   DARKTRACE LIMITED       True          64,62   
4  WESTWOOD PROJECTS HOLDINGS LIMITED      False             64   

            file_codes   sic6  \
0  17_32,16_51,17_50 3  85590   
1          17_15,16_59  90040   
2                12_47  64209   
3          12_47,18_29  62012   
4                12_47  64209   

                                           sic6_desc    lat_dec   lon_dec  \
0                             Other education n.e.c.  51.562137 -1.790839   
1                       Operation of arts facilities  54.995056 -7.319778   
2  Activities of other holding companies (not inc...  53.387306 -2.599222   
3         Business and domestic software development  52.234255  0.151849   
4  Activities of other holding companies (not inc...  51.883627  0.826436   

   address_lvl address_case       ttwa   pc4           lat_lon5  
0            2          pta  E30000276   SN1  51.56214,-1.79084  
1            1          pta  N12000006  BT48  54.99506,-7.31978  
2            1           ro  E30000284   WA1  53.38731,-2.59922  
3            2          pta  E30000186   CB4   52.23426,0.15185  
4            2           ro  E30000193   CO3   51.88363,0.82644  
```

## view_centroids_pc4

### Number of rows: 2,688

### Schema:

```
ibis.Schema {
  pc4    string
  ttwa   string
  c_lon  float64
  c_lat  float64
}
```

### Head of table:

```
    pc4       ttwa     c_lon      c_lat
0  WC1X  E30000234 -0.123036  51.528758
1  WC2E  E30000234 -0.161927  51.543779
2  WC2H  E30000234 -0.192251  51.533907
3   WR7  E30000169 -2.130778  52.169861
4  BD21  E30000018 -1.855785  53.839775
```

## view_centroids_ttwa

### Number of rows: 228

### Schema:

```
ibis.Schema {
  ttwa   string
  c_lon  float64
  c_lat  float64
}
```

### Head of table:

```
        ttwa     c_lon      c_lat
0  E30000237 -0.418375  51.766416
1  E30000046 -2.434190  50.657802
2  S22000063 -2.856921  55.615304
3  E30000029 -1.841078  53.660696
4  E30000232 -4.440537  50.447706
```

## view_prelim_centroids

### Number of rows: 2,688

### Schema:

```
ibis.Schema {
  pc4         string
  prelim_lon  float64
  prelim_lat  float64
}
```

### Head of table:

```
    pc4  prelim_lon  prelim_lat
0  WC1B   -0.141121   51.527876
1  WC2B   -0.176210   51.529686
2   WF1   -1.493024   53.655778
3  WS12   -1.991307   52.707806
4   BB5   -2.306393   53.692913
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
  registered_number  year  employees    fixed_total   total_assets  \
0          04687714  2017        354  171750.433705  306807.558860   
1          00745573  2011         47    1666.959742   15781.644867   
2          01385533  2012        257   12465.362859   16225.054600   
3          03892046  2011         47    7244.332917   27573.065289   
4          07088219  2011        222  102207.389946  195099.072011   

   average_wage          gva1          gva2  gva1_per_worker  gva2_per_worker  \
0     56.530986  44474.174812  37301.482085       125.633262       105.371418   
1     61.897106   3956.504195   4323.370400        84.180940        91.986604   
2     29.489396  10596.185171  10496.917780        41.230292        40.844038   
3     60.509770   2447.295529   2916.337241        52.070118        62.049729   
4     88.422196  48299.633814  44520.224568       217.565918       200.541552   

        tfp registered_number_right                     company_name  \
0  3.463775                04687714  INEOS ENTERPRISES GROUP LIMITED   
1  3.139632                00745573       FRANK ARMITT & SON LIMITED   
2  3.068774                01385533           SELWYNS TRAVEL LIMITED   
3  2.499454                03892046                      SOG LIMITED   
4  3.963793                07088219              MEXICHEM UK LIMITED   

   is_public industry_codes   file_codes   sic6  \
0      False             20        22_11  20130   
1      False          49,52  16_44,17_05  49410   
2      False             49        16_44  49390   
3      False             81        14_50  81100   
4      False             20        22_11  20110   

                                        sic6_desc    lat_dec   lon_dec  \
0  Manufacture of other inorganic basic chemicals  53.322848 -2.748511   
1                       Freight transport by road  53.323778 -2.738472   
2           Other passenger land transport n.e.c.  51.434306 -0.351528   
3          Combined facilities support activities  53.325791 -2.694468   
4                 Manufacture of industrial gases  53.324698 -2.732899   

   address_lvl address_case      pc8       ttwa  pc4           lat_lon5  
0            2           ro  WA7 4EL  E30000284  WA7  53.32285,-2.74851  
1            1          pta  WA7 4EZ  E30000284  WA7  53.32378,-2.73847  
2            1          pta  WA7 4LU  E30000284  WA7  51.43431,-0.35153  
3            2          pta  WA7 4QF  E30000284  WA7  53.32579,-2.69447  
4            2          pta  WA7 4QX  E30000284  WA7    53.3247,-2.7329  
```

