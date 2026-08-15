# Other Tables in DuckDB database

## fame_yearly_consolidated

### Number of rows: 47,456,502

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
0          IE038100  2006         False       NaN           83.255069   
1          IE210547  2006         False       NaN          -91.530930   
2          IE347763  2006         False       NaN                 NaN   
3          04497426  2006         False       NaN          -17.744000   
4          SC192159  2006         False       NaN           53.493000   

   profit_loss_pretax employees   tangibles  tangibles_land_and_buildings  \
0                 NaN      None  463.843315                           NaN   
1                 NaN      None         NaN                           NaN   
2                 NaN      None         NaN                           NaN   
3                 NaN      None    0.928000                           NaN   
4                 NaN      None   14.439000                           NaN   

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
0          NaN          NaN                NaN   463.843315  -457.802590   
1          NaN          NaN                NaN          NaN   -92.427688   
2          NaN          NaN                NaN          NaN          NaN   
3          NaN          NaN                NaN     0.928000   -28.172000   
4          NaN       57.697                NaN    72.136000  -121.089000   

   total_assets  liabilites_lt  cos  admin_expenses  interest_paid  \
0   1749.742728   -1208.685068  NaN             NaN            NaN   
1      0.896758            NaN  NaN             NaN            NaN   
2           NaN            NaN  NaN             NaN            NaN   
3     10.428000            NaN  NaN             NaN            NaN   
4    175.906000      -1.324000  NaN             NaN            NaN   

   profit_loss_pretax2  tax  dividends  depreciation  r_and_d  \
0                  NaN  NaN        NaN           NaN      NaN   
1                  NaN  NaN        NaN           NaN      NaN   
2                  NaN  NaN        NaN           NaN      NaN   
3                  NaN  NaN        NaN           NaN      NaN   
4                  NaN  NaN        NaN           NaN      NaN   

   remuneration_employees  wages  social_security_costs  pensions_costs  \
0                     NaN    NaN                    NaN             NaN   
1                     NaN    NaN                    NaN             NaN   
2                     NaN    NaN                    NaN             NaN   
3                     NaN    NaN                    NaN             NaN   
4                     NaN    NaN                    NaN             NaN   

   other_staff_costs  renumeration_directors  ebitda  
0                NaN                     NaN     NaN  
1                NaN                     NaN     NaN  
2                NaN                     NaN     NaN  
3                NaN                     NaN     NaN  
4                NaN                     NaN     NaN  
```

## working_yearly_kp

### Number of rows: 40,846,539

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
0          05132111  2006         False       NaN           12.431737   
1          02372503  2006         False       NaN           -5.620690   
2          04364733  2006         False       NaN           -0.602273   
3          02200237  2006         False       NaN        15079.604543   
4          02605684  2006         False       NaN          -58.811499   

   profit_loss_pretax employees  tangibles  tangibles_land_and_buildings  \
0                 NaN      None        NaN                           NaN   
1                 NaN      None        NaN                           NaN   
2                 NaN      None        NaN                           NaN   
3                 NaN      None        NaN                           NaN   
4                 NaN      None   1.683842                           NaN   

   tangibles_land_freehold  tangibles_land_leasehold  tangibles_fixt_fit  \
0                      NaN                       NaN                 NaN   
1                      NaN                       NaN                 NaN   
2                      NaN                       NaN                 NaN   
3                      NaN                       NaN                 NaN   
4                      NaN                       NaN            1.683842   

   tangibles_plant_and_vehicles  tangibles_plant  tangibles_vehicles  \
0                           NaN              NaN                 NaN   
1                           NaN              NaN                 NaN   
2                           NaN              NaN                 NaN   
3                           NaN              NaN                 NaN   
4                           NaN              NaN                 NaN   

   fixed_other  intangibles  investments_other   fixed_total   liabilities  \
0          NaN          NaN                NaN           NaN     -2.029124   
1          NaN          NaN           0.003153      0.003153     -5.623844   
2          NaN          NaN                NaN           NaN     -0.630653   
3          NaN          NaN       20701.333983  20701.333983 -29344.827012   
4          NaN          NaN                NaN      1.683842    -65.357672   

   total_assets  liabilites_lt  cos  admin_expenses  interest_paid  \
0     14.460862            NaN  NaN             NaN            NaN   
1      0.003153            NaN  NaN             NaN            NaN   
2      0.028379            NaN  NaN             NaN            NaN   
3  44424.431555            NaN  NaN             NaN            NaN   
4      6.546173            NaN  NaN             NaN            NaN   

   profit_loss_pretax2  tax  dividends  depreciation  r_and_d  \
0                  NaN  NaN        NaN           NaN      NaN   
1                  NaN  NaN        NaN           NaN      NaN   
2                  NaN  NaN        NaN           NaN      NaN   
3                  NaN  NaN        NaN           NaN      NaN   
4                  NaN  NaN        NaN           NaN      NaN   

   remuneration_employees  wages  social_security_costs  pensions_costs  \
0                     NaN    NaN                    NaN             NaN   
1                     NaN    NaN                    NaN             NaN   
2                     NaN    NaN                    NaN             NaN   
3                     NaN    NaN                    NaN             NaN   
4                     NaN    NaN                    NaN             NaN   

   other_staff_costs  renumeration_directors  ebitda  
0                NaN                     NaN     NaN  
1                NaN                     NaN     NaN  
2                NaN                     NaN     NaN  
3                NaN                     NaN     NaN  
4                NaN                     NaN     NaN  
```

