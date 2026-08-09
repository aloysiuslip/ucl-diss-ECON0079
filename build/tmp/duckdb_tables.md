# Tables in DuckDB database

## fame_derived

### Number of rows: 0

### Schema:

```
ibis.Schema {
  registered_number            string
  has_ptaddress                boolean
  has_ptaddress_latlong        boolean
  is_public                    boolean
  has_company_branch_mismatch  boolean
  industry_code                string
  file_code                    string
}
```

### Head of table:

```
Empty DataFrame
Columns: [registered_number, has_ptaddress, has_ptaddress_latlong, is_public, has_company_branch_mismatch, industry_code, file_code]
Index: []
```

## fame_fixed

### Number of rows: 0

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
Empty DataFrame
Columns: [company_name, registered_number, ticker_symbol, primary_trading_address, primary_trading_address_latitude, primary_trading_address_longitude, branch_name, primary_uk_sic_2007_code, primary_uk_sic_2007_description, latest_accounts_date, no_of_available_years, guo, guo_nb, entity_type]
Index: []
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

