# Other Tables in DuckDB database

## temp_spatial_pairs

### Number of rows: 574

### Schema:

```
ibis.Schema {
  registered_number_i  string
  lon_dec_i            float64
  lat_dec_i            float64
  registered_number_j  string
  lon_dec_j            float64
  lat_dec_j            float64
}
```

### Head of table:

```
  registered_number_i  lon_dec_i  lat_dec_i registered_number_j  lon_dec_j  \
0            11243426  -2.655669  53.656073            05842808  -2.626556   
1            11243426  -2.655669  53.656073            04728092  -2.660528   
2            11243426  -2.655669  53.656073            11251227  -2.663115   
3            11243426  -2.655669  53.656073            10473528  -2.673139   
4            11243426  -2.655669  53.656073            04820532  -2.668556   

   lat_dec_j  
0  53.666333  
1  53.584611  
2  53.586649  
3  53.592417  
4  53.589833  
```

## temp_random_peers

### Number of rows: 558

### Schema:

```
ibis.Schema {
  firm_target               string
  firm_peer                 string
  distance_meters           float64
  registered_number_target  string
  ttwa_target               string
  pc8_target                string
  lat_dec_target            float64
  lon_dec_target            float64
  registered_number_peer    string
  ttwa_peer                 string
  pc8_peer                  string
  lat_dec_peer              float64
  lon_dec_peer              float64
}
```

### Head of table:

```
  firm_target firm_peer  distance_meters registered_number_target ttwa_target  \
0    05802836  07200267      3660.148004                 05802836   E30000255   
1    05802836  11497671      3171.662756                 05802836   E30000255   
2    05802836  04085927      1023.730089                 05802836   E30000255   
3    00907939  00328298      3839.927562                 00907939   E30000255   
4    05802836  08765369      4763.353364                 05802836   E30000255   

  pc8_target  lat_dec_target  lon_dec_target registered_number_peer  \
0    PR7 7EL       53.674349       -2.655135               07200267   
1    PR7 7EL       53.674349       -2.655135               11497671   
2    PR7 7EL       53.674349       -2.655135               04085927   
3    PR1 3JJ       53.741333       -2.670806               00328298   
4    PR7 7EL       53.674349       -2.655135               08765369   

   ttwa_peer  pc8_peer  lat_dec_peer  lon_dec_peer  
0  E30000233   L39 4RY     53.659667     -2.625667  
1  E30000255   PR7 1JE     53.653611     -2.635528  
2  E30000255   PR7 7DW     53.672366     -2.646144  
3  E30000255   PR5 8AS     53.724861     -2.640444  
4  E30000255  PR25 2NB     53.694139     -2.693139  
```

