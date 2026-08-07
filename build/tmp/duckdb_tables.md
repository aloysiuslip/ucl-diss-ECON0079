# Tables in DuckDB database

## fame_derived

### Number of rows: 95512

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
  registered_number  has_ptaddress  has_ptaddress_latlong  is_public  \
0          IE007481          False                  False      False   
1          IE008860          False                  False      False   
2          IE012253          False                  False      False   
3          IE013519          False                  False      False   
4          IE014257          False                  False      False   

  has_company_branch_mismatch industry_code file_code  
0                       False            93     17_15  
1                       False            93     17_15  
2                       False            93     17_15  
3                       False            93     17_15  
4                       False            93     17_15  
```

## fame_fixed

### Number of rows: 95512

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
}
```

### Head of table:

```
                              company_name registered_number ticker_symbol  \
0  G. W. BIGGS & COMPANY UNLIMITED COMPANY          IE007481           NaN   
1     D.F. DOYLE PROPERTIES (CORK) LIMITED          IE008860           NaN   
2      SULLIVANS FUNERAL DIRECTORS LIMITED          IE012253           NaN   
3                LAURENCE C. GUNNE LIMITED          IE013519           NaN   
4                A.R. O'HARE & CO. LIMITED          IE014257           NaN   

  primary_trading_address primary_trading_address_latitude  \
0                     NaN                              NaN   
1                     NaN                              NaN   
2                     NaN                              NaN   
3                     NaN                              NaN   
4                     NaN                              NaN   

  primary_trading_address_longitude                              branch_name  \
0                               NaN  G. W. BIGGS & COMPANY UNLIMITED COMPANY   
1                               NaN     D.F. DOYLE PROPERTIES (CORK) LIMITED   
2                               NaN      SULLIVANS FUNERAL DIRECTORS LIMITED   
3                               NaN                LAURENCE C. GUNNE LIMITED   
4                               NaN                A.R. O'HARE & CO. LIMITED   

   primary_uk_sic_2007_code  \
0                   49410.0   
1                   49410.0   
2                   47300.0   
3                   46180.0   
4                   66190.0   

                     primary_uk_sic_2007_description latest_accounts_date  \
0                          Freight transport by road           2017-12-31   
1                          Freight transport by road           2023-12-31   
2  Retail sale of automotive fuel in specialised ...           2024-02-29   
3  Agents specialised in the sale of other partic...           2024-03-31   
4  Other activities auxiliary to financial servic...           2023-09-30   

   no_of_available_years  
0                     11  
1                     20  
2                     20  
3                     20  
4                     20  
```

## ibis_pandas_memtable_b5hirqaowrcqza3ckhezakcr4m

### Number of rows: 10843

### Schema:

```
ibis.Schema {
  primary_trading_address_longitude  float64
  primary_uk_sic_2007_code           float64
  latest_accounts_date               date
  no_of_available_years              int64
  registered_number                  int64
  company_name                       string
  branch_name                        string
  ticker_symbol                      float64
  primary_trading_address_latitude   float64
  primary_uk_sic_2007_description    string
  primary_trading_address            int32
}
```

### Head of table:

```
   primary_trading_address_longitude  primary_uk_sic_2007_code  \
0                                NaN                   49410.0   
1                                NaN                   49320.0   
2                                NaN                   49410.0   
3                                NaN                   49410.0   
4                                NaN                   49410.0   

  latest_accounts_date  no_of_available_years  registered_number  \
0           2024-01-31                      4           12461081   
1           2024-02-29                      4           12461152   
2           2022-02-28                      2           12461270   
3           2023-03-31                      3           12461352   
4           2022-02-28                      2           12461482   

                 company_name                 branch_name  ticker_symbol  \
0       CLARIGO LOGISTICS LTD       CLARIGO LOGISTICS LTD            NaN   
1              RIDESHARKS LTD              RIDESHARKS LTD            NaN   
2   ANDREEA & CATALIN LIMITED   ANDREEA & CATALIN LIMITED            NaN   
3  A2C TRANSPORT SERVICES LTD  A2C TRANSPORT SERVICES LTD            NaN   
4          CHITZ COURIERS LTD          CHITZ COURIERS LTD            NaN   

   primary_trading_address_latitude primary_uk_sic_2007_description  \
0                               NaN       Freight transport by road   
1                               NaN                  Taxi operation   
2                               NaN       Freight transport by road   
3                               NaN       Freight transport by road   
4                               NaN       Freight transport by road   

  primary_trading_address  
0                    None  
1                    None  
2                    None  
3                    None  
4                    None  
```

