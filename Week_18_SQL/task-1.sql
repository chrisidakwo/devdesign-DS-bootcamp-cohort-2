-- 1. Show all columns from the `Album` table. How many columns does it have?
describe Album;

-- Or its shortand
-- desc Album;

-- 2. Show only the `FirstName`, `LastName`, `Email`, and `City` columns from the `Customer` table
select FirstName, LastName, Email, City from Customer;

-- 3. Find all customers from `Canada`
select CustomerId, FirstName, LastName, Email from Customer Where Country = 'Canada';

-- 4. Find all tracks where the `Composer` is `'U2'`
select TrackId, Name, Composer from Track where Composer = 'U2';

-- 5. Find all customers from `Germany` OR `France`
select CustomerId, FirstName, LastName
from Customer
where Country = 'Germany' or Country = 'France';

-- 6. Find all artists whose name contains the word `'Miles'`
select * from Artist
where Name like '%Miles%';

-- 7. Find all tracks where the `Composer` is unknown (NULL)
select TrackId, Name, Composer from Track where Composer is null;

-- alternative where <=> is caled a spaceship operator (null-safe equality operator)
select TrackId, Name, Composer from Track where Composer <=> null;

-- 8. Find all customers whose email uses a `gmail.com` domain
select CustomerId, FirstName, LastName, Email
from Customer
where email like "%gmail.com";











