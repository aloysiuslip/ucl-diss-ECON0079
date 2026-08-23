# Other Tables in DuckDB database

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

