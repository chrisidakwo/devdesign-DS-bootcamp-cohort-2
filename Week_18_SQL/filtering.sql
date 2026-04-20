-- Customers who live in Brazil
select CustomerId, FirstName, LastName, Email from Customer where Country = 'Brazil';

-- Comparison Operators
-- = Equal to
-- > Greater than
-- < Less than
-- != / <> Not equal to
-- >= Greater than or equal to
-- <= Less than or equal to

-- List invoices where the total is less than $5
select InvoiceId, InvoiceDate, Total from Invoice where Total > 5;

-- Logical Operators
-- and
-- or

-- Filtering on a range of numbers (values)
-- List invoices where the total amount is between $3 and $6
select InvoiceId, InvoiceDate, Total from Invoice where Total >= 3 and Total <= 6;

-- List tracks longer than 5 minutes
SELECT Name, Milliseconds FROM Track WHERE Milliseconds >= 360000;

-- You can perform maths operations in your SELECT statement/query and use an alias as the label for the result of said operation
SELECT Name, Milliseconds, (Milliseconds / 1000 / 60) as Minutes
FROM Track 
WHERE Milliseconds >= 360000;


select CustomerId, FirstName, LastName, Email, Country
from Customer
where Country = 'United Kingdom'
	or Country = 'Portugal'
	or Country = 'Canada';

select CustomerId, FirstName, LastName, Email, Country
from Customer
where Country in ('United Kingdom', 'Portugal', 'Canada', 'Sweden');





