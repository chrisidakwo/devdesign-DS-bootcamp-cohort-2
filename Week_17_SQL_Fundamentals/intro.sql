SELECT name, phone
FROM patients
WHERE city = 'Lagos' AND DATEPART(visit_date, 'M') = 1;

SELECT COUNT(*) FROM patients WHERE DATE(visit_date) >= '2026-01-01';

SELECT name, visit_count FROM patients ORDER BY visit_count DESC LIMIT 5;