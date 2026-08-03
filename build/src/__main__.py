import os
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
import duckdb
import ibis

load_dotenv(override=True)
env_data_dir = os.getenv("DATA_DIR")
if env_data_dir is None:
	raise ValueError("DATA_DIR environment variable is not set. Please set it in the .env file.")

pd.options.mode.chained_assignment = None  # default='warn'

# define paths
user = "lazycst"
root_dir = Path(os.getcwd()).parent.parent

work_dir = root_dir / "build" / "src"
data_dir = Path(env_data_dir)						# On mobile env, set DATA_DIR in .env to "H:/Other computers/My computer/fame_clean/1_FAME_raw_data/2025.07.30"
output_dir = root_dir / "build" / "output"

output_dir.mkdir(parents=True, exist_ok=True)

# list industry subfolders
industries = [d.name for d in data_dir.iterdir() if d.is_dir()]
print(f"Found {len(industries)} industry folders.")
print(industries)

def init_fame_database_ibis():
    
    db_path = output_dir / "fame_data.duckdb"
    
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

if __name__ == "__main__":
    init_fame_database_ibis()