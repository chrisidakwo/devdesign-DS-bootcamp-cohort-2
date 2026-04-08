# SQL for Data Scientists — Day 2: JOINs, Subqueries & SQL in Python
## Data Science Bootcamp (with Python)

## Learning Objectives
By the end of this lesson, you will be able to:
1. Understand why JOINs are necessary and how tables relate to each other
2. Write INNER JOIN and LEFT JOIN queries connecting two or more tables
3. Use subqueries to answer complex, multi-step questions
4. Connect to a SQLite database from Python using the `sqlite3` module
5. Load SQL query results into Pandas DataFrames using `pd.read_sql()`
6. Visualize SQL-driven analysis using Matplotlib

## Pre-Class Setup
**What You'll Need:**
- DB Browser for SQLite installed (from Day 1)
- The `chinook.sqlite` file in your `sql-bootcamp` project folder
- Python environment with `pandas` and `matplotlib` installed

---

## Quick Recap — Day 1 (5 minutes)

Yesterday we covered the core building blocks of SQL:
- `SELECT ... FROM` — choosing which columns and table to query
- `WHERE` — filtering rows with conditions
- `ORDER BY` and `LIMIT` — sorting and restricting results
- `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` — aggregate functions
- `GROUP BY` and `HAVING` — grouping data and filtering groups

Today we build on all of that. The big question from yesterday was: *when we grouped tracks by `GenreId`, we got numbers like 1, 2, 3 — not the actual genre names like Rock, Jazz, Latin. How do we get the names?*

The answer is **JOINs** — and that's where we're headed.

---

## Part 1: Understanding JOINs

### Why Do We Need JOINs?

In a well-designed database, information is spread across multiple tables to avoid repetition. For example, the Chinook database doesn't store the artist name inside every single track row. Instead:

- The `Track` table stores an `AlbumId` (a reference to which album the track belongs to)
- The `Album` table stores an `ArtistId` (a reference to which artist made the album)
- The `Artist` table stores the actual artist `Name`

This design avoids duplication — if an artist has 50 tracks, their name is stored once in the `Artist` table, not repeated 50 times in the `Track` table. But it means that when you want to see the artist name alongside track information, you need to **join** the tables together.

A JOIN combines rows from two or more tables based on a related column between them. Think of it as matching records from one table with corresponding records in another, the same way you might cross-reference two spreadsheets by a shared ID column.

### INNER JOIN — Matching Rows from Two Tables

An `INNER JOIN` returns only the rows where there is a match in **both** tables. If an artist has no albums, they won't appear in the result. If an album somehow had no matching artist, it wouldn't appear either.

```sql
-- Albums with their artist names
SELECT Album.Title AS AlbumTitle, 
       Artist.Name AS ArtistName
FROM Album
INNER JOIN Artist ON Album.ArtistId = Artist.ArtistId
LIMIT 15;
```

Let's break down the syntax:
- `FROM Album` — we start with the Album table
- `INNER JOIN Artist` — we want to connect it with the Artist table
- `ON Album.ArtistId = Artist.ArtistId` — this is the matching condition. It says: *"connect each album to the artist whose ArtistId matches"*

When writing JOINs, you'll often use **table aliases** to keep things shorter and more readable:

```sql
-- Same query using aliases (a for Album, ar for Artist)
SELECT a.Title AS AlbumTitle, 
       ar.Name AS ArtistName
FROM Album a
INNER JOIN Artist ar ON a.ArtistId = ar.ArtistId
ORDER BY ar.Name
LIMIT 15;
```

Here `a` is just a short nickname for `Album` and `ar` for `Artist`. You define the alias right after the table name in the `FROM` or `JOIN` clause.

Let's try a few more:

```sql
-- Tracks with their genre names (instead of GenreId numbers)
SELECT t.Name AS TrackName, 
       g.Name AS Genre
FROM Track t
INNER JOIN Genre g ON t.GenreId = g.GenreId
LIMIT 15;
```