## ibis_pandas_memtable_clwcnckrdvcljf2wp4c647qevi

### Number of rows: 12151

### Schema:

```
ibis.Schema {
  primary_trading_address_longitude  string
  primary_uk_sic_2007_code           int64
  latest_accounts_date               date
  no_of_available_years              int64
  registered_number                  int64
  company_name                       string
  branch_name                        string
  ticker_symbol                      float64
  primary_trading_address_latitude   string
  primary_uk_sic_2007_description    string
  primary_trading_address            int32
}
```

### Head of table:

```
  primary_trading_address_longitude  primary_uk_sic_2007_code  \
0                               NaN                     49410   
1                     1° 33' 7.9" W                     49410   
2                    1° 32' 25.3" W                     49410   
3                               NaN                     49410   
4                               NaN                     49320   

  latest_accounts_date  no_of_available_years  registered_number  \
0           2024-01-31                      6           11164351   
1           2023-01-31                      5           11164375   
2           2024-01-31                      6           11164411   
3           2019-08-31                      2           11164456   
4           2024-01-31                      6           11164483   

             company_name             branch_name  ticker_symbol  \
0           PERERA NN LTD           PERERA NN LTD            NaN   
1      KK&L TRANSPORT LTD      KK&L TRANSPORT LTD            NaN   
2          007 RACING LTD          007 RACING LTD            NaN   
3       MJP TRANS LIMITED       MJP TRANS LIMITED            NaN   
4  ALPHA CARS CRAWLEY LTD  ALPHA CARS CRAWLEY LTD            NaN   

  primary_trading_address_latitude primary_uk_sic_2007_description  \
0                              NaN       Freight transport by road   
1                  53° 46' 43.0" N       Freight transport by road   
2                  54° 54' 57.2" N       Freight transport by road   
3                              NaN       Freight transport by road   
4                              NaN                  Taxi operation   

  primary_trading_address  
0                    None  
1                    None  
2                    None  
3                    None  
4                    None  
```

## ibis_pandas_memtable_dtexg34gwrf6deyvqasdf2kx2a

### Number of rows: 4815

### Schema:

```
ibis.Schema {
  primary_trading_address_longitude  float64
  primary_uk_sic_2007_code           float64
  latest_accounts_date               date
  no_of_available_years              int64
  registered_number                  float64
  company_name                       string
  branch_name                        string
  ticker_symbol                      float64
  primary_trading_address_latitude   float64
  primary_uk_sic_2007_description    string
  primary_trading_address            string
}
```

### Head of table:

```
   primary_trading_address_longitude  primary_uk_sic_2007_code  \
0                                NaN                   84250.0   
1                                NaN                   84120.0   
2                                NaN                   84250.0   
3                                NaN                   84120.0   
4                                NaN                   84120.0   

  latest_accounts_date  no_of_available_years  registered_number  \
0           2021-09-30                      1         12891534.0   
1           2023-09-30                      3         12892141.0   
2           2023-04-05                      3         12892417.0   
3           2022-09-30                      2         12892547.0   
4           2023-09-30                      3         12893374.0   

                      company_name                      branch_name  \
0                   E CENG LIMITED                              NaN   
1  ANCHORS HEALTHCARE SERVICES LTD  ANCHORS HEALTHCARE SERVICES LTD   
2      TG FIRE CONSULTANTS LIMITED                              NaN   
3           CAREBRIDGE CHC LIMITED           CAREBRIDGE CHC LIMITED   
4      FIRST FOR MENTAL HEALTH LTD      FIRST FOR MENTAL HEALTH LTD   

   ticker_symbol  primary_trading_address_latitude  \
0            NaN                               NaN   
1            NaN                               NaN   
2            NaN                               NaN   
3            NaN                               NaN   
4            NaN                               NaN   

                     primary_uk_sic_2007_description  \
0                            Fire service activities   
1  Regulation of the activities of providing heal...   
2                            Fire service activities   
3  Regulation of the activities of providing heal...   
4  Regulation of the activities of providing heal...   

                             primary_trading_address  
0                                                NaN  
1        124-128 City Road, London, London, EC1V 2NX  
2                                                NaN  
3  7 The Old Yard, Rectory Lane, Brasted, Westerh...  
4                                                NaN  
```

## ibis_pandas_memtable_kpnhhr74dzc57m6fmqceygxmxm

### Number of rows: 14942

### Schema:

```
ibis.Schema {
  primary_trading_address_longitude  string
  primary_uk_sic_2007_code           float64
  latest_accounts_date               date
  no_of_available_years              int64
  registered_number                  string
  company_name                       string
  branch_name                        string
  ticker_symbol                      string
  primary_trading_address_latitude   string
  primary_uk_sic_2007_description    string
  primary_trading_address            string
}
```

