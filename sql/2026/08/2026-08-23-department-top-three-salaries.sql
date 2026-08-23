-- Problem: Department Top Three Salaries
-- Platform: LeetCode
-- Date: 2026-08-23
-- Topic: JOIN / DENSE_RANK / PARTITION BY

SELECT
    Department,
    Employee,
    Salary
FROM (
    SELECT
        DENSE_RANK() OVER (
            PARTITION BY d.name
            ORDER BY e.salary DESC
        ) AS rnk,
        e.name AS Employee,
        e.salary AS Salary,
        d.name AS Department
    FROM Employee AS e
    JOIN Department AS d
        ON e.departmentId = d.id
) AS t
WHERE rnk <= 3;
