/*
Problem: Duplicate Emails
Platform: LeetCode
Date: 2026-08-20
Topic: GROUP BY / HAVING / COUNT
*/

SELECT
    email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
