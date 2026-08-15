/*
Problem: Second Highest Salary
Platform: LeetCode
Date: 2026-08-15
Topic: Subquery / Window Function / Aggregation
*/


-- Approach 1: MAX + Subquery

SELECT
    MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (
    SELECT MAX(salary)
    FROM Employee
);


-- Approach 2: DENSE_RANK

SELECT
    MAX(salary) AS SecondHighestSalary
FROM (
    SELECT
        salary,
        DENSE_RANK() OVER (
            ORDER BY salary DESC
        ) AS ranking
    FROM Employee
) t
WHERE ranking = 2;