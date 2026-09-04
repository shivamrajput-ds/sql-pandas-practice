-- Problem: Employee Bonus
-- Platform: LeetCode
-- Date: 2026-09-04
-- Topic: LEFT JOIN / NULL Filtering / OR
--
-- Goal:
-- Return employees whose bonus is less than 1000
-- or who do not have a bonus record.

SELECT
    e.name,
    b.bonus
FROM Employee AS e
LEFT JOIN Bonus AS b
    ON e.empId = b.empId
WHERE b.bonus IS NULL
   OR b.bonus < 1000;