### Head of table:

```
  primary_trading_address_longitude  primary_uk_sic_2007_code  \
0                               NaN                   30300.0   
1                               NaN                   84220.0   
2                               NaN                   84110.0   
3                     0° 57' 8.1" W                   70229.0   
4                    1° 13' 12.8" W                   70100.0   

  latest_accounts_date  no_of_available_years registered_number  \
0           2023-12-31                     20          01996687   
1           2024-03-31                     20          02342138   
2           2024-03-31                      7          10881715   
3           2023-12-31                     20          00242246   
4           2023-12-31                     20          04736639   

                        company_name                        branch_name  \
0   BAE SYSTEMS (OPERATIONS) LIMITED   BAE SYSTEMS (OPERATIONS) LIMITED   
1    BABCOCK INTERNATIONAL GROUP PLC    BABCOCK INTERNATIONAL GROUP PLC   
2  SUPPLY CHAIN COORDINATION LIMITED  SUPPLY CHAIN COORDINATION LIMITED   
3                      SERCO LIMITED                      SERCO LIMITED   
4                    AMEY UK LIMITED                    AMEY UK LIMITED   

  ticker_symbol primary_trading_address_latitude  \
0           NaN                              NaN   
1           BAB                              NaN   
2           NaN                              NaN   
3           NaN                  51° 16' 44.7" N   
4           NaN                  51° 42' 56.2" N   

                     primary_uk_sic_2007_description  \
0  Manufacture of air and spacecraft and related ...   
1                                 Defence activities   
2           General public administration activities   
3  Management consultancy activities (other than ...   
4                         Activities of head offices   

                             primary_trading_address  
0                                                NaN  
1                                                NaN  
2                                                NaN  
3  Serco House, 16 Bartley Wood Business Park, Ba...  
4  Chancery Exchange, 10 Furnival Street, London,...  
```

## ibis_pandas_memtable_kvldxrh7ararpjpq62h6llob3i

### Number of rows: 17483

### Schema:

```
ibis.Schema {
  primary_trading_address_longitude  string
  primary_uk_sic_2007_code           float64
  latest_accounts_date               date
  no_of_available_years              int64
  registered_number                  int64
  company_name                       string
  branch_name                        string
  ticker_symbol                      float64
  primary_trading_address_latitude   string
  primary_uk_sic_2007_description    string
  primary_trading_address            int32
}
```

### Head of table:

```
  primary_trading_address_longitude  primary_uk_sic_2007_code  \
0                    1° 27' 44.6" W                   49410.0   
1                    1° 27' 44.6" W                   49410.0   
2                    1° 27' 44.6" W                   49410.0   
3                               NaN                   49410.0   
4                               NaN                   49320.0   

  latest_accounts_date  no_of_available_years  registered_number  \
0           2007-12-31                      3            5318482   
1           2007-12-31                      3            5318497   
2           2007-12-31                      3            5318499   
3           2018-03-31                     13            5318777   
4           2010-12-31                      6            5318801   

                 company_name                 branch_name  ticker_symbol  \
0      GREENSTEAD HELPERS LTD      GREENSTEAD HELPERS LTD            NaN   
1     LUTTERWORTH SUPPORT LTD     LUTTERWORTH SUPPORT LTD            NaN   
2  WILLENHALL ENDORSEMENT LTD  WILLENHALL ENDORSEMENT LTD            NaN   
3         A W HALSALL LIMITED                         NaN            NaN   
4         BRIDGE CABS LIMITED         BRIDGE CABS LIMITED            NaN   

  primary_trading_address_latitude primary_uk_sic_2007_description  \
0                  53° 49' 37.7" N       Freight transport by road   
1                  53° 49' 37.7" N       Freight transport by road   
2                  53° 49' 37.7" N       Freight transport by road   
3                              NaN       Freight transport by road   
4                              NaN                  Taxi operation   

  primary_trading_address  
0                    None  
1                    None  
2                    None  
3                    None  
4                    None  
```

## ibis_pandas_memtable_v2dnn6s2hzdb5ku3ljiqznklcq

### Number of rows: 12288

### Schema:

```
ibis.Schema {
  primary_trading_address_longitude  string
  primary_uk_sic_2007_code           float64
  latest_accounts_date               date
  no_of_available_years              int64
  registered_number                  string
  company_name                       string
  branch_name                        string
  ticker_symbol                      float64
  primary_trading_address_latitude   string
  primary_uk_sic_2007_description    string
  primary_trading_address            string
}
```

