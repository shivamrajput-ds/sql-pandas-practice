-- Problem: Investments in 2016
-- Platform: LeetCode
-- Date: 2026-09-05
-- Topic: GROUP BY / HAVING / IN / EXISTS / NOT EXISTS / Aggregation
--
-- Goal:
-- Sum tiv_2016 for policyholders who:
-- 1. share the same tiv_2015 with at least one other policyholder, and
-- 2. have a unique (lat, lon) location.
-- Round the result to 2 decimal places.


-- Approach 1: GROUP BY + HAVING + IN

SELECT
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT
        tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND pid IN (
    SELECT
        MIN(pid)
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);


-- Approach 2: EXISTS + NOT EXISTS

SELECT
    ROUND(SUM(i.tiv_2016), 2) AS tiv_2016
FROM Insurance AS i
WHERE EXISTS (
    SELECT 1
    FROM Insurance AS x
    WHERE x.tiv_2015 = i.tiv_2015
      AND x.pid <> i.pid
)
AND NOT EXISTS (
    SELECT 1
    FROM Insurance AS y
    WHERE y.lat = i.lat
      AND y.lon = i.lon
      AND y.pid <> i.pid
);