```sql
-- Invoices with customer names
SELECT c.FirstName, 
       c.LastName, 
       c.Country,
       i.InvoiceDate, 
       i.Total
FROM Invoice i
INNER JOIN Customer c ON i.CustomerId = c.CustomerId
ORDER BY i.Total DESC
LIMIT 10;
```

```sql
-- Customers with the name of their support representative (employee)
SELECT c.FirstName AS CustomerFirst, 
       c.LastName AS CustomerLast,
       e.FirstName AS RepFirst, 
       e.LastName AS RepLast
FROM Customer c
INNER JOIN Employee e ON c.SupportRepId = e.EmployeeId
LIMIT 10;
```

### Joining Multiple Tables

The real power of JOINs comes when you chain multiple tables together. Each JOIN adds one more table to the mix:

```sql
-- Tracks with their album title AND artist name
SELECT t.Name AS Track, 
       a.Title AS Album, 
       ar.Name AS Artist
FROM Track t
INNER JOIN Album a ON t.AlbumId = a.AlbumId
INNER JOIN Artist ar ON a.ArtistId = ar.ArtistId
LIMIT 15;
```

Here we start with `Track`, join it to `Album` (through `AlbumId`), then join `Album` to `Artist` (through `ArtistId`). The result gives us track name, album title, and artist name — all in one row.

```sql
-- Tracks with album, artist, AND genre
SELECT t.Name AS Track, 
       ar.Name AS Artist,
       a.Title AS Album, 
       g.Name AS Genre
FROM Track t
INNER JOIN Album a ON t.AlbumId = a.AlbumId
INNER JOIN Artist ar ON a.ArtistId = ar.ArtistId
INNER JOIN Genre g ON t.GenreId = g.GenreId
LIMIT 15;
```

### JOINs with Aggregation

Now we can combine JOINs with the GROUP BY and aggregate functions we learned yesterday. This is where things get really powerful — we can answer real business questions:

```sql
-- Number of tracks per genre (with genre NAMES, not IDs)
SELECT g.Name AS Genre, 
       COUNT(t.TrackId) AS TrackCount
FROM Track t
INNER JOIN Genre g ON t.GenreId = g.GenreId
GROUP BY g.Name
ORDER BY TrackCount DESC;
```

Compare this to yesterday's query that showed `GenreId` numbers — now we see the actual genre names. This is the payoff of JOINs.

```sql
-- Number of albums per artist (with artist names)
SELECT ar.Name AS Artist, 
       COUNT(a.AlbumId) AS AlbumCount
FROM Album a
INNER JOIN Artist ar ON a.ArtistId = ar.ArtistId
GROUP BY ar.Name
ORDER BY AlbumCount DESC
LIMIT 10;
```

```sql
-- Total spending per customer
SELECT c.FirstName || ' ' || c.LastName AS Customer,
       c.Country,
       SUM(i.Total) AS TotalSpent,
       COUNT(i.InvoiceId) AS PurchaseCount
FROM Invoice i
INNER JOIN Customer c ON i.CustomerId = c.CustomerId
GROUP BY c.CustomerId
ORDER BY TotalSpent DESC
LIMIT 10;
```

The `||` operator in SQLite concatenates (joins) text strings together. So `c.FirstName || ' ' || c.LastName` combines the first name, a space, and the last name into a full name.

### The Big Query — Which Artist Generated the Most Revenue?

This question requires a 4-table JOIN chain, because revenue data (in `InvoiceLine`) and artist names (in `Artist`) are separated by several tables:

```
Artist → Album → Track → InvoiceLine
```

- `Artist` has the artist name
- `Album` connects artists to their albums
- `Track` connects albums to individual songs
- `InvoiceLine` records each track sold, with `UnitPrice` and `Quantity`

```sql
-- Top 10 artists by revenue
SELECT 
    ar.Name AS Artist,
    SUM(il.UnitPrice * il.Quantity) AS TotalRevenue
FROM InvoiceLine il
INNER JOIN Track t ON il.TrackId = t.TrackId
INNER JOIN Album a ON t.AlbumId = a.AlbumId
INNER JOIN Artist ar ON a.ArtistId = ar.ArtistId
GROUP BY ar.Name
ORDER BY TotalRevenue DESC
LIMIT 10;
```