## ibis_duckdb_table_5zx4zftkrrghva5cz65r3u2ery

### Number of rows: 0

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
Empty DataFrame
Columns: [registered_number, year, consolidated, turnover, shareholders_funds, profit_loss_pretax, employees, tangibles, tangibles_land_and_buildings, tangibles_land_freehold, tangibles_land_leasehold, tangibles_fixt_fit, tangibles_plant_and_vehicles, tangibles_plant, tangibles_vehicles, fixed_other, intangibles, investments_other, fixed_total, liabilities, total_assets, liabilites_lt, cos, admin_expenses, interest_paid, profit_loss_pretax2, tax, dividends, depreciation, r_and_d, remuneration_employees, wages, social_security_costs, pensions_costs, other_staff_costs, renumeration_directors, ebitda]
Index: []
```

## ibis_duckdb_table_ttloxf4cjbgjzm4w7623raglci

### Number of rows: 0

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
Empty DataFrame
Columns: [registered_number, year, consolidated, turnover, shareholders_funds, profit_loss_pretax, employees, tangibles, tangibles_land_and_buildings, tangibles_land_freehold, tangibles_land_leasehold, tangibles_fixt_fit, tangibles_plant_and_vehicles, tangibles_plant, tangibles_vehicles, fixed_other, intangibles, investments_other, fixed_total, liabilities, total_assets, liabilites_lt, cos, admin_expenses, interest_paid, profit_loss_pretax2, tax, dividends, depreciation, r_and_d, remuneration_employees, wages, social_security_costs, pensions_costs, other_staff_costs, renumeration_directors, ebitda]
Index: []
```

## fame_derived_clean

### Number of rows: 8,771,336

### Schema:

```
ibis.Schema {
  registered_number            string
  has_ptaddress                boolean
  has_ptaddress_latlong        boolean
  is_public                    boolean
  has_company_branch_mismatch  boolean
  industry_codes               string
  file_codes                   string
}
```

### Head of table:

```
  registered_number  has_ptaddress  has_ptaddress_latlong  is_public  \
0          11899400          False                  False      False   
1          08817563          False                  False      False   
2          SC434537           True                  False      False   
3          02874653           True                  False      False   
4          03295446          False                  False      False   

  has_company_branch_mismatch industry_codes file_codes  
0                       False             99      12_49  
1                        None             99      12_49  
2                       False             99      12_49  
3                       False             99      12_49  
4                        None             99      12_49  
```

## fame_yearly_clean

### Number of rows: 45,609,753

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
0          05930391  2014         False       NaN               6.300   
1          06086182  2009         False       NaN               0.001   
2          06090468  2008         False       NaN               0.280   
3          14263317  2023         False       NaN               0.002   
4          00876306  2010         False       NaN             783.064   

   profit_loss_pretax employees  tangibles  tangibles_land_and_buildings  \
