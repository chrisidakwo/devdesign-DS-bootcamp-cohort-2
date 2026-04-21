-- [Preferred method using a sub query]
-- Find customers who have spent more than $40 total
SELECT
    FirstName, LastName, Country
FROM Customer
WHERE CustomerId IN (
    SELECT CustomerId
    FROM Invoice
    GROUP BY CustomerId
    HAVING SUM(Total) > 40
);

-- [Alternative method using a JOIN clause]
-- Find customers who have spent more than $40 total
SELECT
    c.FirstName, c.LastName, c.Country
FROM invoice
JOIN customer c ON invoice.CustomerId = c.CustomerId
GROUP BY invoice.CustomerId
HAVING SUM(invoice.Total) > 40;

-- Find tracks that are longer than the average track length
SELECT Name, Milliseconds
FROM track
WHERE track.Milliseconds > (SELECT AVG(Milliseconds) FROM track)
ORDER BY Milliseconds DESC;