Reading this in plain English: *"For every item sold (InvoiceLine), follow the chain back to the artist. Multiply the price by quantity for each sale. Group all those amounts by artist name, sum them up, and show the top 10."*

```sql
-- Revenue by genre
SELECT 
    g.Name AS Genre,
    SUM(il.UnitPrice * il.Quantity) AS Revenue,
    COUNT(il.InvoiceLineId) AS ItemsSold
FROM InvoiceLine il
INNER JOIN Track t ON il.TrackId = t.TrackId
INNER JOIN Genre g ON t.GenreId = g.GenreId
GROUP BY g.Name
ORDER BY Revenue DESC;
```

### LEFT JOIN — Including Unmatched Rows

An `INNER JOIN` only returns rows that have a match in both tables. A `LEFT JOIN` returns **all rows from the left table**, even if there's no matching row in the right table. Where there's no match, the right-side columns show `NULL`.

This is useful for finding what's **missing** — artists without albums, customers who haven't purchased, etc.

```sql
-- Find artists who have NO albums in the store
SELECT ar.Name AS Artist, 
       a.Title AS Album
FROM Artist ar
LEFT JOIN Album a ON ar.ArtistId = a.ArtistId
WHERE a.Title IS NULL
ORDER BY ar.Name;
```

Here, `LEFT JOIN` keeps all artists. For artists without albums, the `Album.Title` column is `NULL`. The `WHERE a.Title IS NULL` filter then shows only those unmatched artists.

```sql
-- Count albums per artist, including artists with 0 albums
SELECT ar.Name AS Artist, 
       COUNT(a.AlbumId) AS AlbumCount
FROM Artist ar
LEFT JOIN Album a ON ar.ArtistId = a.ArtistId
GROUP BY ar.Name
ORDER BY AlbumCount ASC
LIMIT 15;
```

With `INNER JOIN`, artists with 0 albums would disappear from the results entirely. `LEFT JOIN` keeps them, showing a count of 0.

**When to use which:**
- **INNER JOIN** — when you only want rows that have matches on both sides (most common)
- **LEFT JOIN** — when you want all rows from the left table, even those without a match (useful for finding gaps, missing data, or "who hasn't done X?")

---

## Part 2: Subqueries

### Queries Inside Queries

A subquery is a SQL query nested inside another query. It lets you break complex questions into steps — the inner query runs first, and its result is used by the outer query.

```sql
-- Find tracks that are longer than the average track length
SELECT Name, Milliseconds 
FROM Track 
WHERE Milliseconds > (SELECT AVG(Milliseconds) FROM Track)
ORDER BY Milliseconds DESC
LIMIT 10;
```

The subquery `(SELECT AVG(Milliseconds) FROM Track)` calculates the average track length first. Then the outer query uses that number to filter tracks. You could calculate the average manually and hard-code it, but the subquery keeps it dynamic — if the data changes, the result updates automatically.

```sql
-- Find customers who have spent more than $40 total
SELECT FirstName, LastName, Country
FROM Customer
WHERE CustomerId IN (
    SELECT CustomerId 
    FROM Invoice 
    GROUP BY CustomerId 
    HAVING SUM(Total) > 40
);
```

The inner query finds the `CustomerId` values of high-spending customers. The outer query then pulls the names and countries of those customers. The `IN` operator checks if a value exists in the list returned by the subquery.

```sql
-- Find the artist with the most albums
SELECT Name 
FROM Artist
WHERE ArtistId = (
    SELECT ArtistId 
    FROM Album 
    GROUP BY ArtistId 
    ORDER BY COUNT(*) DESC 
    LIMIT 1
);
```

```sql
-- Find tracks that belong to the genre with the most tracks
SELECT Name, GenreId 
FROM Track
WHERE GenreId = (
    SELECT GenreId 
    FROM Track 
    GROUP BY GenreId 
    ORDER BY COUNT(*) DESC 
    LIMIT 1
)
LIMIT 15;
```