0                 NaN      None        NaN                           NaN   
1                 NaN      None        NaN                           NaN   
2                 NaN      None      1.041                           NaN   
3                 NaN      None        NaN                           NaN   
4                 NaN      None        NaN                           NaN   

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
0          NaN          NaN                NaN          NaN          NaN   
1          NaN          NaN                NaN          NaN          NaN   
2          NaN          NaN                NaN        1.041       -2.249   
3          NaN          NaN                NaN          NaN          NaN   
4          NaN          NaN                NaN          NaN      -19.633   

   total_assets  liabilites_lt  cos  admin_expenses  interest_paid  \
0         6.300            NaN  NaN             NaN            NaN   
1         0.001            NaN  NaN             NaN            NaN   
2         2.529            NaN  NaN             NaN            NaN   
3         0.002            NaN  NaN             NaN            NaN   
4       802.697            NaN  NaN             NaN            NaN   

   profit_loss_pretax2  tax  dividends  depreciation  r_and_d  \
0                  NaN  NaN        NaN           NaN      NaN   
1                  NaN  NaN        NaN           NaN      NaN   
2                  NaN  NaN        NaN         0.334      NaN   
3                  NaN  NaN        NaN           NaN      NaN   
4                  NaN  NaN        NaN           NaN      NaN   

   remuneration_employees  wages  social_security_costs  pensions_costs  \
0                     NaN    NaN                    NaN             NaN   
1                     NaN    NaN                    NaN             NaN   
2                     NaN    NaN                    NaN             NaN   
3                     NaN    NaN                    NaN             NaN   
4                     NaN    NaN                    NaN             NaN   

   other_staff_costs  renumeration_directors  ebitda  
0                NaN                     NaN     NaN  
1                NaN                     NaN     NaN  
2                NaN                     NaN     NaN  
3                NaN                     NaN     NaN  
4                NaN                     NaN     NaN  
```

## ibis_duckdb_table_lff3ldqskrawrhvksgv3c3k2bu

### Number of rows: 0

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
Empty DataFrame
Columns: [registered_number, year, consolidated, turnover, shareholders_funds, profit_loss_pretax, employees, tangibles, tangibles_land_and_buildings, tangibles_land_freehold, tangibles_land_leasehold, tangibles_fixt_fit, tangibles_plant_and_vehicles, tangibles_plant, tangibles_vehicles, fixed_other, intangibles, investments_other, fixed_total, liabilities, total_assets, liabilites_lt, cos, admin_expenses, interest_paid, profit_loss_pretax2, tax, dividends, depreciation, r_and_d, remuneration_employees, wages, social_security_costs, pensions_costs, other_staff_costs, renumeration_directors, ebitda]
Index: []
```

# Other Tables in DuckDB database

## fame_yearly_consolidated

### Number of rows: 47,456,502

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
0          IE038100  2006         False       NaN           83.255069   
1          IE210547  2006         False       NaN          -91.530930   
2          IE347763  2006         False       NaN                 NaN   
3          04497426  2006         False       NaN          -17.744000   
4          SC192159  2006         False       NaN           53.493000   

   profit_loss_pretax employees   tangibles  tangibles_land_and_buildings  \
0                 NaN      None  463.843315                           NaN   
1                 NaN      None         NaN                           NaN   
2                 NaN      None         NaN                           NaN   
3                 NaN      None    0.928000                           NaN   
4                 NaN      None   14.439000                           NaN   

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
0          NaN          NaN                NaN   463.843315  -457.802590   
1          NaN          NaN                NaN          NaN   -92.427688   
2          NaN          NaN                NaN          NaN          NaN   
3          NaN          NaN                NaN     0.928000   -28.172000   
4          NaN       57.697                NaN    72.136000  -121.089000   

   total_assets  liabilites_lt  cos  admin_expenses  interest_paid  \
0   1749.742728   -1208.685068  NaN             NaN            NaN   
1      0.896758            NaN  NaN             NaN            NaN   
2           NaN            NaN  NaN             NaN            NaN   
3     10.428000            NaN  NaN             NaN            NaN   
4    175.906000      -1.324000  NaN             NaN            NaN   

   profit_loss_pretax2  tax  dividends  depreciation  r_and_d  \
