import pandas as pd
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()
# ✅ Load Supabase credentials
url = os.getenv("SUPABASE_URL")  # or directly put your Supabase URL
key = os.getenv("SUPABASE_KEY")  # or directly put your Supabase anon key
supabase: Client = create_client(url, key)

response = supabase.table("sectoral_data_companies3").select("*").execute()
data = response.data

df = pd.DataFrame(data)

pivot_df = df.groupby("industry")["company"].apply(list).to_dict()
max_len = max(len(companies) for companies in pivot_df.values())
normalized = {k: v + [None]*(max_len - len(v)) for k, v in pivot_df.items()}

final_df = pd.DataFrame(normalized)

final_df.to_csv("industry_companies_unloaded.csv", index=False)