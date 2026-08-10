# Tables in DuckDB database

## fame_derived

### Number of rows: 49378

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
0          07377942          False                  False      False   
1          07406279           True                   True      False   
2          07427051          False                  False      False   
3          07428085          False                  False      False   
4          07442873           True                  False      False   

  has_company_branch_mismatch industry_codes file_codes  
0                        None             01      12_33  
1                       False             01      12_33  
2                        None             01      12_33  
3                        None             01      12_33  
4                       False             01      12_33  
```

## fame_fixed

### Number of rows: 49886

### Schema:

```
ibis.Schema {
  company_name                       string
  registered_number                  string
  ticker_symbol                      string
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
}
```

### Head of table:

```
                     company_name registered_number ticker_symbol  \
0                    MANDANNA LTD          07373721           NaN   
1        STONEY ACRE FARM LIMITED          07374017           NaN   
2     ROSEDALE RESERVOIR FARM LTD          07374029           NaN   
3   SIMPATICO ENGINEERING LIMITED          07374199           NaN   
4  RIDGE FARM ENTERPRISES LIMITED          07374750           NaN   

                             primary_trading_address  \
0  Highfield Farm, Greetham, Horncastle, Lincolns...   
1                                                NaN   
2  40 Manor Road, Scarborough, North Yorkshire, Y...   
3  The Old Carriage Works, Moresk Road, Truro, Co...   
4                                                NaN   

  primary_trading_address_latitude primary_trading_address_longitude  \
0                              NaN                               NaN   
1                              NaN                               NaN   
2                   54° 17' 3.5" N                     0° 25' 4.7" W   
3                  50° 16' 10.0" N                     5° 2' 58.0" W   
4                              NaN                               NaN   

                     branch_name  primary_uk_sic_2007_code  \
0                   MANDANNA LTD                    1629.0   
1                            NaN                   77310.0   
2    ROSEDALE RESERVOIR FARM LTD                    1450.0   
3  SIMPATICO ENGINEERING LIMITED                    1190.0   
4                            NaN                    1410.0   

                     primary_uk_sic_2007_description latest_accounts_date  \
