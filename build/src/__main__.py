import os
from pathlib import Path
from flask import json
import pandas as pd
from dotenv import load_dotenv
import ibis

from traverse import build_raw_file_dict
from dirs import get_data_dirs
pd.options.mode.chained_assignment = None  # default='warn'

dirs = get_data_dirs()
      
# # list industry subfolders
# industries = [d.name for d in data_dir.iterdir() if d.is_dir()]
# print(f"Found {len(industries)} industry folders.")
# print(industries)

# Build the raw file dictionary
# Display output as json in ../output/raw_file_dict.json
raw_file_dict = build_raw_file_dict(dirs.raw_data_dir)
with open(dirs.output_dir / "raw_file_dict.json", "w") as f:
    json.dump(raw_file_dict, f, indent=4)
    print(f"✅ Successfully built raw file dictionary and saved to: {dirs.output_dir / 'raw_file_dict.json'}")

def init_fame_database_ibis():
    
    db_path = dirs.output_dir / "fame_data.duckdb"
    
    # 2. Connect to DuckDB using Ibis
    con = ibis.duckdb.connect(str(db_path))
    print(f"Initializing DuckDB via Ibis at: {db_path}")

    # 3. Define the explicit schema using Ibis types
    # This provides type safety and allows your IDE to lint your definitions
    fame_schema = ibis.schema({
        "company_name": "string",
        "registered_number": "string", 
        "ticker_symbol": "string",
        
        # Registered Office (R/O) Details
        "ro_address": "string",
        "ro_address_line_1": "string",
        "ro_address_line_2": "string",
        "ro_address_line_3": "string",
        "ro_address_line_4": "string",
        "ro_address_line_5": "string",
        "ro_city": "string",
        "ro_county": "string",
        "ro_postcode": "string",
        "ro_full_postcode": "string",
        "ro_country": "string",
        
        # Ingested as string due to raw DMS format (e.g., 54° 36' 24.3'' N)
        "ro_latitude": "string", 
        "ro_longitude": "string",
        
        "ro_nuts_region": "string",
        "ro_postal_region": "string",
        "ro_phone": "string",
        "ro_phone_registered_on_tps": "string",
        "ro_phone_registered_on_ctps": "string",
        
        # Primary Trading Address Details
        "primary_trading_address": "string",
        "primary_trading_address_latitude": "string",
        "primary_trading_address_longitude": "string",
        "primary_trading_address_no_of_employees": "string",
        
        # Operations & Classification
        "branch_name": "string",
        "trade_description": "string",
        "primary_uk_sic_2007_code": "string", # String to retain leading zeros
        "primary_uk_sic_2007_description": "string",
        "full_overview": "string",
        "history": "string",
        "primary_business_line": "string",
        "secondary_business_line": "string",
        "main_activity": "string",
        "secondary_activity": "string",
        "main_products_and_services": "string",
        "size_estimate": "string",
        
        # Strategy & International Exposure
        "strategy_organization_and_policy": "string",
        "strategic_alliances": "string",
        "membership_of_a_network": "string",
        "main_brand_names": "string",
        "main_domestic_country": "string",
        "main_foreign_countries_or_regions": "string",
        "main_production_sites": "string",
        "main_distribution_sites": "string",
        "main_sales_representation_sites": "string",
        "main_customers": "string",
        
        # Temporal metadata
        "latest_accounts_date": "date",
        "no_of_available_years": "int32"
    })

    # 4. Execute the table creation using the Ibis schema
    try:
        # overwrite=True prevents errors if the script is run multiple times during setup
        con.create_table("fame_id_data", schema=fame_schema, overwrite=True)
        print("✅ Successfully created Ibis schema for 'fame_id_data'.")
        
        # Optional: Print the table structure to verify
        print("\nTable Schema Verification:")
        print(con.table("fame_id_data").schema())
        
    except Exception as e:
        print(f"❌ Error creating table: {e}")

# if __name__ == "__main__":
#     init_fame_database_ibis()