0                  NaN  NaN        NaN           NaN      NaN   
1                  NaN  NaN        NaN           NaN      NaN   
2                  NaN  NaN        NaN           NaN      NaN   
3                  NaN  NaN        NaN           NaN      NaN   
4                  NaN  NaN        NaN           NaN      NaN   

   remuneration_employees  wages  social_security_costs  pensions_costs  \
0                     NaN    NaN                    NaN             NaN   
1                     NaN    NaN                    NaN             NaN   
2                     NaN    NaN                    NaN             NaN   
3                     NaN    NaN                    NaN             NaN   
4                     NaN    NaN                    NaN             NaN   

   other_staff_costs  renumeration_directors  ebitda  
0                NaN                     NaN     NaN  
1                NaN                     NaN     NaN  
2                NaN                     NaN     NaN  
3                NaN                     NaN     NaN  
4                NaN                     NaN     NaN  
```

## working_yearly_kp

### Number of rows: 40,846,539

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
0          05132111  2006         False       NaN           12.431737   
1          02372503  2006         False       NaN           -5.620690   
2          04364733  2006         False       NaN           -0.602273   
3          02200237  2006         False       NaN        15079.604543   
4          02605684  2006         False       NaN          -58.811499   

   profit_loss_pretax employees  tangibles  tangibles_land_and_buildings  \
0                 NaN      None        NaN                           NaN   
1                 NaN      None        NaN                           NaN   
2                 NaN      None        NaN                           NaN   
3                 NaN      None        NaN                           NaN   
4                 NaN      None   1.683842                           NaN   

   tangibles_land_freehold  tangibles_land_leasehold  tangibles_fixt_fit  \
0                      NaN                       NaN                 NaN   
1                      NaN                       NaN                 NaN   
2                      NaN                       NaN                 NaN   
3                      NaN                       NaN                 NaN   
4                      NaN                       NaN            1.683842   

   tangibles_plant_and_vehicles  tangibles_plant  tangibles_vehicles  \
0                           NaN              NaN                 NaN   
1                           NaN              NaN                 NaN   
2                           NaN              NaN                 NaN   
3                           NaN              NaN                 NaN   
4                           NaN              NaN                 NaN   

   fixed_other  intangibles  investments_other   fixed_total   liabilities  \
0          NaN          NaN                NaN           NaN     -2.029124   
1          NaN          NaN           0.003153      0.003153     -5.623844   
2          NaN          NaN                NaN           NaN     -0.630653   
3          NaN          NaN       20701.333983  20701.333983 -29344.827012   
4          NaN          NaN                NaN      1.683842    -65.357672   

   total_assets  liabilites_lt  cos  admin_expenses  interest_paid  \
0     14.460862            NaN  NaN             NaN            NaN   
1      0.003153            NaN  NaN             NaN            NaN   
2      0.028379            NaN  NaN             NaN            NaN   
3  44424.431555            NaN  NaN             NaN            NaN   
4      6.546173            NaN  NaN             NaN            NaN   

   profit_loss_pretax2  tax  dividends  depreciation  r_and_d  \
0                  NaN  NaN        NaN           NaN      NaN   
1                  NaN  NaN        NaN           NaN      NaN   
2                  NaN  NaN        NaN           NaN      NaN   
3                  NaN  NaN        NaN           NaN      NaN   
4                  NaN  NaN        NaN           NaN      NaN   

   remuneration_employees  wages  social_security_costs  pensions_costs  \
0                     NaN    NaN                    NaN             NaN   
1                     NaN    NaN                    NaN             NaN   
2                     NaN    NaN                    NaN             NaN   
3                     NaN    NaN                    NaN             NaN   
4                     NaN    NaN                    NaN             NaN   

   other_staff_costs  renumeration_directors  ebitda  
0                NaN                     NaN     NaN  
1                NaN                     NaN     NaN  
2                NaN                     NaN     NaN  
3                NaN                     NaN     NaN  
4                NaN                     NaN     NaN  
```