0  Support activities for animal production (othe...           2014-09-30   
1  Renting and leasing of agricultural machinery ...           2023-09-30   
2                         Raising of sheep and goats           2019-09-30   
3               Growing of other non-perennial crops           2022-09-30   
4                            Raising of dairy cattle           2015-03-31   

   no_of_available_years  guo  guo_nb      entity_type  
0                      4  NaN     0.0  Single location  
1                     13  NaN     0.0   Independent co  
2                      9  NaN     0.0  Single location  
3                     12  NaN     0.0  Single location  
4                      5  NaN     0.0  Single location  
```

## fame_yearly

### Number of rows: 0

### Schema:

```
ibis.Schema {
  registered_number  string
  fame_key           string
  year               int64
  value              float64
}
```

### Head of table:

```
Empty DataFrame
Columns: [registered_number, fame_key, year, value]
Index: []
```

## ibis_pandas_memtable_ahysal4e3vdgrhyfty7t3e2h4u

### Number of rows: 62400

### Schema:

```
ibis.Schema {
  registered_number            string
  credit_score                 int64
  credit_score_date            timestamp(6)
  credit_score_indicator       string
  credit_score_prev            int64
  credit_score_indicator_prev  string
  guo_nb                       float64
  entity_type                  string
  guo                          string
  industry_codes               string
  file_codes                   string
}
```

### Head of table:

```
  registered_number  credit_score credit_score_date credit_score_indicator  \
0          IE501098          89.0        2024-10-21                 Secure   
1          NI000166          99.0        2024-05-01                 Secure   
2          05288567          95.0        2025-01-23                 Secure   
3          05969169          77.0        2024-05-14                 Stable   
4          03548572          86.0        2024-03-20                 Secure   

   credit_score_prev credit_score_indicator_prev  guo_nb       entity_type  \
0               92.0                      Secure   109.0  Controlled subs.   
1               99.0                      Secure    62.0  Controlled subs.   
2               95.0                      Secure    20.0               GUO   
3               77.0                      Stable     0.0    Independent co   
4               77.0                      Stable     7.0  Controlled subs.   

                                guo industry_codes file_codes  
0  GLANBIA CO-OPERATIVE SOCIETY LTD             01      16_51  
1      W&R BARNETT HOLDINGS LIMITED             01      16_51  
2      FRONTIER AGRICULTURE LIMITED             01      16_51  
3                               NaN             01      16_51  
4           OPENFIELD GROUP LIMITED             01      16_51  
```

## ibis_pandas_memtable_mvw3czicwjgnzfre45asypbs3a

### Number of rows: 10778

### Schema:

```
ibis.Schema {
  registered_number            string
  credit_score                 int64
  credit_score_date            timestamp(6)
  credit_score_indicator       string
  credit_score_prev            int64
  credit_score_indicator_prev  string
  guo_nb                       int64
  entity_type                  string
  guo                          string
  industry_codes               string
  file_codes                   string
}
```

### Head of table:

```
  registered_number  credit_score credit_score_date credit_score_indicator  \
0          IE138108          92.0        2024-11-07                 Secure   
1          IE226361          99.0        2024-12-09                 Secure   
2          IE101979          99.0        2024-11-11                 Secure   
3          03242286          99.0        2024-10-15                 Secure   
4          13068460          95.0        2024-10-04                 Secure   

   credit_score_prev credit_score_indicator_prev  guo_nb       entity_type  \
0               95.0                      Secure     670  Controlled subs.   
1               99.0                      Secure      13               GUO   
2               99.0                      Secure      20               GUO   
3               92.0                      Secure      67  Controlled subs.   
4               88.0                      Secure      52  Controlled subs.   

                                  guo industry_codes file_codes  
0               GOVERNMENT OF IRELAND             02      18_43  
1      GLENNON BROS. HOLDINGS LIMITED             02      18_43  
2       SUPERMAC'S (HOLDINGS) LIMITED             02      18_43  
3  BINDER BETEILIGUNGSVERWALTUNG GMBH             02      18_43  
4  O.F. AHLMARK & CO EFTR. AKTIEBOLAG             02      18_43  
```

## ibis_pandas_memtable_o3yu6cdsmzhefjm7dxuilstcsq

### Number of rows: 42142

### Schema:

```
ibis.Schema {
  company_name                             string
  registered_number                        string
  ticker_symbol                            string
  ro_address                               string
  ro_address_line_1                        string
  ro_address_line_2                        string
  ro_address_line_3                        string
  ro_address_line_4                        string
  ro_address_line_5                        string
  ro_city                                  string
  ro_county                                string
  ro_postcode                              string
  ro_full_postcode                         string
  ro_country                               string
  ro_latitude                              string
  ro_longitude                             string
  ro_nuts_region                           string
  ro_postal_region                         string
  ro_phone                                 string
  ro_phone_registered_on_tps               string
  ro_phone_registered_on_ctps              string
  primary_trading_address                  string
  primary_trading_address_latitude         string
  primary_trading_address_longitude        string
  primary_trading_address_no_of_employees  int64
  branch_name                              string
  trade_description                        string
  primary_uk_sic_2007_code                 float64
  primary_uk_sic_2007_description          string
  full_overview                            string
  history                                  string
  primary_business_line                    string
  secondary_business_line                  string
  main_activity                            string
  secondary_activity                       string
  main_products_and_services               string
  size_estimate                            string
  strategy_organization_and_policy         string
  strategic_alliances                      string
  membership_of_a_network                  string
  main_brand_names                         string
  main_domestic_country                    string
  main_foreign_countries_or_regions        string
  main_production_sites                    string
  main_distribution_sites                  string
  main_sales_representation_sites          string
  main_customers                           string
  latest_accounts_date                     timestamp(6)
  no_of_available_years                    int64
  industry_codes                           string
  file_codes                               string
}
```

### Head of table:

```
                     company_name registered_number ticker_symbol  \
0                    MANDANNA LTD          07373721           NaN   
1        STONEY ACRE FARM LIMITED          07374017           NaN   
2     ROSEDALE RESERVOIR FARM LTD          07374029           NaN   
3   SIMPATICO ENGINEERING LIMITED          07374199           NaN   
4  RIDGE FARM ENTERPRISES LIMITED          07374750           NaN   

                                          ro_address       ro_address_line_1  \
0  Highfield Farm, Greetham, Horncastle, Lincolns...          Highfield Farm   
1  17 Victoria Road East, Thornton-Cleveleys, Lan...   17 Victoria Road East   
2  40 Manor Road, Scarborough, North Yorkshire, Y...           40 Manor Road   
3  The Old Carriage Works, Moresk Road, Truro, Co...  The Old Carriage Works   
4  25 St Thomas Street, Winchester, Hampshire, SO...     25 St Thomas Street   

  ro_address_line_2 ro_address_line_3 ro_address_line_4 ro_address_line_5  \
0          Greetham               NaN               NaN               NaN   
1               NaN               NaN               NaN               NaN   
2               NaN               NaN               NaN               NaN   
3       Moresk Road               NaN               NaN               NaN   
4               NaN               NaN               NaN               NaN   

              ro_city  ... main_domestic_country  \
0          Horncastle  ...                   NaN   
1  Thornton-Cleveleys  ...                   NaN   
2         Scarborough  ...                   NaN   
3               Truro  ...                   NaN   
4          Winchester  ...                   NaN   

  main_foreign_countries_or_regions main_production_sites  \
0                               NaN                   NaN   
1                               NaN                   NaN   
2                               NaN                   NaN   
3                               NaN                   NaN   
4                               NaN                   NaN   

  main_distribution_sites main_sales_representation_sites main_customers  \
0                     NaN                             NaN            NaN   
1                     NaN                             NaN            NaN   
2                     NaN                             NaN            NaN   
3                     NaN                             NaN            NaN   
4                     NaN                             NaN            NaN   

  latest_accounts_date no_of_available_years industry_codes file_codes  
0           2014-09-30                     4             01      12_33  
1           2023-09-30                    13             01      12_33  
2           2019-09-30                     9             01      12_33  
3           2022-09-30                    12             01      12_33  
4           2015-03-31                     5             01      12_33  

[5 rows x 51 columns]
```

## ibis_pandas_memtable_uehvzqsxancfzduim7utu6hxxm

### Number of rows: 7744

### Schema:

```
ibis.Schema {
  company_name                             string
  registered_number                        string
  ticker_symbol                            string
  ro_address                               string
  ro_address_line_1                        string
  ro_address_line_2                        string
  ro_address_line_3                        string
  ro_address_line_4                        string
  ro_address_line_5                        string
  ro_city                                  string
  ro_county                                string
  ro_postcode                              string
  ro_full_postcode                         string
  ro_country                               string
  ro_latitude                              string
  ro_longitude                             string
  ro_nuts_region                           string
  ro_postal_region                         string
  ro_phone                                 string
  ro_phone_registered_on_tps               string
  ro_phone_registered_on_ctps              string
  primary_trading_address                  string
  primary_trading_address_latitude         string
  primary_trading_address_longitude        string
  primary_trading_address_no_of_employees  int64
  branch_name                              string
  trade_description                        string
  primary_uk_sic_2007_code                 float64
  primary_uk_sic_2007_description          string
  full_overview                            string
  history                                  string
  primary_business_line                    string
  secondary_business_line                  string
  main_activity                            string
  secondary_activity                       float64
  main_products_and_services               string
  size_estimate                            string
  strategy_organization_and_policy         string
  strategic_alliances                      string
  membership_of_a_network                  string
  main_brand_names                         string
  main_domestic_country                    string
  main_foreign_countries_or_regions        string
  main_production_sites                    string
  main_distribution_sites                  string
  main_sales_representation_sites          string
  main_customers                           string
  latest_accounts_date                     timestamp(6)
  no_of_available_years                    int64
  industry_codes                           string
  file_codes                               string
}
```

### Head of table:

```
                  company_name registered_number ticker_symbol  \
0     TILHILL FORESTRY LIMITED          03242286           NaN   
1  EUROFOREST HOLDINGS LIMITED          13068460           NaN   
2   SCOTTISH WOODLANDS LIMITED          SC101787           NaN   
3                  SWL LIMITED          SC274096           NaN   
4           EUROFOREST LIMITED          01153003           NaN   

                                          ro_address  \
0  3rd Floor 1 Ashley Road, Altrincham, Cheshire,...   
1  Karlstad House, 3 Merchants Drive, Carlisle, C...   
2  2 Roddinglaw Court, Roddinglaw Business Park, ...   
3  Research Park, Riccarton, Edinburgh, Currie, M...   
4  Karlstad House, 3 Merchants Drive, Carlisle, C...   

          ro_address_line_1         ro_address_line_2 ro_address_line_3  \
0   3rd Floor 1 Ashley Road                       NaN               NaN   
1            Karlstad House         3 Merchants Drive               NaN   
2        2 Roddinglaw Court  Roddinglaw Business Park   Roddinglaw Road   
3  Research Park, Riccarton                 Edinburgh               NaN   
4            Karlstad House         3 Merchants Drive               NaN   

  ro_address_line_4 ro_address_line_5     ro_city  ... main_domestic_country  \
0               NaN               NaN  Altrincham  ...        United Kingdom   
1               NaN               NaN    Carlisle  ...        United Kingdom   
2               NaN               NaN   Edinburgh  ...        United Kingdom   
3               NaN               NaN      Currie  ...        United Kingdom   
4               NaN               NaN    Carlisle  ...        United Kingdom   

  main_foreign_countries_or_regions main_production_sites  \
0                               NaN                   NaN   
1                               NaN                   NaN   
2                               NaN                   NaN   
3                               NaN                   NaN   
4                               NaN                   NaN   

  main_distribution_sites main_sales_representation_sites main_customers  \
0                     NaN                             NaN            NaN   
1                     NaN                             NaN            NaN   
2                     NaN                             NaN            NaN   
3                     NaN                             NaN            NaN   
4                     NaN                             NaN            NaN   

  latest_accounts_date no_of_available_years industry_codes file_codes  
0           2023-12-31                    20             02      12_39  
1           2023-12-30                     4             02      12_39  
2           2023-09-30                    20             02      12_39  
3           2023-09-30                    19             02      12_39  
4           2023-12-30                    20             02      12_39  

[5 rows x 51 columns]
```

