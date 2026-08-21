/*
Problem: Customers Who Never Order
Platform: LeetCode
Date: 2026-08-21
Topic: LEFT JOIN / Anti Join / NOT EXISTS
*/

-- Approach 1: LEFT JOIN + IS NULL
SELECT
    c.name AS Customers
FROM Customers AS c
LEFT JOIN Orders AS o
    ON c.id = o.customerId
WHERE o.customerId IS NULL;


-- Approach 2: NOT EXISTS
SELECT
    c.name AS Customers
FROM Customers AS c
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders AS o
    WHERE o.customerId = c.id
);