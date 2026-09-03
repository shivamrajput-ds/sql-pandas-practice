-- Problem: Managers with at Least 5 Direct Reports
-- Platform: LeetCode
-- Date: 2026-09-03
-- Topic: GROUP BY / HAVING / IN / Self Join
--
-- Goal:
-- Return the names of managers who have at least 5 direct reports.


-- Approach 1: GROUP BY managerId + IN

SELECT
    name
FROM Employee
WHERE id IN (
    SELECT
        managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
);


-- Approach 2: Self Join + GROUP BY

SELECT
    name
FROM Employee
WHERE id IN (
    SELECT
        m.id
    FROM Employee AS m
    JOIN Employee AS e
        ON m.id = e.managerId
    GROUP BY m.id
    HAVING COUNT(*) >= 5
);
