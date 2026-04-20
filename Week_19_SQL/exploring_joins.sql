SELECT T.Name AS Track, G.Name AS Genre, AR.Name AS Artist
FROM track AS T
JOIN genre AS G ON T.GenreId = G.GenreId
JOIN album AS AL ON T.AlbumId = AL.AlbumId
JOIN artist AS AR ON AL.ArtistId = AR.ArtistId;

SELECT *
FROM album
JOIN artist on album.ArtistId = artist.Name