-- 1. Show all tracks with their genre name (not GenreId). Display the track name and genre name.
-- Limit to 20 results.

SELECT
    t.Name AS Track, g.Name AS Genre
FROM track t
JOIN genre g ON t.GenreId = g.GenreId
LIMIT 20;

-- 2. Show all albums with their artist name, sorted alphabetically by artist name. Limit to 20 results.

SELECT
    al.Title AS Album, ar.Name AS Artist
FROM album al
INNER JOIN artist ar ON al.ArtistId = ar.ArtistId
ORDER BY ar.Name
LIMIT 20;

-- 3. Show all invoices with the customer's full name (first and last), their country, the invoice date,
-- and the total amount. Sort by total amount descending. Show the top 15.

SELECT
    CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName, c.Country, i.InvoiceDate, Total as TotalAmt
FROM invoice i
JOIN customer c ON i.CustomerId = c.CustomerId
LIMIT 15;

--
-- SELECT
--     CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName, c.Country, SUM(Total) as TotalAmt
-- FROM invoice i
-- JOIN customer c ON i.CustomerId = c.CustomerId
-- GROUP BY i.CustomerId
-- LIMIT 15;

-- 4. Show all tracks with their album title, artist name, AND genre name (this requires joining 4 tables).
-- Limit to 20 results.

SELECT
    t.Name AS Track,
    a.Title AS Album,
    ar.Name AS Artist,
    g.Name AS Genre
FROM track t
JOIN album a ON t.AlbumId = a.AlbumId
JOIN artist ar ON a.ArtistId = ar.ArtistId
JOIN genre g ON t.GenreId = g.GenreId
LIMIT 20;

-- 5. How many tracks does each artist have? Show artist name and track count, sorted by track count descending.
-- Limit to top 10. *(Hint: join Track → Album → Artist, then GROUP BY artist name)*

SELECT
    ar.Name as Artist,
    COUNT(t.TrackId) as TrackCount
FROM track t
JOIN album a ON t.AlbumId = a.AlbumId
JOIN artist ar ON a.ArtistId = ar.ArtistId
GROUP BY ar.Name
ORDER BY TrackCount DESC
LIMIT 10;

-- 6. What are the top 5 genres by total revenue? Show genre name and total revenue.
-- *(Hint: join InvoiceLine → Track → Genre)*

SELECT
    g.Name AS Genre, SUM(il.UnitPrice * il.Quantity) AS TotalRevenue
FROM invoiceline il
JOIN track t ON il.TrackId = t.TrackId
JOIN genre g ON t.GenreId = g.GenreId
GROUP BY g.Name
ORDER BY TotalRevenue DESC
LIMIT 5;

-- 7. Which customers have spent more than $40 in total? Show customer full name, country,
-- and total amount spent. Sort by total spent descending.
-- *(You can solve this with either a JOIN + GROUP BY or a subquery — try both approaches!)*

-- Approach 1: Using a sub query
SELECT
    CONCAT(FirstName, ' ', LastName) AS Customer,
    Country,
    (SELECT SUM(Total)
         FROM invoice
         WHERE invoice.CustomerId = customer.CustomerId
     ) AS TotalSpent
FROM customer
WHERE CustomerId IN (
    SELECT CustomerId
    FROM invoice
    GROUP BY CustomerId
    HAVING SUM(Total) > 40
)
ORDER BY TotalSpent DESC;

-- 7. Which customers have spent more than $40 in total? Show customer full name, country,
-- and total amount spent. Sort by total spent descending.

-- Approach 2: Using JOIN clause
SELECT
    CONCAT(c.FirstName, ' ', c.LastName) AS Customer,
    c.Country,
    SUM(i.Total) AS TotalSpent
FROM customer c
JOIN invoice i ON i.CustomerId = c.CustomerId
GROUP BY c.CustomerId
HAVING SUM(i.Total) > 40
ORDER BY TotalSpent DESC;

-- 8. Find all artists who have no albums in the database. How many are there? *(Hint: LEFT JOIN + IS NULL)*

SELECT COUNT(ar.ArtistId) AS ArtistsWithNoAlbum
FROM artist ar
LEFT JOIN album a ON ar.ArtistId = a.ArtistId
WHERE a.AlbumId IS NULL;

-- To list them
SELECT
    ar.Name AS Artist,
    COUNT(a.AlbumId) as AlbumCount
FROM artist ar
LEFT JOIN album a ON ar.ArtistId = a.ArtistId
WHERE a.AlbumId IS NULL
GROUP BY ar.Name
ORDER BY ar.Name;

-- 9. Find all tracks that are longer than the average track length. How many are there?

-- List them
SELECT Name, Milliseconds, (SELECT ROUND(AVG(Milliseconds), 2) FROM track) AS AvgTrackDuration
FROM track
WHERE track.Milliseconds > (SELECT AVG(Milliseconds) FROM track)
ORDER BY Milliseconds DESC;

-- Count them
SELECT
    Count(*)
FROM track
WHERE Milliseconds > (SELECT AVG(Milliseconds) FROM track);