```sql
-- Find all albums by the artist 'Iron Maiden' (without using JOIN)
SELECT Title 
FROM Album
WHERE ArtistId = (
    SELECT ArtistId 
    FROM Artist 
    WHERE Name = 'Iron Maiden'
);
```

This last example is worth noting — you can often solve the same problem with either a JOIN or a subquery. JOINs are generally preferred for combining data from multiple tables, while subqueries are useful when you need to calculate a value (like an average or a max) to use as a filter condition.

### 🛠 Hands-on Exercise 1: "Connecting the Music Store"

**Real-world Context:**
The music store's analytics team is preparing a quarterly business review. They need reports that combine data from multiple tables — customer behavior, artist performance, and sales trends. Yesterday you could only work with one table at a time. Now, with JOINs and subqueries, you can answer the questions that actually matter to the business.

**Tasks:**

1. Show all tracks with their genre name (not GenreId). Display the track name and genre name. Limit to 20 results.

2. Show all albums with their artist name, sorted alphabetically by artist name. Limit to 20 results.

3. Show all invoices with the customer's full name (first and last), their country, the invoice date, and the total amount. Sort by total amount descending. Show the top 15.

4. Show all tracks with their album title, artist name, AND genre name (this requires joining 4 tables). Limit to 20 results.

5. How many tracks does each artist have? Show artist name and track count, sorted by track count descending. Limit to top 10. *(Hint: join Track → Album → Artist, then GROUP BY artist name)*

6. What are the top 5 genres by total revenue? Show genre name and total revenue. *(Hint: join InvoiceLine → Track → Genre)*

7. Which customers have spent more than $40 in total? Show customer full name, country, and total amount spent. Sort by total spent descending. *(You can solve this with either a JOIN + GROUP BY or a subquery — try both approaches!)*

8. Find all artists who have no albums in the database. How many are there? *(Hint: LEFT JOIN + IS NULL)*

9. Find all tracks that are longer than the average track length. How many are there?

10. **Challenge:** Which employee (support rep) is responsible for the most revenue? Show employee full name and total revenue from their assigned customers' invoices. *(Hint: this requires joining Employee → Customer → Invoice)*

**Why This Matters:**
In the real world, useful data almost never lives in a single table. JOINs are the most critical SQL skill for data scientists — they allow you to combine customer data with transaction data, product data with sales data, employee data with performance data. The ability to chain multiple JOINs to answer a business question is what separates someone who knows SQL basics from someone who can actually use SQL for analysis.

---

## Part 3: SQL Meets Python

### Why Combine SQL and Python?

SQL is excellent at extracting, filtering, and aggregating data from databases. Python (with Pandas, Matplotlib, Seaborn) is excellent at analysis, visualization, and machine learning. The most effective data science workflow combines both:

1. **SQL** pulls and prepares the data you need from the database
2. **Python** receives the result as a DataFrame and does the analysis, visualization, or modeling

This is how most professional data scientists work daily. Let's set it up.

### Connecting to SQLite from Python

Python's built-in `sqlite3` module lets you connect to any SQLite database. Combined with Pandas' `pd.read_sql()` function, you can run a SQL query and get the result directly as a DataFrame — no intermediate CSV files needed.

```python
import sqlite3
import pandas as pd

# Connect to the Chinook database
conn = sqlite3.connect('chinook.sqlite')

# Run a query and load results into a DataFrame
df = pd.read_sql("SELECT * FROM Customer", conn)
print(df.head())
print(f"\nShape: {df.shape}")
print(f"\nColumns: {df.columns.tolist()}")
```

The `sqlite3.connect()` function opens a connection to the database file. The `pd.read_sql()` function takes a SQL query string and a connection object, runs the query, and returns the result as a Pandas DataFrame. From this point, you can work with the data using all the Pandas skills you already know.

