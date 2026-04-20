-- 1. Show the top 15 most expensive tracks by `UnitPrice`. Display the track name and price.
select TrackId, Name, UnitPrice
from Track
order by UnitPrice DESC
limit 15;

-- 2. Show all customers sorted by `Country` in ascending order, then by `LastName` within each country.
select CustomerId, FirstName, LastName, Email, Country
from Customer
order by Country ASC, LastName asc;

-- 3. Show the 10 most recent invoices. Display invoice ID, date, billing country, and total amount.
select InvoiceId, InvoiceDate, BillingCountry, Total
from invoice
order by InvoiceDate desc
limit 10;

-- 4. List all unique countries where the music store has customers. How many unique countries are there?
select distinct Country
from Customer;

-- 2nd part of the task: How many unique countries are there?
select COUNT(distinct Country) as CountryCount
from Customer;

-- 5. Find the 5 shortest tracks in the database. Show the track name and duration in milliseconds.
select TrackId, Name, Milliseconds
from track
order by Milliseconds
limit 5;


-- 6. Show the top 10 highest-value invoices. Display invoice ID, customer ID, billing country, and total.
select InvoiceId, CustomerId, BillingCountry, Total
from invoice
order by Total desc
limit 10;

