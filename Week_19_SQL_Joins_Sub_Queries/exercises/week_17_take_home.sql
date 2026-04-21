-- # 1. List all unique countries where customers are located. How many unique countries are there?

-- Part A: List all unique countries
SELECT DISTINCT Country FROM customer ORDER BY Country;

-- Part B: Count how many uni que countries there are
SELECT COUNT(DISTINCT Country) AS UniqueCountryCount
FROM customer;

-- # 2. Find all tracks that cost more than $0.99. How many are there?

-- Part A: List all tracks that cost more than 0.99
SELECT
    NAME, UnitPrice
FROM track
WHERE UnitPrice > 0.99
ORDER BY UnitPrice;

-- Part B: Count how many tracks that cost more than 0.99

SELECT COUNT(*) AS ExpensiveTrackCount
FROM track
WHERE UnitPrice > 0.99;

-- # 3. Which 5 countries have the most customers? Show the country name and customer count.

SELECT
    Country,
    COUNT(CustomerId) AS CustomerCount
FROM customer
GROUP BY Country
ORDER BY CustomerCount DESC
LIMIT 5;

-- # 4. What is the total revenue, average invoice amount, smallest invoice, and largest invoice across all invoices? Round all values to 2 decimal places. *(Hint: use the `ROUND()` function)*

SELECT
    ROUND(SUM(total), 2) AS TotalRevenue,
    ROUND(AVG(total), 2) as AvgRevenue,
    ROUND(MIN(total), 2) as SmallestRevenueAmt,
    ROUND(MAX(total), 2) as LargestRevenueAmt
FROM Invoice;

-- # 5. How many invoices were billed to each country in the year 2010? Show the billing country and invoice count, sorted by count descending. *(Hint: use `WHERE InvoiceDate LIKE '2010%'`)*

-- # WHERE InvoiceDate LIKE '2010%' -- Not good pattern

SELECT BillingCountry, COUNT(InvoiceId) AS InvoiceCount
FROM invoice
WHERE YEAR(InvoiceDate) = 2010
GROUP BY BillingCountry
ORDER BY InvoiceCount DESC;

-- # 6. Which 3 billing cities generated the most revenue? Show the city, country, and total revenue.

SELECT BillingCity, BillingCountry, SUM(Total) AS TotalRevenue
FROM invoice
GROUP BY BillingCity, BillingCountry
ORDER BY TotalRevenue DESC
LIMIT 3;

-- # 7. How many tracks belong to each genre (`GenreId`)? Only show genres with more than 50 tracks. Sort by track count descending.

SELECT
    GenreId, COUNT(TrackId) AS TrackCount
FROM track
GROUP BY genreId
HAVING COUNT(TrackId) > 50
ORDER BY TrackCount DESC;

-- # 8. Find the total number of tracks, the average track length in minutes (not milliseconds), and the average track price. Round all values to 2 decimal places. *(Hint: divide milliseconds by 60,000 to get minutes)*

SELECT
    COUNT(TrackId) AS TrackCount,
    ROUND(AVG(Milliseconds / 1000 / 60), 2) AS AverageLengthMins,
    ROUND(AVG(UnitPrice), 2) as AvgTrackPrice
FROM track;

-- # 9. **Challenge:** For each year in the database, calculate the total revenue, total number of invoices,
-- # and the average invoice value. Sort by year. Which year had the highest revenue?

SELECT
    YEAR(InvoiceDate) AS InvoiceYear,
    SUM(Total) AS Revenue,
    COUNT(InvoiceId) AS InvoiceCount,
    AVG(Total) AS AvgInvoiceValue
FROM invoice
GROUP BY InvoiceYear
ORDER BY InvoiceYear;

-- # 10. **Challenge:** Find all customers whose `FirstName` starts with the letter 'A'
-- # and who are from a country that has more than 3 customers in total.
-- # *(Hint: first figure out which countries have more than 3 customers,
-- # then use that information in your WHERE clause with the `IN` operator)*

SELECT FirstName, LastName, Country
FROM customer
WHERE FirstName LIKE 'A%'
    AND Country IN (
        SELECT Country
        FROM customer
        GROUP BY Country
        HAVING COUNT(CustomerId) > 3
    );