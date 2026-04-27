import pandas as pd
from mysql.connector import connect
import matplotlib.pyplot as plt

conn = connect(
    host="127.0.0.1",
    user="root",
    password="chrisidakwo",
    database="chinook"
)

# Revenue by Country — Horizontal Bar Chart
query = """
SELECT BillingCountry AS Country, 
       ROUND(SUM(Total), 2) AS Revenue
FROM Invoice 
GROUP BY BillingCountry 
ORDER BY Revenue DESC
LIMIT 10
"""

df = pd.read_sql(query, conn)

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df['Country'], df['Revenue'], color='teal')
ax.set_xlabel('Revenue ($)')
ax.set_title('Top 10 Countries by Revenue — Chinook Music Store')
ax.invert_yaxis()
plt.tight_layout()
plt.show()