### Head of table:

```
  primary_trading_address_longitude  primary_uk_sic_2007_code  \
0                               NaN                       NaN   
1                               NaN                       NaN   
2                               NaN                   93290.0   
3                               NaN                   93290.0   
4                               NaN                   93290.0   

  latest_accounts_date  no_of_available_years registered_number  \
0           2010-12-31                      4          IE430990   
1           2015-11-30                      9          IE431230   
2           2023-11-30                     17          IE431532   
3           2024-02-29                     17          IE431551   
4           2023-12-31                     17          IE431821   

                              company_name  \
0  FRESHFORD DISTRICT & CHILDCARE  LIMITED   
1              WEXFORD YOUTHS F.C. LIMITED   
2              LUACHRA PRODUCTIONS LIMITED   
3      CLAYCASTLE RECORDING STUDIO LIMITED   
4              MERMAID PRODUCTIONS LIMITED   

                               branch_name  ticker_symbol  \
0  FRESHFORD DISTRICT & CHILDCARE  LIMITED            NaN   
1              WEXFORD YOUTHS F.C. LIMITED            NaN   
2              LUACHRA PRODUCTIONS LIMITED            NaN   
3      CLAYCASTLE RECORDING STUDIO LIMITED            NaN   
4              MERMAID PRODUCTIONS LIMITED            NaN   

  primary_trading_address_latitude            primary_uk_sic_2007_description  \
0                              NaN                                        NaN   
1                              NaN                                        NaN   
2                              NaN  Other amusement and recreation activities   
3                              NaN  Other amusement and recreation activities   
4                              NaN  Other amusement and recreation activities   

                            primary_trading_address  
0                                               NaN  
1                                               NaN  
2                                               NaN  
3                                               NaN  
4  25 Herbert Place, Dublin 2, Co. Dublin, D02 AY86  
```

## ibis_pandas_memtable_x46kkdybcnapviv4xblsy5nbma

### Number of rows: 1933

### Schema:

```
ibis.Schema {
  primary_trading_address_longitude  string
  primary_uk_sic_2007_code           float64
  latest_accounts_date               date
  no_of_available_years              int64
  registered_number                  string
  company_name                       string
  branch_name                        string
  ticker_symbol                      float64
  primary_trading_address_latitude   string
  primary_uk_sic_2007_description    string
  primary_trading_address            int32
}
```

### Head of table:

```
  primary_trading_address_longitude  primary_uk_sic_2007_code  \
0                               NaN                   49410.0   
1                               NaN                   49410.0   
2                               NaN                   47300.0   
3                               NaN                   46180.0   
4                               NaN                   66190.0   

  latest_accounts_date  no_of_available_years registered_number  \
0           2017-12-31                     11          IE007481   
1           2023-12-31                     20          IE008860   
2           2024-02-29                     20          IE012253   
3           2024-03-31                     20          IE013519   
4           2023-09-30                     20          IE014257   

                              company_name  \
0  G. W. BIGGS & COMPANY UNLIMITED COMPANY   
1     D.F. DOYLE PROPERTIES (CORK) LIMITED   
2      SULLIVANS FUNERAL DIRECTORS LIMITED   
3                LAURENCE C. GUNNE LIMITED   
4                A.R. O'HARE & CO. LIMITED   

                               branch_name  ticker_symbol  \
0  G. W. BIGGS & COMPANY UNLIMITED COMPANY            NaN   
1     D.F. DOYLE PROPERTIES (CORK) LIMITED            NaN   
2      SULLIVANS FUNERAL DIRECTORS LIMITED            NaN   
3                LAURENCE C. GUNNE LIMITED            NaN   
4                A.R. O'HARE & CO. LIMITED            NaN   

  primary_trading_address_latitude  \
0                              NaN   
1                              NaN   
2                              NaN   
3                              NaN   
4                              NaN   

                     primary_uk_sic_2007_description primary_trading_address  
0                          Freight transport by road                    None  
1                          Freight transport by road                    None  
2  Retail sale of automotive fuel in specialised ...                    None  
3  Agents specialised in the sale of other partic...                    None  
4  Other activities auxiliary to financial servic...                    None  
```

## ibis_pandas_memtable_zbcvkrpqtjg7xbjxuurxptacr4

### Number of rows: 1647

### Schema:

```
ibis.Schema {
  primary_trading_address_longitude  string
  primary_uk_sic_2007_code           float64
  latest_accounts_date               date
  no_of_available_years              int64
  registered_number                  string
  company_name                       string
  branch_name                        string
  ticker_symbol                      string
  primary_trading_address_latitude   string
  primary_uk_sic_2007_description    string
  primary_trading_address            string
}
```

