import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

#  Create database connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="<password>"
)

cursor = conn.cursor()

# Create a new database
cursor.execute("CREATE DATABASE IF NOT EXISTS spotify_top_hits")
cursor.execute("USE spotify_top_hits")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS songs
    (
       id               INT AUTO_INCREMENT PRIMARY KEY,
       artist           VARCHAR(50),
       song             VARCHAR(50),
       duration_ms      INT,
       explicit         BOOLEAN,
       year             INT,
       popularity       INT,
       danceability       FLOAT,
       energy       FLOAT,
       `key`       INT,
       loudness       FLOAT,
       mode    INT,
       speechiness FLOAT,
       acousticness FLOAT,
       instrumentalness FLOAT,
       liveness FLOAT,
       valence FLOAT,
       tempo FLOAT,
       genre VARCHAR(50)
    )
""")

# Provide database name to the connection object
conn.database = "spotify_top_hits"

# Read CSV
csv_df = pd.read_csv('../data/spotify_top_hits_2000_2009.csv')

# Option 1: Insert data from Pandas dataframe to database using sqlalchemy
engine = create_engine("mysql+pymysql://root:<password>@localhost:3306/spotify_top_hits")

csv_df.to_sql(
    name="songs",
    con=engine,
    if_exists="replace",
    index=True
)

print(f"Done - {len(csv_df)} rows inserted")

# Option 2: Alternative way to insert to database (from csv) without using sqlalchemy
records = []

for index, row in csv_df.iterrows():
    records.append(
        (row['artist'], row['song'], row['duration_ms'], row['explicit'], row['year'], row['popularity'],
         row['danceability'], row['energy'], row['key'], row['loudness'], row['mode'], row['speechiness'],
         row['acousticness'], row['instrumentalness'], row['liveness'], row['valence'], row['tempo'], row['genre'])
    )

# IMPORTANT NOTE: I had to wrap the key and mode columns in backticks because they're both reserved words
# Without wrapping them, MySQL would think we're trying to use the KEY (PRIMARY KEY) keyword and MODE (as in SQL modes)
# and will not see them as column names

cursor.executemany("""
    INSERT INTO songs (artist, song, duration_ms, explicit, year, popularity, danceability, energy, `key`, loudness, `mode`, speechiness, acousticness, instrumentalness, liveness, valence, tempo, genre)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", records)

print(f"Done - {len(records)} rows inserted")
