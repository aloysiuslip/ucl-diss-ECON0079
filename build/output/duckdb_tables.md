# Tables in DuckDB database

## lars_fixed

### Number of rows: 452,638

### Schema:

```
ibis.Schema {
  registered_number                string
  company_name_A                   string
  primary_uk_sic_2007_code         string
  primary_uk_sic_2007_description  string
  full_overview                    string
  primary_business_line            string
  no_of_available_years            string
  latest_accounts_date             string
  company_name_B                   string
  inactive                         string
  quoted                           string
  own_data                         string
  woco                             string
  bv_d_id_number                   string
  company_status                   string
  status_date                      string
  legal_form                       string
  date_of_incorporation            string
  accounting_reference_date        string
  registered_accounts_type         string
  jordans_company_classification   string
  account_currency                 string
  guo_name                         string
  guo_bv_d_id_number               string
  duo_name                         string
  duo_bv_d_id_number               string
}
```

### Head of table:

```
  registered_number           company_name_A primary_uk_sic_2007_code  \
0           0028326       BLACKSTAR GROUP SE                    66120   
1           0043472          SCOTTY GROUP SE                    26309   
2           0053787       PETRA DIAMONDS LTD                    08990   
3           0054897               HISCOX LTD                    65120   
4           0056130  LANCASHIRE HOLDINGS LTD                    65120   

                     primary_uk_sic_2007_description full_overview  \
0         Security and commodity contracts brokerage           NaN   
1  Manufacture of communication equipment (other ...           NaN   
2                  Other mining and quarrying n.e.c.           NaN   
3                                 Non-life insurance           NaN   
4                                 Non-life insurance           NaN   

  primary_business_line no_of_available_years latest_accounts_date  \
0                   NaN                     6           2016-06-30   
1                   NaN                     1           2011-12-31   
2                   NaN                     7           2017-06-30   
3                   NaN                     8           2023-12-31   
4                   NaN                     8           2023-12-31   

            company_name_B inactive quoted own_data woco bv_d_id_number  \
0       BLACKSTAR GROUP SE       No     No       No   No     GBH0028326   
1          SCOTTY GROUP SE       No     No       No   No     GBH0043472   
2       PETRA DIAMONDS LTD       No     No       No   No     GBH0053787   
3               HISCOX LTD       No    Yes       No   No     GBH0054897   
4  LANCASHIRE HOLDINGS LTD       No    Yes       No   No     GBH0056130   

  company_status status_date      legal_form date_of_incorporation  \
0         Active         NaN      Public AIM                   NaN   
1         Active         NaN           Other            2012-05-11   
2         Active         NaN      Public AIM            1997-03-25   
3         Active         NaN  Public, Quoted            2006-09-06   
4         Active         NaN  Public, Quoted            2005-10-12   

  accounting_reference_date registered_accounts_type  \
0                       NaN                      NaN   
1                       NaN                      NaN   
2                       NaN                      NaN   
3                       NaN                      NaN   
4                       NaN                      NaN   

  jordans_company_classification account_currency guo_name guo_bv_d_id_number  \
0               Fame A, full a/c              GBP      NaN                NaN   
1               Fame A, full a/c              GBP      NaN                NaN   
2               Fame A, full a/c              GBP      NaN                NaN   
3               Fame A, full a/c              GBP      NaN                NaN   
4               Fame A, full a/c              GBP      NaN                NaN   

  duo_name duo_bv_d_id_number  
0      NaN                NaN  
1      NaN                NaN  
2      NaN                NaN  
3      NaN                NaN  
4      NaN                NaN  
```

## fame_yearly

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
0          IE145517  2007         False       NaN           757.13466   
1          IE205077  2015         False       NaN                 NaN   
2          SC263368  2011         False    27.965            39.65400   
3          SC150956  2008         False       NaN            -3.08000   
4          05312357  2011         False       NaN             1.02000   

   profit_loss_pretax employees  tangibles  tangibles_land_and_buildings  \
0                 NaN      None        NaN                           NaN   
1                 NaN      None        NaN                           NaN   
2              25.714      None        NaN                           NaN   
3                 NaN      None        NaN                           NaN   
4                 NaN      None      2.777                           NaN   

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
0          NaN          NaN                NaN          NaN  -166.945063   
1          NaN          NaN                NaN          NaN          NaN   
2          NaN          NaN                NaN          NaN   -19.363000   
3          NaN          NaN                NaN          NaN    -4.080000   
4        2.777          NaN                NaN        2.777    -9.550000   

   total_assets  liabilites_lt    cos  admin_expenses  interest_paid  \
0    924.079723            NaN    NaN             NaN            NaN   
1           NaN            NaN    NaN             NaN            NaN   
2     59.017000            NaN -0.611           -1.64            NaN   
3      1.390000          -0.39    NaN             NaN            NaN   
4     10.570000            NaN    NaN             NaN            NaN   

   profit_loss_pretax2    tax  dividends  depreciation  r_and_d  \
