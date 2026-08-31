/*
Problem: Rising Temperature

Platform: LeetCode

Date: 2026-08-31

Topic: Self Join / DATEDIFF / LAG / Window Functions

Goal:

Find all ids where the temperature is higher than the previous calendar day.
*/

-- Approach 1: Self Join + DATEDIFF

SELECT
    w2.id
FROM Weather w1
JOIN Weather w2
    ON DATEDIFF(day, w1.recordDate, w2.recordDate) = 1
WHERE w2.temperature > w1.temperature;


-- Approach 2: LAG + DATEDIFF

SELECT
    id
FROM (
    SELECT
        id,
        recordDate AS curr_date,
        LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date,
        LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
        temperature AS curr_temp
    FROM Weather
) t
WHERE DATEDIFF(day, prev_date, curr_date) = 1
  AND curr_temp > prev_temp;