```python
# You can pass any SQL query — including JOINs and aggregations
query = """
SELECT BillingCountry AS Country, 
       SUM(Total) AS Revenue,
       COUNT(*) AS Invoices,
       AVG(Total) AS AvgInvoice
FROM Invoice 
GROUP BY BillingCountry 
ORDER BY Revenue DESC
LIMIT 10
"""

revenue_df = pd.read_sql(query, conn)
print(revenue_df)
```

**Pro Tip:** Use triple-quoted strings (`"""..."""`) for multi-line SQL queries. This keeps them readable inside your Python code.

### Visualizing SQL Results

Once query results are in a DataFrame, you can visualize them with Matplotlib and Seaborn just like any other data:

```python
import matplotlib.pyplot as plt

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
```

```python
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
```

```python
# Monthly Revenue Trend — Line Chart
query = """
SELECT strftime('%Y-%m', InvoiceDate) AS Month, 
       ROUND(SUM(Total), 2) AS Revenue
FROM Invoice
GROUP BY Month
ORDER BY Month
"""

df = pd.read_sql(query, conn)

fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(df['Month'], df['Revenue'], marker='o', markersize=3, linewidth=1, color='coral')
ax.set_title('Monthly Revenue Trend')
ax.set_ylabel('Revenue ($)')
plt.xticks(rotation=90, fontsize=6)
plt.tight_layout()
plt.show()
```

```python
# Top 10 Artists by Revenue — using a multi-table JOIN in SQL
query = """
SELECT 
    ar.Name AS Artist,
    ROUND(SUM(il.UnitPrice * il.Quantity), 2) AS Revenue
FROM InvoiceLine il
JOIN Track t ON il.TrackId = t.TrackId
JOIN Album a ON t.AlbumId = a.AlbumId
JOIN Artist ar ON a.ArtistId = ar.ArtistId
GROUP BY ar.Name
ORDER BY Revenue DESC
LIMIT 10
"""

df = pd.read_sql(query, conn)

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df['Artist'], df['Revenue'], color='mediumpurple')
ax.set_xlabel('Revenue ($)')
ax.set_title('Top 10 Artists by Revenue')
ax.invert_yaxis()
plt.tight_layout()
plt.show()
```

### Creating Your Own Database from a CSV

Sometimes you need to go the other direction — take a CSV file or DataFrame and push it into a SQLite database so you can query it with SQL. Pandas makes this trivially easy:

```python
# Create a sample DataFrame (or load from CSV)
data = {
    'student_id': range(1, 11),
    'first_name': ['Chinedu', 'Aisha', 'Kwame', 'Fatima', 'Emeka', 
                    'Zainab', 'Kofi', 'Ngozi', 'Yusuf', 'Adaeze'],
    'last_name': ['Okafor', 'Bello', 'Mensah', 'Ibrahim', 'Nwosu',
                   'Abubakar', 'Asante', 'Eze', 'Abdullahi', 'Obi'],
    'city': ['Lagos', 'Abuja', 'Accra', 'Kano', 'Enugu',
             'Kaduna', 'Kumasi', 'Owerri', 'Sokoto', 'Onitsha'],
    'math_score': [85, 92, 78, 88, 95, 70, 82, 91, 76, 89],
    'science_score': [90, 85, 82, 79, 88, 75, 80, 93, 71, 86]
}
df = pd.DataFrame(data)

# Create a new SQLite database and push the DataFrame into it as a table
new_conn = sqlite3.connect('my_school.db')
df.to_sql('students', new_conn, if_exists='replace', index=False)
print("Table 'students' created successfully!")

# Now query it with SQL
result = pd.read_sql("SELECT * FROM students WHERE math_score > 85", new_conn)
print(result)

# Close the connection when done
new_conn.close()
```

The `df.to_sql()` method writes a DataFrame to a SQL table. The `if_exists='replace'` parameter means: if the table already exists, drop it and create a new one. You could also use `if_exists='append'` to add rows to an existing table.

This is powerful because you can take any CSV file from previous weeks — student records, sales data, telecom data — and turn it into a queryable SQL database in two lines of code.

