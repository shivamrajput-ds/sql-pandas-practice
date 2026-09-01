-- Problem: Big Countries
-- Platform: LeetCode
-- Date: 2026-09-01
-- Topic: WHERE / OR / Filtering

SELECT
    name,
    population,
    area
FROM World
WHERE area >= 3000000
   OR population >= 25000000;