0                  NaN    NaN        NaN           NaN      NaN   
1                  NaN    NaN        NaN           NaN      NaN   
2               25.714 -6.929        NaN           NaN      NaN   
3                  NaN    NaN        NaN        24.768      NaN   
4                  NaN    NaN        NaN           NaN      NaN   

   remuneration_employees  wages  social_security_costs  pensions_costs  \
0                     NaN    NaN                    NaN             NaN   
1                     NaN    NaN                    NaN             NaN   
2                     NaN    NaN                    NaN             NaN   
3                     NaN    NaN                    NaN             NaN   
4                     NaN    NaN                    NaN             NaN   

   other_staff_costs  renumeration_directors  ebitda  
0                NaN                     NaN     NaN  
1                NaN                     NaN     NaN  
2                NaN                     NaN  25.714  
3                NaN                     NaN     NaN  
4                NaN                     NaN     NaN  
```

## fame_derived

### Number of rows: 7,948,736

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

## lars_yearly

### Number of rows: 2,378,089

### Schema:

```
ibis.Schema {
  registered_number                         string
  company_name                              string
  year                                      string
  consolidated                              string
  employees                                 string
  systemA_industry                          string
  cons_uncons                               string
  turnover_th_gbp                           string
  shareholders_funds_th_gbp                 string
  profit_loss_before_taxation_th_gbp        string
  number_of_employees                       string
  total_assets_th_gbp                       string
  ebitda_th_gbp                             string
  current_liabilities_th_gbp                string
  long_term_liabilities_th_gbp              string
  research_development_th_gbp               string
  wages_salaries_th_gbp                     string
  interest_paid_th_gbp                      string
  taxation_th_gbp                           string
  depreciation_th_gbp                       string
  tangible_assets_th_gbp                    string
  intangible_assets_th_gbp                  string
  fixed_assets_th_gbp                       string
  other_fixed_assets_th_gbp                 string
  pension_costs_th_gbp                      string
  social_security_costs_th_gbp              string
  dividends_distributable_profit_th_gbp     string
  systemB_group                             string
  cost_of_sales_th_gbp                      string
  exceptional_items_pre_gp_th_gbp           string
  cash_out_in_flow_investing_activ_th_gbp   string
  capital_expenditure_financ_invest_th_gbp  string
  acquisition_disposal_th_gbp               string
  equity_dividends_paid_th_gbp              string
  company_name_raw                          string
}
```

### Head of table:

```
  registered_number        company_name  year consolidated employees  \
0           0028326  BLACKSTAR GROUP SE  2013            1        16   
1           0028326  BLACKSTAR GROUP SE  2014            1        13   
2           0028326  BLACKSTAR GROUP SE  2015            1        15   
3           0028326  BLACKSTAR GROUP SE  2016            1        12   
4           0043472     SCOTTY GROUP SE  2011            1        31   

  systemA_industry   cons_uncons turnover_th_gbp shareholders_funds_th_gbp  \
0               58  Consolidated             NaN                     74804   
1               58  Consolidated           13737                     80563   
2               58  Consolidated           22316                    230416   
3               58  Consolidated           19696                    179223   
4               26  Consolidated            5002                      5673   

  profit_loss_before_taxation_th_gbp number_of_employees total_assets_th_gbp  \
0                              12203                  16               75701   
1                               8168                  13               85856   
2                              18384                  15              254899   
3                             -33814                  12              200788   
4                               -200                  31                7517   

  ebitda_th_gbp current_liabilities_th_gbp long_term_liabilities_th_gbp  \
0         12233                       -882                          -15   
1          8587                      -5292                           -1   
2         18730                     -24475                           -8   
3        -31522                     -21500                          -65   
4          3805                      -1684                         -159   

  research_development_th_gbp wages_salaries_th_gbp interest_paid_th_gbp  \
0                         NaN                  1674                 -223   
1                         NaN                   NaN                 -489   
2                         NaN                   NaN                 -322   
3                         NaN                   NaN                -2334   
4                         NaN                  1709                  -27   

  taxation_th_gbp depreciation_th_gbp tangible_assets_th_gbp  \
0              15                  16                     78   
1               8                  12                     66   
2              15                   6                     56   
3             -45                  16                    222   
4             287                  88                    214   

  intangible_assets_th_gbp fixed_assets_th_gbp other_fixed_assets_th_gbp  \
0                       51               67937                       NaN   
1                       49               82094                       NaN   
2                      NaN              252167                       NaN   
3                      NaN              199901                       NaN   
4                     4971                5672                       NaN   

  pension_costs_th_gbp social_security_costs_th_gbp  \
0                  NaN                          NaN   
1                  NaN                          NaN   
2                  NaN                          NaN   
3                  NaN                          NaN   
4                  NaN                          340   

  dividends_distributable_profit_th_gbp   systemB_group cost_of_sales_th_gbp  \
0                                 -1382  58_59_60_61_63                  NaN   
1                                 -1034  58_59_60_61_63                  NaN   
2                                  -647  58_59_60_61_63                  NaN   
3                                  -466  58_59_60_61_63                  NaN   
4                                   NaN           22_30                -2072   

  exceptional_items_pre_gp_th_gbp cash_out_in_flow_investing_activ_th_gbp  \