```python
# Example: loading a CSV directly into SQLite
students_df = pd.read_csv('students.csv')

conn = sqlite3.connect('bootcamp_data.db')
students_df.to_sql('nigerian_students', conn, if_exists='replace', index=False)

# Query it
top_students = pd.read_sql("""
    SELECT first_name, last_name, math_score 
    FROM nigerian_students 
    WHERE math_score > 90 
    ORDER BY math_score DESC
""", conn)
print(top_students)

conn.close()
```

**Always close your connection** with `conn.close()` when you're finished. This releases the database file so other programs can access it.

### 🛠 Hands-on Exercise 2: "Chinook Music Store Analysis"

**Real-world Context:**
You've been contracted as a data science consultant by the Chinook Music Store. The CEO wants a data-driven report on the store's performance. Your deliverable is a Python script (or Jupyter Notebook) that pulls data from the database using SQL, then creates clear visualizations to answer the CEO's questions. This is the exact workflow you'll follow in real data science roles — SQL to extract, Python to analyze and present.

**Tasks:**

1. **Top 10 Artists by Number of Tracks**
   Write a SQL query that joins Track → Album → Artist, counts the number of tracks per artist, and returns the top 10. Load the result into a DataFrame and create a horizontal bar chart.

2. **Revenue by Genre**
   Write a SQL query that joins InvoiceLine → Track → Genre to calculate total revenue per genre. Load into a DataFrame and create a bar chart showing the top 8 genres.

3. **Customer Spending Distribution**
   Write a SQL query that calculates total spending per customer (SUM of Invoice.Total, grouped by CustomerId). Load the result into a DataFrame and create a histogram showing the distribution of customer spending.

4. **Revenue by Year**
   Write a SQL query that extracts the year from `InvoiceDate` using `strftime('%Y', InvoiceDate)` and calculates total revenue per year. Load into a DataFrame and create a bar chart.

5. **Sales Performance by Employee**
   Write a SQL query that joins Employee → Customer → Invoice to calculate total revenue handled by each support representative. Load into a DataFrame and create a horizontal bar chart. Which employee drives the most revenue?

6. **Challenge — Customer Dashboard:**
   Create a single figure with 4 subplots (2×2 grid) showing:
   - Top 10 countries by number of customers (bar chart)
   - Top 10 countries by total revenue (bar chart)
   - Monthly revenue trend across all years (line chart)
   - Top 10 artists by revenue (horizontal bar chart)

   Save the figure as `chinook_dashboard.png`.

**Why This Matters:**
This exercise mirrors a real data science deliverable. In practice, you'll often receive a database, explore it with SQL, and produce a visual report summarizing your findings. The ability to move fluidly between SQL and Python — using each where it's strongest — is one of the most valuable skills in a data scientist's toolkit.

---

## Key Takeaways

1. **JOINs Connect Tables**
   - `INNER JOIN` returns only rows with matches in both tables — use this most of the time
   - `LEFT JOIN` returns all rows from the left table, even without matches — useful for finding missing data
   - You can chain multiple JOINs to connect 3, 4, or more tables in a single query
   - Table aliases (`FROM Track t`) make multi-table queries easier to read and write

2. **Subqueries Break Down Complex Questions**
   - A subquery is a query nested inside another query — the inner query runs first
   - Use subqueries when you need to calculate a value (average, max) to use as a filter condition
   - The `IN` operator checks if a value exists in a list returned by a subquery
   - Many problems can be solved with either a JOIN or a subquery — JOINs are generally preferred for combining data, subqueries for computed conditions

3. **SQL + Python = The Data Science Workflow**
   - `sqlite3.connect()` opens a connection to a SQLite database from Python
   - `pd.read_sql(query, connection)` runs a SQL query and returns the result as a Pandas DataFrame
   - SQL handles the heavy lifting (filtering, joining, aggregating), Python handles the analysis and visualization
   - `df.to_sql()` writes a DataFrame to a SQL table — you can convert any CSV to a queryable database in two lines
   - Always close your connection with `conn.close()` when finished

