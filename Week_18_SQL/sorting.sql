SELECT TrackId, Name, Milliseconds
FROM Track 
ORDER BY Milliseconds DESC;

-- Order results using an alias column
SELECT TrackId, Name, Milliseconds, (Milliseconds / 1000 / 60) as Minutes
FROM Track 
ORDER BY Minutes;

-- Customers sorted alphabetically by country, then by last name within each country
SELECT FirstName, LastName, Country 
FROM Customer 
ORDER BY Country ASC, LastName desc;

-- Can also order by a date column
-- Most recent invoices first
SELECT InvoiceId, CustomerId, InvoiceDate, Total
FROM Invoice
ORDER BY InvoiceDate DESC;

