import pandas as pd
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()
# ✅ Load Supabase credentials
url = os.getenv("SUPABASE_URL")  # or directly put your Supabase URL
key = os.getenv("SUPABASE_KEY")  # or directly put your Supabase anon key
supabase: Client = create_client(url, key)

# ✅ Load CSV
df = pd.read_csv("sectoral_data_companies.csv")

# ✅ Convert wide to long format
df_melted = df.melt(var_name="industry", value_name="company")

# ✅ Remove null/NaN values
df_melted = df_melted.dropna(subset=["company"]).reset_index(drop=True)

# ✅ Convert to records
records = df_melted.to_dict(orient="records")

# ✅ Upload in batches
batch_size = 500
for i in range(0, len(records), batch_size):
    batch = records[i:i + batch_size]
    #response = supabase.table("sectoral_data_companies").insert(batch).execute()

    try:
        response = supabase.table("sectoral_data_companies").insert(batch).execute()
        print("✅ Uploaded batch successfully:", response.data)
    except Exception as e:
        print("❌ Error uploading batch:", e)