### Head of table:

```
  primary_trading_address_longitude  primary_uk_sic_2007_code  \
0                               NaN                       NaN   
1                               NaN                   94120.0   
2                               NaN                       NaN   
3                               NaN                   35230.0   
4                               NaN                   94990.0   

  latest_accounts_date  no_of_available_years registered_number  \
0           2004-03-31                      4          IE017163   
1           2017-10-31                     17          IE020724   
2           2001-12-31                      4          IE020937   
3           2023-12-31                     20          IE021207   
4           2023-12-31                     20          IE021589   

                                        company_name  \
0                        J. P. FREYNE & SONS LIMITED   
1  LOCAL AUTHORITY MEDICAL SPECIALISTS COMPANY LI...   
2                                   C.E.R.T. LIMITED   
3                         THE GATHERING PROJECT 2013   
4    ORDER OF MALTA IRELAND PROPERTY HOLDING COMPANY   

                                         branch_name ticker_symbol  \
0                        J. P. FREYNE & SONS LIMITED           NaN   
1  LOCAL AUTHORITY MEDICAL SPECIALISTS COMPANY LI...           NaN   
2                                   C.E.R.T. LIMITED           NaN   
3                         THE GATHERING PROJECT 2013           NaN   
4    ORDER OF MALTA IRELAND PROPERTY HOLDING COMPANY           NaN   

  primary_trading_address_latitude  \
0                              NaN   
1                              NaN   
2                              NaN   
3                              NaN   
4                              NaN   

                     primary_uk_sic_2007_description  \
0                                                NaN   
1  Activities of professional membership organisa...   
2                                                NaN   
3                         Trade of gas through mains   
4  Activities of other membership organisations n...   

                             primary_trading_address  
0                                                NaN  
1                                                NaN  
2                                                NaN  
3                                                NaN  
4  32 Clyde Road, Ballsbridge, Dublin 4, Dublin, ...  
```

## ibis_pandas_memtable_zpsg5s5trjdodhyicmrd4stuoi

### Number of rows: 19440

### Schema:

```
ibis.Schema {
  primary_trading_address_longitude  string
  primary_uk_sic_2007_code           float64
  latest_accounts_date               date
  no_of_available_years              int64
  registered_number                  string
  company_name                       string
  branch_name                        string
  ticker_symbol                      string
  primary_trading_address_latitude   string
  primary_uk_sic_2007_description    string
  primary_trading_address            string
}
```

### Head of table:

```
  primary_trading_address_longitude  primary_uk_sic_2007_code  \
0                     0° 9' 28.2" W                   93199.0   
1                      0° 8' 0.1" W                   60200.0   
2                               NaN                   92000.0   
3                               NaN                   93290.0   
4                    2° 12' 15.6" W                   93120.0   

  latest_accounts_date  no_of_available_years registered_number  \
0           2023-07-31                     20          02719699   
1           2023-12-31                     20          04174493   
2           2008-09-27                      6          04639005   
3           2023-11-30                      7          10354575   
4           2023-06-30                     20          00040946   

                                      company_name  \
0  THE FOOTBALL ASSOCIATION PREMIER LEAGUE LIMITED   
1           FORMULA ONE WORLD CHAMPIONSHIP LIMITED   
2                             SUITCASE ONE LIMITED   
3                      FENIX INTERNATIONAL LIMITED   
4            MANCHESTER CITY FOOTBALL CLUB LIMITED   

                                       branch_name ticker_symbol  \
0  THE FOOTBALL ASSOCIATION PREMIER LEAGUE LIMITED           NaN   
1           FORMULA ONE WORLD CHAMPIONSHIP LIMITED           NaN   
2                                              NaN           NaN   
3                      FENIX INTERNATIONAL LIMITED           NaN   
4            MANCHESTER CITY FOOTBALL CLUB LIMITED           NaN   

  primary_trading_address_latitude  \
0                   51° 31' 4.0" N   
1                  51° 30' 33.3" N   
2                              NaN   
3                              NaN   
4                  53° 28' 58.1" N   

                     primary_uk_sic_2007_description  \
0  Other sports activities (not including activit...   
1  Television programming and broadcasting activi...   
2                    Gambling and betting activities   
3          Other amusement and recreation activities   
4                          Activities of sport clubs   

                             primary_trading_address  
0  Brunel Building, 57 North Wharf Road, London, ...  
1  No. 2 St. James's Market, London, London, SW1Y...  
2                                                NaN  
3                                                NaN  
4  Etihad Stadium Etihad Campus, City of Manchest...  
```

