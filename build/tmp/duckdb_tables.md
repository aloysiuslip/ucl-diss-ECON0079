# Tables in DuckDB database

## fame_derived

### Number of rows: 40072

### Schema:

```
ibis.Schema {
  registered_number      string
  has_ptaddress          boolean
  has_ptaddress_latlong  boolean
  is_public              boolean
  industry_code          string
  file_code              string
}
```

### Head of table:

```
  registered_number  has_ptaddress  has_ptaddress_latlong  is_public  \
0          13380867           True                  False      False   
1          13380876          False                  False      False   
2          13380905           True                  False      False   
3          13380928           True                  False      False   
4          13380933           True                  False      False   

  industry_code                                          file_code  
0            56  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...  
1            56  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...  
2            56  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...  
3            56  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...  
4            56  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...  
```

## fame_fixed

### Number of rows: 40072

### Schema:

```
ibis.Schema {
  company_name                     string
  registered_number                string
  primary_uk_sic_2007_code         string
  primary_uk_sic_2007_description  string
  latest_accounts_date             date
  no_of_available_years            int32
}
```

### Head of table:

```
                          company_name registered_number  \
0                     TBZ HOUNSLOW LTD          13380867   
1  THE OLD BAKEHOUSE AT RUDDINGTON LTD          13380876   
2                         SK GRILL LTD          13380905   
3                          KUCAKLI LTD          13380928   
4                      YUMILICIOUS LTD          13380933   

  primary_uk_sic_2007_code              primary_uk_sic_2007_description  \
0                  56210.0                    Event catering activities   
1                  56102.0             Unlicensed restaurants and cafes   
2                  56103.0  Take away food shops and mobile food stands   
3                  56102.0             Unlicensed restaurants and cafes   
4                  56103.0  Take away food shops and mobile food stands   

  latest_accounts_date  no_of_available_years  
0           2023-05-31                      2  
1           2023-05-31                      2  
2           2024-05-31                      3  
3           2022-04-30                      1  
4           2023-10-31                      2  
```

## ibis_pandas_memtable_6zo2zsvhvjgmxmkf2nko25vuga

### Number of rows: 10981

### Schema:

```
ibis.Schema {
  is_public              boolean
  file_code              string
  has_ptaddress          boolean
  registered_number      int64
  has_ptaddress_latlong  boolean
  industry_code          string
}
```

### Head of table:

```
   is_public                                          file_code  \
0      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
1      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
2      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
3      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
4      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   

   has_ptaddress  registered_number  has_ptaddress_latlong industry_code  
0           True           13380867                  False            56  
1          False           13380876                  False            56  
2           True           13380905                  False            56  
3           True           13380928                  False            56  
4           True           13380933                  False            56  
```

## ibis_pandas_memtable_73y32keenbfylg65ulds2rhiam

### Number of rows: 16384

### Schema:

```
ibis.Schema {
  is_public              boolean
  file_code              string
  has_ptaddress          boolean
  registered_number      int64
  has_ptaddress_latlong  boolean
  industry_code          string
}
```

### Head of table:

```
   is_public                                          file_code  \
0      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
1      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
2      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
3      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
4      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   

   has_ptaddress  registered_number  has_ptaddress_latlong industry_code  
0           True            7983195                  False            56  
1          False            7983211                  False            56  
2          False            7983240                  False            56  
3           True            7983250                   True            56  
4           True            7983251                   True            56  
```

## ibis_pandas_memtable_7ep763uynzfotlzsekomek7o44

### Number of rows: 12540

### Schema:

```
ibis.Schema {
  is_public              boolean
  file_code              string
  has_ptaddress          boolean
  registered_number      int64
  has_ptaddress_latlong  boolean
  industry_code          string
}
```

### Head of table:

```
   is_public                                          file_code  \
0      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
1      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
2      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
3      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
4      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   

   has_ptaddress  registered_number  has_ptaddress_latlong industry_code  
0           True           12044476                   True            56  
1           True           12044527                   True            56  
2          False           12044529                  False            56  
3           True           12044548                   True            56  
4           True           12044573                   True            56  
```

## ibis_pandas_memtable_7gmu7dtuhbhblkryruzscve4vu

### Number of rows: 167

### Schema:

```
ibis.Schema {
  company_name                     string
  registered_number                int64
  primary_uk_sic_2007_code         float64
  primary_uk_sic_2007_description  string
  latest_accounts_date             date
  no_of_available_years            int64
}
```

### Head of table:

```
                  company_name  registered_number  primary_uk_sic_2007_code  \
0                RIANOS UK LTD           15356891                   56103.0   
1       VICTORIA ASTON LIMITED           15357275                   56103.0   
2              MEDLUXEFOOD LTD           15359314                   47240.0   
3           CAL9LATION TEA LTD           15360668                   56103.0   
4  FIREHOUSE PERI PERI LIMITED           15361179                   56103.0   

                     primary_uk_sic_2007_description latest_accounts_date  \
0        Take away food shops and mobile food stands           2024-12-31   
1        Take away food shops and mobile food stands           2024-03-31   
2  Retail sale of bread, cakes, flour confectione...           2024-12-31   
3        Take away food shops and mobile food stands           2024-12-31   
4        Take away food shops and mobile food stands           2024-03-31   

   no_of_available_years  
0                      1  
1                      1  
2                      1  
3                      1  
4                      1  
```

## ibis_pandas_memtable_gn4sbzjfevefxbzjcmhuyekl3a

### Number of rows: 16384

### Schema:

