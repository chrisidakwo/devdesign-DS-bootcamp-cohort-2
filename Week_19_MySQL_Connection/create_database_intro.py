import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="chrisidakwo"
)

cursor = conn.cursor()

# Create a new database
cursor.execute("CREATE DATABASE IF NOT EXISTS sample_db")
cursor.execute("USE sample_db")

# Deletes all the rows in a table and resets the auto-increment memory to 1; for that table.
# cursor.execute("TRUNACATE TABLE students")

# Removes the table from the database
# cursor.execute("DROP TABLE IF EXISTS students")

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        city VARCHAR(50),
        math_score INT,
        science_score INT,
        
        CONSTRAINT ix_student_name UNIQUE(first_name, last_name)
    )
""")

# # Data to insert
students = [
    ('Chinedu', 'Okafor', 'Lagos', 85, 90),
    ('Aisha', 'Bello', 'Abuja', 92, 85),
    ('Kwame', 'Mensah', 'Accra', 78, 82),
    ('Fatima', 'Ibrahim', 'Kano', 88, 79),
    ('Emeka', 'Nwosu', 'Enugu', 95, 88),
    ('Zainab', 'Abubakar', 'Kaduna', 70, 75),
    ('Kofi', 'Asante', 'Kumasi', 82, 80),
    ('Ngozi', 'Eze', 'Owerri', 91, 93),
    ('Yusuf', 'Abdullahi', 'Sokoto', 76, 71),
    ('Adaeze', 'Obi', 'Onitsha', 89, 86)
]

cursor.executemany("""
    INSERT INTO students (first_name, last_name, city, math_score, science_score) 
    VALUES (%s, %s, %s, %s, %s)
""", students)

conn.commit()   # Save the changes to the database

conn.database = "sample_db"

df = pd.read_sql("SELECT * FROM students", conn)
print("\n")
print(df)

cursor.close()
conn.close()


