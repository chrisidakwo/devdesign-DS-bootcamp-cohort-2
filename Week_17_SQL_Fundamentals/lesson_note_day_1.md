# SQL for Data Scientists — Day 1: SQL Fundamentals and Querying Data
## Data Science Bootcamp (with Python)

## Learning Objectives
By the end of this lesson, you will be able to:
1. Understand what databases are and why they matter in data science
2. Distinguish between different database engines and understand where SQLite fits
3. Navigate the sqliteonline.com environment to run SQL queries
4. Write SQL queries using SELECT, FROM, WHERE, ORDER BY, and LIMIT
5. Use aggregate functions (COUNT, SUM, AVG, MIN, MAX) with GROUP BY
6. Filter grouped data using HAVING
7. Set up VSCode with SQLite extensions for local SQL development

## Pre-Class Setup
**What You'll Need:**
- A web browser (Chrome or Firefox recommended)
- The Chinook SQLite database file (`chinook.db`) — download from the shared class folder
- VSCode installed (from previous weeks)

**Instructor:**
- Download the Chinook SQLite database from: https://github.com/lerocha/chinook-database/releases
  (Download `Chinook_Sqlite.sqlite` and rename it to `chinook.db`)
- Upload `chinook.db` to the shared Google Drive folder
- Verify that https://sqliteonline.com is accessible

---

## Part 1: What is a Database and Why SQL?

### What is a Database?

A database is an organized collection of data stored electronically. Think of it like a collection of spreadsheets — but much more powerful, faster, and designed to handle millions of rows without breaking a sweat.

If you've been working with CSV files and Pandas DataFrames, you're already familiar with the concept of structured data in rows and columns. A database takes this further by:
- Storing multiple related tables that connect to each other
- Enforcing rules about what data can go into each column (data types, constraints)
- Allowing multiple people to read and write data at the same time without conflicts
- Handling millions or even billions of rows efficiently
- Keeping data safe with backup, recovery, and access control features

In the real world, virtually every company stores its data in databases — not in CSV files. When you work as a data scientist, the data you need for analysis almost always lives in a database somewhere. Your customer records, sales transactions, website activity logs, sensor readings — all sitting in databases waiting to be queried.

### What is SQL?

SQL stands for **Structured Query Language**. It's the standard language for communicating with databases. When you want to ask a database a question — like "how many customers do we have in Lagos?" or "what were our total sales last quarter?" — you write that question in SQL.

SQL has been around since the 1970s and remains the most widely used language for data retrieval. As a data scientist, you'll use SQL almost daily to:
- **Extract data** from company databases for analysis
- **Filter and aggregate** large datasets before loading them into Python
- **Join related tables** to combine information from different sources
- **Explore data** quickly without writing Python scripts

Here's what a SQL query looks like — don't worry about understanding it yet, just notice how readable it is:

```sql
SELECT customer_name, city, total_purchases
FROM customers
WHERE country = 'Nigeria'
ORDER BY total_purchases DESC
LIMIT 10;
```

Even without knowing SQL, you can probably guess what this does: *"Give me the customer name, city, and total purchases from the customers table, but only for customers in Nigeria, sorted by the highest purchases, and show me just the top 10."* That's the beauty of SQL — it reads almost like English.

### Database Engines — The Software Behind Databases

A **database engine** (also called a Database Management System or DBMS) is the software that creates, manages, and lets you query databases. There are many database engines out there, each with different strengths. Here are the most common ones you'll encounter as a data scientist:

**Popular Database Engines:**

| Database Engine | Type | Commonly Used By |
|---|---|---|
| **PostgreSQL** | Server-based, open source | Startups, tech companies, data teams |
| **MySQL** | Server-based, open source | Web applications, WordPress, e-commerce |
| **Microsoft SQL Server** | Server-based, commercial | Enterprise companies, banks, government |
| **Oracle Database** | Server-based, commercial | Large corporations, telecom companies |
| **SQLite** | File-based, open source | Mobile apps, prototyping, embedded systems, learning |
| **Google BigQuery** | Cloud-based | Large-scale data analytics |
| **Amazon Redshift** | Cloud-based | Data warehousing |