0                             NaN                                     -37   
1                             NaN                                     -10   
2                             NaN                                      -3   
3                             NaN                                    -171   
4                             NaN                                    -145   

  capital_expenditure_financ_invest_th_gbp acquisition_disposal_th_gbp  \
0                                      NaN                         NaN   
1                                      NaN                         NaN   
2                                      NaN                         NaN   
3                                      NaN                         NaN   
4                                      NaN                         NaN   

  equity_dividends_paid_th_gbp    company_name_raw  
0                        -1382  BLACKSTAR GROUP SE  
1                        -1034  BLACKSTAR GROUP SE  
2                         -647  BLACKSTAR GROUP SE  
3                         -466  BLACKSTAR GROUP SE  
4                          NaN     SCOTTY GROUP SE  
```

## fame_fixed

### Number of rows: 7,948,736

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
}
```

### Head of table:

```
                            company_name registered_number ticker_symbol  \
0     GATOR INTERMEDIATE HOLDCO (UK) LTD          11899400           NaN   
1                         KIEWIT UK LTD.          08817563           NaN   
2           LIQUID GAS EQUIPMENT LIMITED          SC434537           NaN   
3                   CAMFED INTERNATIONAL          02874653           NaN   
4  OCEANEERING SERVICES OVERSEAS LIMITED          03295446           NaN   

                                          ro_address  \
0  Lincoln House, Wellington Crescent, Fradley Pa...   
1  c/o Winston & Strawn London Llp, Citypoint One...   
2  Rosyth Business Park Rosyth, Dunfermline, Fife...   
3  20 Station Road, Cambridge, Cambridgeshire, CB...   
4  c/o Company Secretarial Departme, 280 Bishopsg...   

                  ro_address_line_1               ro_address_line_2  \
0                     Lincoln House             Wellington Crescent   
1   c/o Winston & Strawn London Llp  Citypoint One Ropemaker Street   
2       Rosyth Business Park Rosyth                             NaN   
3                   20 Station Road                             NaN   
4  c/o Company Secretarial Departme                 280 Bishopsgate   

  ro_address_line_3 ro_address_line_4 ro_address_line_5      ro_city  \
0      Fradley Park               NaN               NaN    Lichfield   
1               NaN               NaN               NaN       London   
2               NaN               NaN               NaN  Dunfermline   
3               NaN               NaN               NaN    Cambridge   
4               NaN               NaN               NaN       London   

        ro_county ro_postcode ro_full_postcode ro_country      ro_latitude  \
0   Staffordshire        WS13         WS13 8RZ    England  52° 42' 12.7" N   
1          London        EC2Y         EC2Y 9AW    England  51° 31' 10.8" N   
2            Fife        KY11         KY11 2YD   Scotland              NaN   
3  Cambridgeshire        CB 1          CB1 2JD    England  52° 11' 41.5" N   
4          London        EC2M         EC2M 4AG    England              NaN   

     ro_longitude           ro_nuts_region ro_postal_region  \
0  1° 46' 53.5" W  West Midlands (England)    West Midlands   
1   0° 5' 20.1" W                   London     London Inner   
2             NaN                 Scotland         Scotland   
3    0° 8' 3.2" E          East of England          Eastern   
4             NaN                      NaN     London Inner   

                             primary_trading_address  \
0                                                NaN   
1                                                NaN   
2  Rosyth Business Park Rosyth, Dunfermline, Fife...   
3  20 Station Road, Cambridge, Cambridgeshire, CB...   
4                                                NaN   

  primary_trading_address_latitude primary_trading_address_longitude  \
0                              NaN                               NaN   
1                              NaN                               NaN   
2                              NaN                               NaN   
3                              NaN                               NaN   
4                              NaN                               NaN   

                          branch_name  primary_uk_sic_2007_code  \
0  GATOR INTERMEDIATE HOLDCO (UK) LTD                     99000   
1                                 NaN                     99000   
2        LIQUID GAS EQUIPMENT LIMITED                     99000   
3                CAMFED INTERNATIONAL                     99000   
4                                 NaN                     99000   

                     primary_uk_sic_2007_description latest_accounts_date  \
0  Activities of extraterritorial organisations a...           2023-12-31   
1  Activities of extraterritorial organisations a...           2014-12-31   
2  Activities of extraterritorial organisations a...           2024-03-31   
3  Activities of extraterritorial organisations a...           2023-12-31   
4  Activities of extraterritorial organisations a...           2023-12-31   

   no_of_available_years                              guo  guo_nb  \
0                      5            GAYTOR PARENT LIMITED      73   
1                      1                              NaN       0   
2                     11  BABCOCK INTERNATIONAL GROUP PLC     211   
3                     20                              NaN       0   
4                     20    OCEANEERING INTERNATIONAL INC      94   

        entity_type  
0  Controlled subs.  
1   Single location  
2  Controlled subs.  
3   Single location  
4  Controlled subs.  
```

