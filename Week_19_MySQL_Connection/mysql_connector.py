import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="<password>",
    database="<database>"
)

df = pd.read_sql("""
SELECT BillingCountry AS Country, 
       SUM(Total) AS Revenue,
       COUNT(*) AS Invoices,
       AVG(Total) AS AvgInvoice
FROM Invoice 
GROUP BY BillingCountry 
ORDER BY Revenue DESC
LIMIT 10
""", conn)

print("\n")
print(df)
