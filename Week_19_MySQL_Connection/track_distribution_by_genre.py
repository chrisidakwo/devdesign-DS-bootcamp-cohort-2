import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='chrisidakwo',
    database='chinook'
)

# Track Distribution by Genre — Pie Chart
query = """
SELECT g.Name AS Genre, COUNT(t.TrackId) AS TrackCount
FROM Track t
JOIN Genre g ON t.GenreId = g.GenreId
GROUP BY g.Name
ORDER BY TrackCount DESC
LIMIT 8
"""

df = pd.read_sql(query, conn)

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(df['TrackCount'], labels=df['Genre'], autopct='%1.1f%%', startangle=140)
ax.set_title('Track Distribution by Genre (Top 8)')
plt.tight_layout()
plt.show()