# Other Tables in DuckDB database

## fame_yearly_consolidated

### Number of rows: 47,456,502

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
0          IE038100  2006         False       NaN           83.255069   
1          IE210547  2006         False       NaN          -91.530930   
2          IE347763  2006         False       NaN                 NaN   
3          04497426  2006         False       NaN          -17.744000   
4          SC192159  2006         False       NaN           53.493000   

   profit_loss_pretax employees   tangibles  tangibles_land_and_buildings  \
0                 NaN      None  463.843315                           NaN   
1                 NaN      None         NaN                           NaN   
2                 NaN      None         NaN                           NaN   
3                 NaN      None    0.928000                           NaN   
4                 NaN      None   14.439000                           NaN   

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
0          NaN          NaN                NaN   463.843315  -457.802590   
1          NaN          NaN                NaN          NaN   -92.427688   
2          NaN          NaN                NaN          NaN          NaN   
3          NaN          NaN                NaN     0.928000   -28.172000   
4          NaN       57.697                NaN    72.136000  -121.089000   

   total_assets  liabilites_lt  cos  admin_expenses  interest_paid  \
0   1749.742728   -1208.685068  NaN             NaN            NaN   
1      0.896758            NaN  NaN             NaN            NaN   
2           NaN            NaN  NaN             NaN            NaN   
3     10.428000            NaN  NaN             NaN            NaN   
4    175.906000      -1.324000  NaN             NaN            NaN   

   profit_loss_pretax2  tax  dividends  depreciation  r_and_d  \
0                  NaN  NaN        NaN           NaN      NaN   
1                  NaN  NaN        NaN           NaN      NaN   
2                  NaN  NaN        NaN           NaN      NaN   
3                  NaN  NaN        NaN           NaN      NaN   
4                  NaN  NaN        NaN           NaN      NaN   

   remuneration_employees  wages  social_security_costs  pensions_costs  \
0                     NaN    NaN                    NaN             NaN   
1                     NaN    NaN                    NaN             NaN   
2                     NaN    NaN                    NaN             NaN   
3                     NaN    NaN                    NaN             NaN   
4                     NaN    NaN                    NaN             NaN   

   other_staff_costs  renumeration_directors  ebitda  
0                NaN                     NaN     NaN  
1                NaN                     NaN     NaN  
2                NaN                     NaN     NaN  
3                NaN                     NaN     NaN  
4                NaN                     NaN     NaN  
```

## working_yearly_kp

### Number of rows: 40,846,539

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
0          05132111  2006         False       NaN           12.431737   
1          02372503  2006         False       NaN           -5.620690   
2          04364733  2006         False       NaN           -0.602273   
3          02200237  2006         False       NaN        15079.604543   
4          02605684  2006         False       NaN          -58.811499   

   profit_loss_pretax employees  tangibles  tangibles_land_and_buildings  \
0                 NaN      None        NaN                           NaN   
1                 NaN      None        NaN                           NaN   
2                 NaN      None        NaN                           NaN   
3                 NaN      None        NaN                           NaN   
4                 NaN      None   1.683842                           NaN   

   tangibles_land_freehold  tangibles_land_leasehold  tangibles_fixt_fit  \
0                      NaN                       NaN                 NaN   
1                      NaN                       NaN                 NaN   
2                      NaN                       NaN                 NaN   
3                      NaN                       NaN                 NaN   
4                      NaN                       NaN            1.683842   

   tangibles_plant_and_vehicles  tangibles_plant  tangibles_vehicles  \
0                           NaN              NaN                 NaN   
1                           NaN              NaN                 NaN   
2                           NaN              NaN                 NaN   
3                           NaN              NaN                 NaN   
4                           NaN              NaN                 NaN   

   fixed_other  intangibles  investments_other   fixed_total   liabilities  \
0          NaN          NaN                NaN           NaN     -2.029124   
1          NaN          NaN           0.003153      0.003153     -5.623844   
2          NaN          NaN                NaN           NaN     -0.630653   
3          NaN          NaN       20701.333983  20701.333983 -29344.827012   
4          NaN          NaN                NaN      1.683842    -65.357672   

   total_assets  liabilites_lt  cos  admin_expenses  interest_paid  \
0     14.460862            NaN  NaN             NaN            NaN   
1      0.003153            NaN  NaN             NaN            NaN   
2      0.028379            NaN  NaN             NaN            NaN   
3  44424.431555            NaN  NaN             NaN            NaN   
4      6.546173            NaN  NaN             NaN            NaN   

   profit_loss_pretax2  tax  dividends  depreciation  r_and_d  \
0                  NaN  NaN        NaN           NaN      NaN   
1                  NaN  NaN        NaN           NaN      NaN   
2                  NaN  NaN        NaN           NaN      NaN   
3                  NaN  NaN        NaN           NaN      NaN   
4                  NaN  NaN        NaN           NaN      NaN   

   remuneration_employees  wages  social_security_costs  pensions_costs  \
0                     NaN    NaN                    NaN             NaN   
1                     NaN    NaN                    NaN             NaN   
2                     NaN    NaN                    NaN             NaN   
3                     NaN    NaN                    NaN             NaN   
4                     NaN    NaN                    NaN             NaN   

   other_staff_costs  renumeration_directors  ebitda  
0                NaN                     NaN     NaN  
1                NaN                     NaN     NaN  
2                NaN                     NaN     NaN  
3                NaN                     NaN     NaN  
4                NaN                     NaN     NaN  
```

