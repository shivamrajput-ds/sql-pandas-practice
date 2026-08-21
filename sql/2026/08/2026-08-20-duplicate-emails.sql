/*
Problem: Duplicate Emails
Platform: LeetCode
Date: 2026-08-20
Topic: GROUP BY / HAVING / COUNT / Window Function
*/

-- Approach 1: GROUP BY + HAVING
SELECT
    email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;


-- Approach 2: Window Function
SELECT DISTINCT
    email AS Email
FROM (
    SELECT
        email,
        COUNT(*) OVER (PARTITION BY email) AS email_count
    FROM Person
) AS t
WHERE email_count > 1;