use chinook;

select BillingCity, SUM(Total) as total_sales
from Invoice
group by BillingCity;