# Other Tables in DuckDB database

## fame_yearly_consolidated

### Number of rows: 47,456,502

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
0          IE038100  2006         False       NaN           83.255069   
1          IE210547  2006         False       NaN          -91.530930   
2          IE347763  2006         False       NaN                 NaN   
3          04497426  2006         False       NaN          -17.744000   
4          SC192159  2006         False       NaN           53.493000   

   profit_loss_pretax employees   tangibles  tangibles_land_and_buildings  \
0                 NaN      None  463.843315                           NaN   
1                 NaN      None         NaN                           NaN   
2                 NaN      None         NaN                           NaN   
3                 NaN      None    0.928000                           NaN   
4                 NaN      None   14.439000                           NaN   

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
0          NaN          NaN                NaN   463.843315  -457.802590   
1          NaN          NaN                NaN          NaN   -92.427688   
2          NaN          NaN                NaN          NaN          NaN   
3          NaN          NaN                NaN     0.928000   -28.172000   
4          NaN       57.697                NaN    72.136000  -121.089000   

   total_assets  liabilites_lt  cos  admin_expenses  interest_paid  \
0   1749.742728   -1208.685068  NaN             NaN            NaN   
1      0.896758            NaN  NaN             NaN            NaN   
2           NaN            NaN  NaN             NaN            NaN   
3     10.428000            NaN  NaN             NaN            NaN   
4    175.906000      -1.324000  NaN             NaN            NaN   

   profit_loss_pretax2  tax  dividends  depreciation  r_and_d  \
0                  NaN  NaN        NaN           NaN      NaN   
1                  NaN  NaN        NaN           NaN      NaN   
2                  NaN  NaN        NaN           NaN      NaN   
3                  NaN  NaN        NaN           NaN      NaN   
4                  NaN  NaN        NaN           NaN      NaN   

   remuneration_employees  wages  social_security_costs  pensions_costs  \
0                     NaN    NaN                    NaN             NaN   
1                     NaN    NaN                    NaN             NaN   
2                     NaN    NaN                    NaN             NaN   
3                     NaN    NaN                    NaN             NaN   
4                     NaN    NaN                    NaN             NaN   

   other_staff_costs  renumeration_directors  ebitda  
