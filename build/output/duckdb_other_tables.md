# Other Tables in DuckDB database

## working_yearly_peers

### Number of rows: 1,081,520

### Schema:

```
ibis.Schema {
  registered_number    string
  year                 int64
  tfp_pc8              float64
  gva1_pc8             float64
  total_assets_pc8     float64
  employees_pc8        float64
  tfp_pc4_d            float64
  gva1_pc4_d           float64
  total_assets_pc4_d   float64
  employees_pc4_d      float64
  tfp_ttwa_d           float64
  gva1_ttwa_d          float64
  total_assets_ttwa_d  float64
  employees_ttwa_d     float64
}
```

## extended_yearly

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
}
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

