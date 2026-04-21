SELECT T.Name AS Track, G.Name AS Genre, AR.Name AS Artist
FROM track AS T
JOIN genre AS G ON T.GenreId = G.GenreId
JOIN album AS AL ON T.AlbumId = AL.AlbumId
JOIN artist AS AR ON AL.ArtistId = AR.ArtistId;

SELECT *
FROM album
INNER JOIN artist ON album.ArtistId = artist.ArtistId;

-- Number of tracks per genre (with genre names)
SELECT g.Name AS Genre,
       COUNT(t.TrackId) AS TrackCount
FROM Track t
INNER JOIN genre g ON t.GenreId = g.GenreId
GROUP BY g.Name
ORDER BY TrackCount DESC;

-- Number of albums per artist (with artist names)
SELECT
    ar.Name AS Artist,
    COUNT(al.AlbumId) AS AlbumCount
FROM album al
JOIN artist ar ON al.ArtistId = ar.ArtistId
GROUP BY ar.Name
ORDER BY AlbumCount DESC;

-- Total Spending Per Customer
SELECT CONCAT(c.FirstName, ' ', c.LastName) AS Name, SUM(i.Total) AS TotalSpent
FROM invoice i
INNER JOIN customer c ON i.CustomerId = c.CustomerId
GROUP BY c.CustomerId
ORDER BY TotalSpent DESC;

-- Top 10 artists by revenue
SELECT
    aR.name AS Artist,
    SUM(iL.UnitPrice * iL.Quantity) AS Revenue
FROM invoiceline iL
JOIN track t ON iL.TrackId = t.TrackId
JOIN album aL ON t.AlbumId = aL.AlbumId
JOIN artist aR ON aL.ArtistId = aR.ArtistId
GROUP BY aR.ArtistId
ORDER BY Revenue DESC
LIMIT 10;