0                NaN                     NaN     NaN  
1                NaN                     NaN     NaN  
2                NaN                     NaN     NaN  
3                NaN                     NaN     NaN  
4                NaN                     NaN     NaN  
```

## working_yearly_kp

### Number of rows: 40,846,539

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
0          05132111  2006         False       NaN           12.431737   
1          02372503  2006         False       NaN           -5.620690   
2          04364733  2006         False       NaN           -0.602273   
3          02200237  2006         False       NaN        15079.604543   
4          02605684  2006         False       NaN          -58.811499   

   profit_loss_pretax employees  tangibles  tangibles_land_and_buildings  \
0                 NaN      None        NaN                           NaN   
1                 NaN      None        NaN                           NaN   
2                 NaN      None        NaN                           NaN   
3                 NaN      None        NaN                           NaN   
4                 NaN      None   1.683842                           NaN   

   tangibles_land_freehold  tangibles_land_leasehold  tangibles_fixt_fit  \
0                      NaN                       NaN                 NaN   
1                      NaN                       NaN                 NaN   
2                      NaN                       NaN                 NaN   
3                      NaN                       NaN                 NaN   
4                      NaN                       NaN            1.683842   

   tangibles_plant_and_vehicles  tangibles_plant  tangibles_vehicles  \
0                           NaN              NaN                 NaN   
1                           NaN              NaN                 NaN   
2                           NaN              NaN                 NaN   
3                           NaN              NaN                 NaN   
4                           NaN              NaN                 NaN   

   fixed_other  intangibles  investments_other   fixed_total   liabilities  \
0          NaN          NaN                NaN           NaN     -2.029124   
1          NaN          NaN           0.003153      0.003153     -5.623844   
2          NaN          NaN                NaN           NaN     -0.630653   
3          NaN          NaN       20701.333983  20701.333983 -29344.827012   
4          NaN          NaN                NaN      1.683842    -65.357672   

   total_assets  liabilites_lt  cos  admin_expenses  interest_paid  \
0     14.460862            NaN  NaN             NaN            NaN   
1      0.003153            NaN  NaN             NaN            NaN   
2      0.028379            NaN  NaN             NaN            NaN   
3  44424.431555            NaN  NaN             NaN            NaN   
4      6.546173            NaN  NaN             NaN            NaN   

   profit_loss_pretax2  tax  dividends  depreciation  r_and_d  \
0                  NaN  NaN        NaN           NaN      NaN   
1                  NaN  NaN        NaN           NaN      NaN   
2                  NaN  NaN        NaN           NaN      NaN   
3                  NaN  NaN        NaN           NaN      NaN   
4                  NaN  NaN        NaN           NaN      NaN   

   remuneration_employees  wages  social_security_costs  pensions_costs  \
0                     NaN    NaN                    NaN             NaN   
1                     NaN    NaN                    NaN             NaN   
2                     NaN    NaN                    NaN             NaN   
3                     NaN    NaN                    NaN             NaN   
4                     NaN    NaN                    NaN             NaN   

   other_staff_costs  renumeration_directors  ebitda  
0                NaN                     NaN     NaN  
1                NaN                     NaN     NaN  
2                NaN                     NaN     NaN  
3                NaN                     NaN     NaN  
4                NaN                     NaN     NaN  
```

# Other Tables in DuckDB database

## fame_yearly_consolidated

### Number of rows: 47,456,502

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
0          IE038100  2006         False       NaN           83.255069   
1          IE210547  2006         False       NaN          -91.530930   
2          IE347763  2006         False       NaN                 NaN   
3          04497426  2006         False       NaN          -17.744000   
4          SC192159  2006         False       NaN           53.493000   

   profit_loss_pretax employees   tangibles  tangibles_land_and_buildings  \
0                 NaN      None  463.843315                           NaN   
1                 NaN      None         NaN                           NaN   
2                 NaN      None         NaN                           NaN   
3                 NaN      None    0.928000                           NaN   
4                 NaN      None   14.439000                           NaN   

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
0          NaN          NaN                NaN   463.843315  -457.802590   
1          NaN          NaN                NaN          NaN   -92.427688   
2          NaN          NaN                NaN          NaN          NaN   
3          NaN          NaN                NaN     0.928000   -28.172000   
4          NaN       57.697                NaN    72.136000  -121.089000   

   total_assets  liabilites_lt  cos  admin_expenses  interest_paid  \
0   1749.742728   -1208.685068  NaN             NaN            NaN   
1      0.896758            NaN  NaN             NaN            NaN   
2           NaN            NaN  NaN             NaN            NaN   
3     10.428000            NaN  NaN             NaN            NaN   
4    175.906000      -1.324000  NaN             NaN            NaN   

   profit_loss_pretax2  tax  dividends  depreciation  r_and_d  \
