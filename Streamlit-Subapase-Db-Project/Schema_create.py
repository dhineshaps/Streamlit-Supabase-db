import pandas as pd

df = pd.read_csv("sectoral_data_companies.csv")
print(df.dtypes)

def generate_create_table_sql(df, table_name="sectoral_data_companies"):
    dtype_map = {
        "object": "TEXT",
        "int64": "BIGINT",
        "float64": "DOUBLE PRECISION",
        "bool": "BOOLEAN",
        "datetime64[ns]": "TIMESTAMP"
    }

    sql_lines = [f'CREATE TABLE "{table_name}" (']
    for col in df.columns:
        col_type = dtype_map.get(str(df[col].dtype), "TEXT")
        sql_lines.append(f'  "{col}" {col_type},')
    sql_lines[-1] = sql_lines[-1].rstrip(',')  # remove last comma
    sql_lines.append(");")
    return "\n".join(sql_lines)

sql = generate_create_table_sql(df, "sectoral_data_companies")
print(sql)