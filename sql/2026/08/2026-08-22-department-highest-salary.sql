-- LeetCode 184: Department Highest Salary
-- Date: 2026-08-22
--
-- Approach:
-- 1. Join Employee and Department tables.
-- 2. Rank employees by salary inside each department.
-- 3. Keep rank 1 so all employees tied for the highest salary are returned.
--
-- Time Complexity: O(n log n) due to ranking/sorting
-- Space Complexity: O(n)

SELECT
    Department,
    Employee,
    Salary
FROM (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (
            PARTITION BY d.id
            ORDER BY e.salary DESC
        ) AS rnk
    FROM Employee AS e
    INNER JOIN Department AS d
        ON e.departmentId = d.id
) AS t
WHERE rnk = 1;
