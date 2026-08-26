-- Problem: Game Play Analysis I
-- Platform: LeetCode
-- Date: 2026-08-26
-- Topic: GROUP BY / MIN / ROW_NUMBER / Window Function
--
-- Goal:
-- Find the first login date for each player.


-- Approach 1: GROUP BY + MIN()

SELECT
    player_id,
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;


-- Approach 2: ROW_NUMBER()

SELECT
    player_id,
    event_date AS first_login
FROM (
    SELECT
        player_id,
        ROW_NUMBER() OVER (
            PARTITION BY player_id
            ORDER BY event_date ASC
        ) AS rnk,
        event_date
    FROM Activity
) AS t
WHERE rnk = 1;
