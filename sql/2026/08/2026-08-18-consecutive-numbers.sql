/*
Problem: Consecutive Numbers
Platform: LeetCode
Date: 2026-08-18
Topic: LEAD / LAG / Window Functions / Self Join
*/

-- Approach 1: LEAD + LAG
SELECT DISTINCT
    num AS ConsecutiveNums
FROM (
    SELECT
        num,
        LEAD(num) OVER (ORDER BY id ASC) AS next_num,
        LAG(num) OVER (ORDER BY id ASC) AS prev_num
    FROM Logs
) AS t
WHERE num = next_num
  AND num = prev_num;


-- Approach 2: Self Join
SELECT DISTINCT
    l1.num AS ConsecutiveNums
FROM Logs AS l1
JOIN Logs AS l2
    ON l2.id = l1.id + 1
JOIN Logs AS l3
    ON l3.id = l1.id + 2
WHERE l1.num = l2.num
  AND l2.num = l3.num;