0                  NaN  NaN        NaN           NaN      NaN   
1                  NaN  NaN        NaN           NaN      NaN   
2                  NaN  NaN        NaN           NaN      NaN   
3                  NaN  NaN        NaN           NaN      NaN   
4                  NaN  NaN        NaN           NaN      NaN   

   remuneration_employees  wages  social_security_costs  pensions_costs  \
0                     NaN    NaN                    NaN             NaN   
1                     NaN    NaN                    NaN             NaN   
2                     NaN    NaN                    NaN             NaN   
3                     NaN    NaN                    NaN             NaN   
4                     NaN    NaN                    NaN             NaN   

   other_staff_costs  renumeration_directors  ebitda  
0                NaN                     NaN     NaN  
1                NaN                     NaN     NaN  
2                NaN                     NaN     NaN  
3                NaN                     NaN     NaN  
4                NaN                     NaN     NaN  
```

## working_yearly_kp

### Number of rows: 40,846,539

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
0          05132111  2006         False       NaN           12.431737   
1          02372503  2006         False       NaN           -5.620690   
2          04364733  2006         False       NaN           -0.602273   
3          02200237  2006         False       NaN        15079.604543   
4          02605684  2006         False       NaN          -58.811499   

   profit_loss_pretax employees  tangibles  tangibles_land_and_buildings  \
0                 NaN      None        NaN                           NaN   
1                 NaN      None        NaN                           NaN   
2                 NaN      None        NaN                           NaN   
3                 NaN      None        NaN                           NaN   
4                 NaN      None   1.683842                           NaN   

   tangibles_land_freehold  tangibles_land_leasehold  tangibles_fixt_fit  \
0                      NaN                       NaN                 NaN   
1                      NaN                       NaN                 NaN   
2                      NaN                       NaN                 NaN   
3                      NaN                       NaN                 NaN   
4                      NaN                       NaN            1.683842   

   tangibles_plant_and_vehicles  tangibles_plant  tangibles_vehicles  \
0                           NaN              NaN                 NaN   
1                           NaN              NaN                 NaN   
2                           NaN              NaN                 NaN   
3                           NaN              NaN                 NaN   
4                           NaN              NaN                 NaN   

   fixed_other  intangibles  investments_other   fixed_total   liabilities  \
0          NaN          NaN                NaN           NaN     -2.029124   
1          NaN          NaN           0.003153      0.003153     -5.623844   
2          NaN          NaN                NaN           NaN     -0.630653   
3          NaN          NaN       20701.333983  20701.333983 -29344.827012   
4          NaN          NaN                NaN      1.683842    -65.357672   

   total_assets  liabilites_lt  cos  admin_expenses  interest_paid  \
0     14.460862            NaN  NaN             NaN            NaN   
1      0.003153            NaN  NaN             NaN            NaN   
2      0.028379            NaN  NaN             NaN            NaN   
3  44424.431555            NaN  NaN             NaN            NaN   
4      6.546173            NaN  NaN             NaN            NaN   

   profit_loss_pretax2  tax  dividends  depreciation  r_and_d  \
0                  NaN  NaN        NaN           NaN      NaN   
1                  NaN  NaN        NaN           NaN      NaN   
2                  NaN  NaN        NaN           NaN      NaN   
3                  NaN  NaN        NaN           NaN      NaN   
4                  NaN  NaN        NaN           NaN      NaN   

   remuneration_employees  wages  social_security_costs  pensions_costs  \
0                     NaN    NaN                    NaN             NaN   
1                     NaN    NaN                    NaN             NaN   
2                     NaN    NaN                    NaN             NaN   
3                     NaN    NaN                    NaN             NaN   
4                     NaN    NaN                    NaN             NaN   

   other_staff_costs  renumeration_directors  ebitda  
0                NaN                     NaN     NaN  
1                NaN                     NaN     NaN  
2                NaN                     NaN     NaN  
3                NaN                     NaN     NaN  
4                NaN                     NaN     NaN  
```

