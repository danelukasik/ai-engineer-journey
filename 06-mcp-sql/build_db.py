import pandas as pd
import sqlite3
from pathlib import Path

HERE = Path(__file__).resolve().parent
df = pd.read_csv(HERE.parent / "Data Sets" / "Superstore sales dataset.csv", encoding="utf-8-sig")

# Clean column names so SQL queries don't need quotes
df.columns = [c.strip().replace(" ", "_").replace("-", "_") for c in df.columns]

# Convert day/month/year text dates to YYYY-MM-DD
for col in ["Order_Date", "Ship_Date"]:
    df[col] = pd.to_datetime(df[col], dayfirst=True).dt.strftime("%Y-%m-%d")

conn = sqlite3.connect(HERE / "superstore.db")
df.to_sql("orders", conn, if_exists="replace", index=False)

print(f"Loaded {len(df)} rows")
print(pd.read_sql("SELECT Row_ID, Order_Date, Ship_Date, Sales FROM orders LIMIT 3", conn))
conn.close()