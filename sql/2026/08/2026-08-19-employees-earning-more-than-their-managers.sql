/*
Problem: Employees Earning More Than Their Managers
Platform: LeetCode
Date: 2026-08-19
Topic: Self Join / Filtering
*/

SELECT
    e1.name AS Employee
FROM Employee AS e1
JOIN Employee AS e2
    ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;
