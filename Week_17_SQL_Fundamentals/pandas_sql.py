import sqlite3
import pandas as pd

# Connection statement
conn = sqlite3.connect("../data/Chinook_Sqlite.sqlite")

# Run a SQL query and load the result into a DataFrame
df = pd.read_sql("SELECT * FROM Customer", conn)

print("")
print(df[["CustomerId", "FirstName", "LastName", "Email"]].head())
print(f"\nShape: {df.shape}")
print(f"\nColumns: {df.columns.tolist()}")
print("\n", "-"*60, "\n")