The key thing to understand is: **they all use SQL**. The core SQL language is the same across all these engines. Once you learn SQL on one engine, you can use it on any other — the syntax is 90-95% identical. There are minor differences in advanced features, but the fundamentals (which is what we'll focus on) are universal.

This means what you learn this week is **directly transferable** to any job or project that involves databases — regardless of which specific engine the company uses.

### Why SQLite for This Class?

We'll be using **SQLite** for our lessons, and there are very good reasons for this:

1. **Zero setup required** — SQLite doesn't need you to install a database server. The entire database is just a single file (like `chinook.db`). No server installation, no configuration, no passwords.

2. **Built into Python** — Python ships with the `sqlite3` module. You can connect to a SQLite database without installing any additional packages. Just `import sqlite3` and you're ready.

3. **Portable** — A SQLite database is a single `.db` file that you can share via Google Drive, WhatsApp, email, or USB drive. Everyone gets the same data instantly.

4. **Perfect for learning** — Because there's no server to manage, you can focus entirely on learning SQL itself rather than fighting with database administration.

5. **Real-world usage** — SQLite is not just a toy. It's used in every Android phone, every iPhone, every web browser (Chrome, Firefox, Safari), WhatsApp, Skype, and countless other applications. It's the most deployed database engine in the world.

The trade-off is that SQLite is designed for single-user, lightweight applications — it's not what a bank would use for its core transaction system. But for learning SQL and for data science work (loading data, prototyping queries, local analysis), it's ideal.

### Why SQL Matters for Data Scientists

You might wonder: *"I already know Pandas — why do I need SQL?"* Great question. Here's the reality:

1. **Data lives in databases** — In most companies, you won't receive a CSV file. You'll be given access to a database and expected to pull your own data. SQL is how you do that.

2. **SQL handles scale** — Pandas loads everything into your computer's memory (RAM). If a dataset has 500 million rows, your laptop will struggle. SQL databases can filter and aggregate that data on the server before sending you only the results you need.

3. **It's the universal data language** — Every data scientist, data analyst, data engineer, and backend developer speaks SQL. It's the common language across data teams.

4. **Job interviews require it** — Almost every data science job interview includes SQL questions. It's a non-negotiable skill.

5. **SQL + Python = Power combo** — The best workflow is often: use SQL to pull and filter the data you need, then use Python (Pandas, Matplotlib, Scikit-learn) for analysis, visualization, and modeling. We'll practice this exact workflow tomorrow.

---

## Part 2: Exploring sqliteonline.com and the Chinook Database

### Getting Started with sqliteonline.com

sqliteonline.com is a free, browser-based tool that lets you open and query SQLite databases without installing anything. It's perfect for getting started quickly.

**Let's set it up together:**

1. Open your browser and go to **https://sqliteonline.com**
2. You'll see a SQL editor on the right and a sidebar on the left
3. Click **"File"** → **"Open DB"** at the top
4. Select the `chinook.db` file you downloaded from the class folder
5. The left sidebar should now show a list of tables — that means the database is loaded!

The interface has three main areas:
- **Left sidebar** — shows all the tables in the database. Click on a table name to see its structure (column names and data types).
- **SQL editor (top right)** — this is where you type your SQL queries
- **Results panel (bottom right)** — this is where query results appear after you click "Run"

Try it now — type this in the SQL editor and click **Run**:

```sql
SELECT * FROM Artist LIMIT 5;
```

You should see 5 rows of artist data. Congratulations — you've just run your first SQL query!

### The Chinook Database — Our Music Store

The Chinook database models a **digital music store** (think of it like a simplified version of Apple Music or Spotify's backend). It contains data about artists, albums, songs, customers, and purchases. Let's explore what's inside.

**Tables in the Chinook Database:**

| Table | What It Stores | Row Count |
|---|---|---|
| `Artist` | Music artists/bands | 275 |
| `Album` | Albums released by artists | 347 |
| `Track` | Individual songs/tracks | 3,503 |
| `Genre` | Music genres (Rock, Jazz, etc.) | 25 |
| `MediaType` | Format of the track (MP3, AAC, etc.) | 5 |
| `Playlist` | Curated playlists | 18 |
| `PlaylistTrack` | Which tracks are in which playlist | 8,715 |
| `Customer` | Store customers | 59 |
| `Employee` | Store staff | 8 |
| `Invoice` | Customer purchases/orders | 412 |
| `InvoiceLine` | Individual items in each purchase | 2,240 |

**How the tables connect to each other:**

The tables are related — they reference each other through shared columns (called **foreign keys**). Here's how the main relationships work:

- An **Artist** has many **Albums**
- An **Album** has many **Tracks**
- Each **Track** belongs to one **Genre** and one **MediaType**
- A **Customer** can have many **Invoices** (purchases)
- Each **Invoice** has many **InvoiceLines** (the individual tracks purchased)
- Each **Customer** is supported by one **Employee** (their support representative)

This connected structure is what makes databases powerful — you can follow the relationships to answer complex questions like *"Which artist generated the most revenue?"* by tracing the chain: Artist → Album → Track → InvoiceLine → Invoice.

Let's quickly peek at a few key tables to get familiar with the data:

```sql
-- Look at the first 10 artists
SELECT * FROM Artist LIMIT 10;
```

```sql
-- Look at the first 10 customers
SELECT * FROM Customer LIMIT 10;
```

```sql
-- Look at the structure of the Track table
SELECT * FROM Track LIMIT 5;
```

```sql
-- What genres are available?
SELECT * FROM Genre;
```

Take a moment to click through the tables in the sqliteonline.com sidebar and browse the data. Notice the column names, the data types, and how some columns (like `ArtistId` in the `Album` table) reference other tables.

---

## Part 3: SQL Fundamentals — SELECT, FROM, and WHERE

### Your First SQL Queries — SELECT and FROM

Every SQL query starts with two essential keywords:
- **SELECT** — specifies *which columns* you want to see
- **FROM** — specifies *which table* to get the data from

```sql
-- See everything in the Artist table
-- The * means "all columns"
SELECT * FROM Artist;
```

The `*` (asterisk) is a wildcard that means "give me all columns." While convenient for exploring, in practice you'll usually specify exactly which columns you need:

```sql
-- Select specific columns from the Customer table
SELECT FirstName, LastName, Country FROM Customer;
```

This returns only three columns instead of all thirteen columns in the Customer table. This is more efficient and easier to read, especially when tables have many columns.

```sql
-- See what genres exist in the store
SELECT Name FROM Genre;
```

```sql
-- See album titles
SELECT Title FROM Album;
```

**Column Aliases with AS:**

You can rename columns in your results using `AS` to make them more readable:

```sql
-- Give columns friendlier names
SELECT FirstName AS First_Name, 
       LastName AS Last_Name, 
       Email AS Email_Address 
FROM Customer;
```

The `AS` keyword creates an alias — a temporary name for the column that only applies to your query results. The actual column name in the database doesn't change.

### Filtering Data with WHERE

The `WHERE` clause lets you filter rows based on conditions — like asking *"only show me rows where this condition is true."*

```sql
-- Customers from Brazil
SELECT FirstName, LastName, City, Country 
FROM Customer 
WHERE Country = 'Brazil';
```

The `WHERE` clause works with several comparison operators:

| Operator | Meaning | Example |
|---|---|---|
| `=` | Equal to | `WHERE Country = 'Brazil'` |
| `!=` or `<>` | Not equal to | `WHERE Country != 'Brazil'` |
| `>` | Greater than | `WHERE Total > 10` |
| `<` | Less than | `WHERE Total < 5` |
| `>=` | Greater than or equal to | `WHERE Total >= 10` |
| `<=` | Less than or equal to | `WHERE Total <= 5` |

```sql
-- Tracks longer than 5 minutes (duration is stored in milliseconds)
-- 5 minutes = 5 × 60 × 1000 = 300,000 milliseconds
SELECT Name, Milliseconds 
FROM Track 
WHERE Milliseconds > 300000;
```

```sql
-- Tracks in the Rock genre (GenreId 1 = Rock)
SELECT Name, Composer 
FROM Track 
WHERE GenreId = 1;
```

```sql
-- Invoices with a total greater than $10
SELECT InvoiceId, CustomerId, Total, InvoiceDate
FROM Invoice
WHERE Total > 10;
```

### Combining Conditions — AND, OR, NOT

You can combine multiple conditions using logical operators:

```sql
-- Customers from Brazil who live in São Paulo
SELECT FirstName, LastName, City 
FROM Customer 
WHERE Country = 'Brazil' AND City = 'São Paulo';
```

```sql
-- Customers from Brazil OR Argentina
SELECT FirstName, LastName, Country 
FROM Customer 
WHERE Country = 'Brazil' OR Country = 'Argentina';
```

```sql
-- Tracks that are NOT in the Rock genre
SELECT Name, GenreId 
FROM Track 
WHERE GenreId != 1;
```

```sql
-- Combine AND and OR (use parentheses to be clear about order)
SELECT FirstName, LastName, Country, City
FROM Customer
WHERE Country = 'USA' AND (City = 'New York' OR City = 'Chicago');
```

### The IN Operator — Checking Multiple Values

When you need to check if a column matches any value from a list, use `IN` instead of writing multiple `OR` conditions:

```sql
-- Customers from any of these countries
SELECT FirstName, LastName, Country 
FROM Customer 
WHERE Country IN ('Brazil', 'Germany', 'France', 'United Kingdom');
```

This is much cleaner than writing:
```sql
WHERE Country = 'Brazil' OR Country = 'Germany' OR Country = 'France' OR Country = 'United Kingdom'
```

### Pattern Matching with LIKE

The `LIKE` operator lets you search for patterns within text columns. It uses two special wildcard characters:
- `%` — a wildcard that matches any sequence of characters (zero or more characters)
- `_` — matches exactly one character

```sql
-- Artists whose name starts with 'The'
SELECT * FROM Artist 
WHERE Name LIKE 'The%';
```

```sql
-- Artists with 'Black' anywhere in the name
SELECT * FROM Artist 
WHERE Name LIKE '%Black%';
```

```sql
-- Customers whose email ends with '.com'
SELECT FirstName, LastName, Email 
FROM Customer 
WHERE Email LIKE '%.com';
```

```sql
-- Customers with a 5-letter first name (each _ matches one character)
SELECT FirstName, LastName 
FROM Customer 
WHERE FirstName LIKE '_____';
```

### Handling NULL Values

`NULL` in SQL represents missing or unknown data. It's similar to `NaN` in Pandas. You cannot use `=` to check for NULL — you must use `IS NULL` or `IS NOT NULL`:

```sql
-- Tracks where the composer is unknown
SELECT Name, Composer 
FROM Track 
WHERE Composer IS NULL 
LIMIT 10;
```

```sql
-- Tracks where the composer IS known
SELECT Name, Composer 
FROM Track 
WHERE Composer IS NOT NULL 
LIMIT 10;
```

### 🛠 Hands-on Exercise 1: "Exploring the Music Store"

**Real-world Context:**
You've just been hired as a data analyst at a digital music store. Your manager has given you access to the database and wants you to familiarize yourself with the data by answering some basic questions.

**Tasks:**
1. Show all columns from the `Album` table. How many columns does it have?
2. Show only the `FirstName`, `LastName`, `Email`, and `City` columns from the `Customer` table
3. Find all customers from `Canada`
4. Find all tracks where the `Composer` is `'U2'`
5. Find all customers from `Germany` OR `France`
6. Find all artists whose name contains the word `'Miles'`
7. Find all tracks where the `Composer` is unknown (NULL)
8. Find all customers whose email uses a `gmail.com` domain

**Why This Matters:**
In any data science role, the first thing you do with a new database is explore it — understand what tables exist, what columns they have, and what the data looks like. These exploration queries are something you'll do every single time you encounter a new dataset.

---

## Part 4: Sorting, Limiting, and Removing Duplicates

### Sorting Results with ORDER BY

The `ORDER BY` clause sorts your results by one or more columns. By default, it sorts in ascending order (`ASC`). Use `DESC` for descending order:

```sql
-- Tracks sorted by duration, longest first
SELECT Name, Milliseconds 
FROM Track 
ORDER BY Milliseconds DESC;
```

```sql
-- Customers sorted alphabetically by country, then by last name within each country
SELECT FirstName, LastName, Country 
FROM Customer 
ORDER BY Country ASC, LastName ASC;
```

```sql
-- Most recent invoices first
SELECT InvoiceId, CustomerId, InvoiceDate, Total
FROM Invoice
ORDER BY InvoiceDate DESC;
```

### Limiting Results with LIMIT

`LIMIT` restricts the number of rows returned. This is essential when working with large tables — you don't want to accidentally return millions of rows:

```sql
-- Top 10 longest tracks
SELECT Name, Milliseconds 
FROM Track 
ORDER BY Milliseconds DESC 
LIMIT 10;
```

```sql
-- 5 most expensive invoices
SELECT InvoiceId, CustomerId, Total 
FROM Invoice 
ORDER BY Total DESC 
LIMIT 5;
```

```sql
-- First 10 customers alphabetically
SELECT FirstName, LastName, Country
FROM Customer
ORDER BY LastName ASC
LIMIT 10;
```

### Removing Duplicates with DISTINCT

`DISTINCT` removes duplicate rows from your results:

```sql
-- What unique countries do our customers come from?
SELECT DISTINCT Country FROM Customer ORDER BY Country;
```

```sql
-- What unique billing cities appear in our invoices?
SELECT DISTINCT BillingCity, BillingCountry 
FROM Invoice 
ORDER BY BillingCountry, BillingCity;
```

```sql
-- How many unique countries do we have customers in?
SELECT COUNT(DISTINCT Country) AS UniqueCountries FROM Customer;
```

### 🛠 Hands-on Exercise 2: "Top Lists and Rankings"

**Real-world Context:**
Your music store manager is preparing for a quarterly review meeting and needs quick reports on various "top" and "bottom" lists.

**Tasks:**
1. Show the top 15 most expensive tracks by `UnitPrice`. Display the track name and price.
2. Show all customers sorted by `Country` in ascending order, then by `LastName` within each country.
3. Show the 10 most recent invoices. Display invoice ID, date, billing country, and total amount.
4. List all unique countries where the music store has customers. How many unique countries are there?
5. Find the 5 shortest tracks in the database. Show the track name and duration in milliseconds.
6. Show the top 10 highest-value invoices. Display invoice ID, customer ID, billing country, and total.

**Why This Matters:**
Sorting and limiting are critical for generating reports and dashboards. Business stakeholders frequently want "top N" lists — top customers, top products, most recent transactions. The `DISTINCT` keyword helps you understand the unique values in your data, which is essential for data exploration and quality checks.

---

## Part 5: Aggregate Functions and GROUP BY

### Counting, Summing, and Averaging

Aggregate functions perform calculations across multiple rows and return a single result. The most common aggregate functions are:

| Function | What It Does | Example |
|---|---|---|
| `COUNT(*)` | Counts the number of rows | How many customers? |
| `COUNT(column)` | Counts non-NULL values in a column | How many tracks have a composer? |
| `SUM(column)` | Adds up all values | Total revenue |
| `AVG(column)` | Calculates the average | Average invoice amount |
| `MIN(column)` | Finds the smallest value | Cheapest track |
| `MAX(column)` | Finds the largest value | Longest track |

```sql
-- How many tracks are in the database?
SELECT COUNT(*) AS TotalTracks FROM Track;
```

```sql
-- How many tracks have a known composer?
SELECT COUNT(Composer) AS TracksWithComposer FROM Track;
```

```sql
-- Total revenue from all invoices
SELECT SUM(Total) AS TotalRevenue FROM Invoice;
```

```sql
-- Average invoice amount
SELECT AVG(Total) AS AverageInvoice FROM Invoice;
```

```sql
-- Get a complete summary in one query
SELECT 
    COUNT(*) AS TotalInvoices,
    SUM(Total) AS TotalRevenue,
    AVG(Total) AS AverageInvoice,
    MIN(Total) AS SmallestInvoice,
    MAX(Total) AS LargestInvoice
FROM Invoice;
```

### Grouping Data with GROUP BY

`GROUP BY` splits your data into groups and applies aggregate functions to each group separately. This is where SQL gets truly powerful for analysis:

```sql
-- How many customers per country?
SELECT Country, COUNT(*) AS CustomerCount 
FROM Customer 
GROUP BY Country 
ORDER BY CustomerCount DESC;
```

The `GROUP BY` clause works like Pandas' `groupby()`. The query above is equivalent to:
```python
# Pandas equivalent
df.groupby('Country').size().sort_values(ascending=False)
```

```sql
-- Revenue by billing country
SELECT BillingCountry, 
       SUM(Total) AS Revenue, 
       COUNT(*) AS NumberOfInvoices,
       AVG(Total) AS AvgInvoiceValue
FROM Invoice 
GROUP BY BillingCountry 
ORDER BY Revenue DESC;
```

```sql
-- Number of albums per artist (using ArtistId for now — we'll get names tomorrow with JOINs)
SELECT ArtistId, COUNT(*) AS AlbumCount
FROM Album
GROUP BY ArtistId
ORDER BY AlbumCount DESC
LIMIT 10;
```

```sql
-- Number of tracks per genre
SELECT GenreId, 
       COUNT(*) AS TrackCount,
       AVG(Milliseconds) AS AvgDuration,
       AVG(UnitPrice) AS AvgPrice
FROM Track
GROUP BY GenreId
ORDER BY TrackCount DESC;
```

```sql
-- Revenue by year
SELECT strftime('%Y', InvoiceDate) AS Year, 
       SUM(Total) AS Revenue,
       COUNT(*) AS InvoiceCount
FROM Invoice 
GROUP BY Year 
ORDER BY Year;
```

The `strftime('%Y', InvoiceDate)` function extracts the year from a date column. `strftime` stands for "string format time" and is SQLite's way of working with dates. The `'%Y'` format code means "four-digit year."

### Filtering Groups with HAVING

`WHERE` filters individual rows *before* grouping. `HAVING` filters *groups after* aggregation. This distinction is important:

```sql
-- Countries with more than 5 customers
SELECT Country, COUNT(*) AS CustomerCount 
FROM Customer 
GROUP BY Country 
HAVING CustomerCount > 5
ORDER BY CustomerCount DESC;
```

```sql
-- Billing countries that generated more than $30 in total revenue
SELECT BillingCountry, SUM(Total) AS Revenue 
FROM Invoice 
GROUP BY BillingCountry 
HAVING Revenue > 30
ORDER BY Revenue DESC;
```

```sql
-- Artists with more than 5 albums
SELECT ArtistId, COUNT(*) AS AlbumCount 
FROM Album 
GROUP BY ArtistId 
HAVING AlbumCount > 5
ORDER BY AlbumCount DESC;
```

**Understanding WHERE vs HAVING:**

```sql
-- WHERE filters rows BEFORE grouping
-- "Only look at invoices from 2012, then group by country"
SELECT BillingCountry, SUM(Total) AS Revenue 
FROM Invoice 
WHERE InvoiceDate LIKE '2012%'
GROUP BY BillingCountry 
ORDER BY Revenue DESC;
```

```sql
-- HAVING filters AFTER grouping
-- "Group all invoices by country, then only show countries with revenue > $40"
SELECT BillingCountry, SUM(Total) AS Revenue 
FROM Invoice 
GROUP BY BillingCountry 
HAVING Revenue > 40
ORDER BY Revenue DESC;
```

```sql
-- You can use both together
-- "Look at 2012 invoices only, group by country, then show only countries above $10"
SELECT BillingCountry, SUM(Total) AS Revenue 
FROM Invoice 
WHERE InvoiceDate LIKE '2012%'
GROUP BY BillingCountry 
HAVING Revenue > 10
ORDER BY Revenue DESC;
```

### 🛠 Hands-on Exercise 3: "Music Store Analytics"

**Real-world Context:**
The music store's management team is preparing an annual business review. They need aggregated reports on revenue, customer distribution, and catalog composition. You've been asked to produce these reports using SQL.

**Tasks:**
1. How many artists are in the database?
2. How many albums does each artist have? Show `ArtistId` and the count, sorted by count descending. Limit to the top 10.
3. What is the total revenue from each billing country? Show country and total revenue, sorted by revenue descending.
4. What is the average track length (in milliseconds) per `GenreId`? Sort by average length descending. Which genre has the longest tracks on average?
5. Which billing cities have generated more than $30 in total revenue? Show city, country, and total revenue.
6. How many invoices were generated in each year? Show the year and count, sorted by year.
7. How many tracks are there per `MediaTypeId`? Which media type has the most tracks?
8. **Bonus:** Find genres (`GenreId`) that have more than 100 tracks AND an average track price above $0.99.

**Why This Matters:**
GROUP BY and aggregate functions are the bread and butter of data analysis in SQL. Almost every business question — "what are our top markets?", "how has revenue changed over time?", "which product categories perform best?" — requires grouping and aggregating data. Mastering this skill means you can answer most analytical questions directly in SQL before ever opening Python.

---

## Part 6: Setting Up VSCode for SQL

### Why Move to VSCode?

sqliteonline.com is great for getting started quickly. But as data scientists, we want our SQL work in the same environment as our Python code. VSCode gives us:
- Syntax highlighting for SQL files
- The ability to save and organize our queries in `.sql` files
- Side-by-side work with Python notebooks and scripts
- A professional workflow that mirrors real data science environments

### Step 1: Install the SQLite Extensions and Browse the Database Visually

[//]: # TODO(Update the installation step to use DB Browser for SQLite)
1. In VSCode's file explorer (left sidebar), click on `chinook.db`
2. The **SQLite Viewer** extension will open it, showing all tables in a visual interface
3. Click on any table name (e.g., `Customer`) to see its data in a spreadsheet-like view
4. You can click column headers to sort the data
5. This is a quick way to inspect what data looks like before writing queries

### Step 4: Write and Run Your First Query in VSCode

1. Create a new file: **File → New File**, save it as `day1_practice.sql`
2. Type this query:

```sql
SELECT FirstName, LastName, Country 
FROM Customer 
WHERE Country = 'Brazil';
```

3. Select (highlight) the query text
4. Right-click on the selected text → choose **"Run Selected Query"**
5. The results appear in a new tab at the bottom of VSCode!

**Pro Tips for Working with SQL in VSCode:**
- You can write multiple queries in one `.sql` file — just highlight the specific query you want to run
- Add comments with `--` to document your queries
- Separate queries with a blank line for readability

### Step 6: Practice in VSCode

Create a file called `day1_vscode_practice.sql` and write these queries. Run each one to verify it works:

```sql
-- Query 1: Top 10 longest tracks
SELECT Name, Milliseconds 
FROM Track 
ORDER BY Milliseconds DESC 
LIMIT 10;

-- Query 2: Customer count by country
SELECT Country, COUNT(*) AS CustomerCount 
FROM Customer 
GROUP BY Country 
ORDER BY CustomerCount DESC;

-- Query 3: Total revenue by billing country (top 10)
SELECT BillingCountry, 
       SUM(Total) AS Revenue
FROM Invoice 
GROUP BY BillingCountry 
ORDER BY Revenue DESC 
LIMIT 10;

-- Query 4: Revenue summary
SELECT 
    COUNT(*) AS TotalInvoices,
    ROUND(SUM(Total), 2) AS TotalRevenue,
    ROUND(AVG(Total), 2) AS AvgInvoice,
    MIN(Total) AS MinInvoice,
    MAX(Total) AS MaxInvoice
FROM Invoice;
```

---

## Key Takeaways

1. **Databases and SQL Basics**
   - A database is an organized collection of related tables, more powerful than CSV files
   - SQL is the universal language for querying databases — learn it once, use it everywhere
   - SQLite is a lightweight, file-based database engine that's perfect for learning and data science prototyping
   - The skills you learn with SQLite transfer directly to PostgreSQL, MySQL, SQL Server, and all other database engines

2. **Core SQL Query Structure**
   - `SELECT` specifies which columns to retrieve; `FROM` specifies the table
   - `WHERE` filters rows based on conditions; supports `AND`, `OR`, `NOT`, `IN`, `LIKE`, `IS NULL`
   - `ORDER BY` sorts results; `LIMIT` restricts the number of rows returned
   - `DISTINCT` removes duplicate values from results

3. **Aggregate Functions and Grouping**
   - `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` perform calculations across rows
   - `GROUP BY` splits data into groups before applying aggregate functions
   - `HAVING` filters groups after aggregation (unlike `WHERE` which filters before)
   - Combining `GROUP BY` with aggregate functions is how you answer most business analytics questions

4. **The Chinook Database**
   - A music store database with 11 related tables covering artists, albums, tracks, customers, and sales
   - Tables connect through shared columns (foreign keys) — we'll explore these connections with JOINs tomorrow

5. **Development Environment**
   - sqliteonline.com provides instant, browser-based SQL querying with no setup
   - VSCode with the SQLite Viewer and SQLite extensions provides a professional local development environment
   - Save your queries in `.sql` files for documentation and reuse

---

## 📝 Take-Home Exercise: "Getting to Know the Music Store"

**Real-world Context:**
You've just completed your first day as a data analyst at the Chinook Music Store. Your team lead wants to see that you can navigate the database independently. They've given you a list of questions to answer using SQL — save all your queries in a file called `day1_homework.sql` with clear comments explaining what each query does.

**Tasks:**

1. List all unique countries where customers are located. How many unique countries are there?

2. Find all tracks that cost more than $0.99. How many are there?

3. Which 5 countries have the most customers? Show the country name and customer count.

4. What is the total revenue, average invoice amount, smallest invoice, and largest invoice across all invoices? Round all values to 2 decimal places. *(Hint: use the `ROUND()` function)*

5. How many invoices were billed to each country in the year 2010? Show the billing country and invoice count, sorted by count descending. *(Hint: use `WHERE InvoiceDate LIKE '2010%'`)*

6. Which 3 billing cities generated the most revenue? Show the city, country, and total revenue.

7. How many tracks belong to each genre (`GenreId`)? Only show genres with more than 50 tracks. Sort by track count descending.

8. Find the total number of tracks, the average track length in minutes (not milliseconds), and the average track price. Round all values to 2 decimal places. *(Hint: divide milliseconds by 60,000 to get minutes)*

9. **Challenge:** For each year in the database, calculate the total revenue, total number of invoices, and the average invoice value. Sort by year. Which year had the highest revenue?

10. **Challenge:** Find all customers whose `FirstName` starts with the letter 'A' and who are from a country that has more than 3 customers in total. *(Hint: first figure out which countries have more than 3 customers, then use that information in your WHERE clause with the `IN` operator)*

## Additional Resources
- [SQL Tutorial — W3Schools](https://www.w3schools.com/sql/) — Quick reference for SQL syntax
- [SQLite Documentation](https://www.sqlite.org/docs.html) — Official SQLite documentation
- [Chinook Database on GitHub](https://github.com/lerocha/chinook-database) — Source and documentation for the Chinook database
- [sqliteonline.com](https://sqliteonline.com/) — Browser-based SQLite environment