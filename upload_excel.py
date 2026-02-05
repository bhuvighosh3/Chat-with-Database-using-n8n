import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine('postgresql://n8n:n8npass@localhost:5432/retaildb')
file_path = os.path.expanduser('~/Downloads/online_retail_II.xlsx')

excel_file = pd.ExcelFile(file_path)

print("Starting upload...")
print(f"Found {len(excel_file.sheet_names)} sheets: {excel_file.sheet_names}")
print("")

for sheet_name in excel_file.sheet_names:
    print(f"Processing sheet: {sheet_name}")
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    table_name = sheet_name.lower().replace(' ', '_').replace('-', '_')
    print(f"  - Rows: {len(df)}")
    print(f"  - Columns: {list(df.columns)}")
    print(f"  - Creating table: {table_name}")
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"  Uploaded successfully")
    print("")

print("All sheets uploaded successfully")
