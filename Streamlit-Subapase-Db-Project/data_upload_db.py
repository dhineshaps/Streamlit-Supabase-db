import pandas as pd
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import math

# Load env variables
load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)



# Load your CSV file
df = pd.read_csv("All_Stocks_Data.csv", index_col=0)
df["BSE_Symbol"] = pd.to_numeric(df["BSE_Symbol"], errors="coerce").fillna(0).astype(int).astype(str)
# df["BSE_Symbol"] = pd.to_numeric(df["BSE_Symbol"], errors="coerce")  # ensures numbers
# # df["BSE_Symbol"] = df["BSE_Symbol"].fillna(0).astype(int)
# df["BSE_Symbol"] = df["BSE_Symbol"].astype(str)
df = df.fillna("missing") 
# df = df.where(pd.notnull(df), None)

# Convert DataFrame to list of dictionaries (Supabase accepts this)
records = df.to_dict(orient="records")

# Split into batches (Supabase limit is 1000 per insert)
batch_size = 500
total_batches = math.ceil(len(records) / batch_size)

for i in range(total_batches):
    batch = records[i * batch_size : (i + 1) * batch_size]
    try:
        response = supabase.table("All_Stock_Data").insert(batch).execute()
        print(f"✅ Uploaded batch {i + 1}/{total_batches}")
    except Exception as e:
        print(f"❌ Error uploading batch {i + 1}: {e}")