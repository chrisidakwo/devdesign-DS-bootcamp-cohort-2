-- What unique countries do our customers come from?
select DISTINCT Country FROM Customer ORDER BY Country;

-- What unique billing cities appear in our invoices?
SELECT DISTINCT BillingCity, BillingCountry
FROM Invoice 
ORDER by BillingCountry, BillingCity;