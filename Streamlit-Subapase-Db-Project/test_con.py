import os
from dotenv import load_dotenv
from supabase import create_client, Client
import pandas as pd

load_dotenv()

# print(os.environ.get("SUPABASE_URL"))

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# print(supabase)

response = (
    supabase.table("All_Stocks_Data")
    .select("*")
    .execute()
)

data = response.data
df = pd.DataFrame(data)

# Display or use the DataFrame
print(df)