```
ibis.Schema {
  company_name                     string
  registered_number                int64
  primary_uk_sic_2007_code         float64
  primary_uk_sic_2007_description  string
  latest_accounts_date             date
  no_of_available_years            int64
}
```

### Head of table:

```
                   company_name  registered_number  primary_uk_sic_2007_code  \
0  MARCANTONIO CATERING LIMITED            7983195                   56101.0   
1       JKC HOSPITALITY LIMITED            7983211                   56302.0   
2         MIMI'S BISTRO LIMITED            7983240                   56102.0   
3       BAWARCHI RESTAURANT LTD            7983250                   56101.0   
4          READING INNS LIMITED            7983251                   56302.0   

    primary_uk_sic_2007_description latest_accounts_date  \
0              Licensed restaurants           2023-03-31   
1            Public houses and bars           2017-03-31   
2  Unlicensed restaurants and cafes           2014-04-30   
3              Licensed restaurants           2021-03-31   
4            Public houses and bars           2015-03-31   

   no_of_available_years  
0                     11  
1                      5  
2                      2  
3                      9  
4                      3  
```

## ibis_pandas_memtable_j6m7f57yqzdt5ddw4jiu5dvxp4

### Number of rows: 167

### Schema:

```
ibis.Schema {
  is_public              boolean
  file_code              string
  has_ptaddress          boolean
  registered_number      int64
  has_ptaddress_latlong  boolean
  industry_code          string
}
```

### Head of table:

```
   is_public                                          file_code  \
0      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
1      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
2      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
3      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   
4      False  LN dataset\Dropbox\fame_clean\1_FAME_raw_data\...   

   has_ptaddress  registered_number  has_ptaddress_latlong industry_code  
0          False           15356891                  False            56  
1          False           15357275                  False            56  
2          False           15359314                  False            56  
3          False           15360668                  False            56  
4          False           15361179                  False            56  
```

## ibis_pandas_memtable_kfe4mgraqbcufjreximfoxyzhq

### Number of rows: 12540

### Schema:

```
ibis.Schema {
  company_name                     string
  registered_number                int64
  primary_uk_sic_2007_code         float64
  primary_uk_sic_2007_description  string
  latest_accounts_date             date
  no_of_available_years            int64
}
```

### Head of table:

```
                 company_name  registered_number  primary_uk_sic_2007_code  \
0            SORAZTRA BAR LTD           12044476                   56101.0   
1    KRUSHA'S DELIGHT LIMITED           12044527                   56101.0   
2        CONNECT FAST LIMITED           12044529                   46450.0   
3  ANIKAS INDIAN TAKEAWAY LTD           12044548                   56103.0   
4   REDDISH EXPRESS PIZZA LTD           12044573                   56103.0   

               primary_uk_sic_2007_description latest_accounts_date  \
0                         Licensed restaurants           2023-06-30   
1                         Licensed restaurants           2020-06-30   
2           Wholesale of perfume and cosmetics           2020-06-30   
3  Take away food shops and mobile food stands           2022-03-31   
4  Take away food shops and mobile food stands           2022-06-30   

   no_of_available_years  
0                      4  
1                      1  
2                      1  
3                      3  
4                      3  
```

## ibis_pandas_memtable_m3wyyldqyzfmpixq4ybfy5hzuy

### Number of rows: 0

### Schema:

```
ibis.Schema {
  is_public              boolean
  file_code              string
  has_ptaddress          boolean
  registered_number      float64
  has_ptaddress_latlong  boolean
  industry_code          string
}
```

### Head of table:

```
Empty DataFrame
Columns: [is_public, file_code, has_ptaddress, registered_number, has_ptaddress_latlong, industry_code]
Index: []
```

## ibis_pandas_memtable_nlqkrcuevragzks3mang2bfwca

### Number of rows: 10981

### Schema:

```
ibis.Schema {
  company_name                     string
  registered_number                int64
  primary_uk_sic_2007_code         float64
  primary_uk_sic_2007_description  string
  latest_accounts_date             date
  no_of_available_years            int64
}
```

### Head of table:

```
                          company_name  registered_number  \
0                     TBZ HOUNSLOW LTD           13380867   
1  THE OLD BAKEHOUSE AT RUDDINGTON LTD           13380876   
2                         SK GRILL LTD           13380905   
3                          KUCAKLI LTD           13380928   
4                      YUMILICIOUS LTD           13380933   

   primary_uk_sic_2007_code              primary_uk_sic_2007_description  \
0                   56210.0                    Event catering activities   
1                   56102.0             Unlicensed restaurants and cafes   
2                   56103.0  Take away food shops and mobile food stands   
3                   56102.0             Unlicensed restaurants and cafes   
4                   56103.0  Take away food shops and mobile food stands   

  latest_accounts_date  no_of_available_years  
0           2023-05-31                      2  
1           2023-05-31                      2  
2           2024-05-31                      3  
3           2022-04-30                      1  
4           2023-10-31                      2  
```

## ibis_pandas_memtable_r5nkeeehorcbxndat5kh6owvjq

### Number of rows: 0

### Schema:

```
ibis.Schema {
  company_name                     string
  registered_number                float64
  primary_uk_sic_2007_code         int64
  primary_uk_sic_2007_description  string
  latest_accounts_date             int64
  no_of_available_years            int64
}
```

### Head of table:

```
Empty DataFrame
Columns: [company_name, registered_number, primary_uk_sic_2007_code, primary_uk_sic_2007_description, latest_accounts_date, no_of_available_years]
Index: []
```