4. **Transferable Skills**
   - Everything you've learned — SELECT, WHERE, JOIN, GROUP BY, subqueries — works on PostgreSQL, MySQL, SQL Server, and every other major database engine
   - The Python integration pattern (`pd.read_sql()`) works with any database that has a Python connector, not just SQLite
   - In professional environments, you'll use the same SQL skills against much larger databases with millions of rows

---

## 📝 Take-Home Exercise: "Chinook Business Intelligence Report"

**Real-world Context:**
The Chinook Music Store's board of directors is meeting next week. They've asked you to prepare a comprehensive business intelligence report backed by data. Your report should include both the SQL queries (so the data team can verify your work) and Python visualizations (for the board presentation).

**Part A: SQL Queries** — Save in `day2_homework.sql`

1. Find the top 5 artists by total revenue generated. Show artist name and total revenue rounded to 2 decimal places. *(Hint: join InvoiceLine → Track → Album → Artist)*

2. Which employee (support representative) has the most customers assigned to them? Show employee full name and customer count.

3. Find all customers who have never made a purchase. *(Hint: LEFT JOIN Customer to Invoice, look for NULL InvoiceId)*

4. What are the top 3 best-selling genres by total revenue? Show genre name and revenue.

5. For each year in the database (2009–2013), calculate the total revenue and the number of invoices. Sort by year.

6. Which country has the highest average invoice value? Show country and average invoice, but only for countries with more than 5 invoices.

7. **Challenge:** For each customer, find their favorite genre — the genre they've spent the most money on. Show customer full name, country, genre name, and amount spent on that genre. *(Hint: this requires joining Customer → Invoice → InvoiceLine → Track → Genre, grouping by customer and genre, and then using a subquery or clever ordering to pick the top genre per customer)*

**Part B: Python Visualizations** — Save in `day2_analysis.py` or `day2_analysis.ipynb`

8. Create a bar chart showing revenue by year (2009–2013). Add a title and axis labels.

9. Create a horizontal bar chart of the top 10 best-selling artists by revenue.

10. Create a multi-panel figure (2×2 grid) as a "CEO Dashboard" showing:
   - Revenue by year (bar chart)
   - Top 8 genres by revenue (bar chart)
   - Top 10 countries by customer count (horizontal bar chart)
   - Monthly revenue trend for the most recent year in the data (line chart)

   Save the dashboard as `ceo_dashboard.png`.

## Additional Resources
- [SQL JOINs Explained Visually](https://www.atlassian.com/data/sql/sql-join) — Visual guide to different JOIN types
- [Pandas read_sql Documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html) — Official docs for `pd.read_sql()`
- [SQLite Functions Reference](https://www.sqlite.org/lang_corefunc.html) — Built-in SQLite functions including `strftime`
- [Chinook Database Schema Diagram](https://github.com/lerocha/chinook-database) — Visual diagram of table relationships

## SQL Quick Reference Card

| Concept | Syntax |
|---|---|
| Inner Join | `FROM table1 JOIN table2 ON table1.col = table2.col` |
| Left Join | `FROM table1 LEFT JOIN table2 ON table1.col = table2.col` |
| Multi-table Join | Chain multiple `JOIN ... ON` clauses |
| Table Alias | `FROM Track t` (then use `t.Name` instead of `Track.Name`) |
| Concatenate Text | `col1 \|\| ' ' \|\| col2` |
| Subquery as Filter | `WHERE col IN (SELECT col FROM ...)` |
| Subquery as Value | `WHERE col > (SELECT AVG(col) FROM ...)` |
| Extract Year | `strftime('%Y', date_column)` |
| Extract Month | `strftime('%m', date_column)` |
| Year-Month | `strftime('%Y-%m', date_column)` |
| Round | `ROUND(value, decimal_places)` |
| Python Connect | `conn = sqlite3.connect('file.db')` |
| SQL to DataFrame | `df = pd.read_sql("query", conn)` |
| DataFrame to SQL | `df.to_sql('table', conn, if_exists='replace', index=False)` |
| Close Connection | `conn.close()` |