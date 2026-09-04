-- Problem: Find Customer Referee
-- Platform: LeetCode
-- Date: 2026-09-04
-- Topic: WHERE / NULL Filtering / OR
--
-- Goal:
-- Return customers who were not referred by customer with id 2,
-- including customers whose referee_id is NULL.

SELECT
    name
FROM Customer
WHERE referee_id IS NULL
   OR referee_id <> 2;
