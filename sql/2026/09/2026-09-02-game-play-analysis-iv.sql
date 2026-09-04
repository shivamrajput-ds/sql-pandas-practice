-- Problem: Game Play Analysis IV
-- Platform: LeetCode
-- Date: 2026-09-02
-- Topic: CTE / GROUP BY / MIN / JOIN / DATEDIFF / Aggregation
--
-- Goal:
-- Find the fraction of players who logged in again exactly one day
-- after their first login, rounded to 2 decimal places.

;WITH first_login AS (
    SELECT
        player_id,
        MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
)

SELECT
    ROUND(
        1.0 * COUNT(DISTINCT a.player_id)
        / (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction
FROM Activity AS a
JOIN first_login AS f
    ON a.player_id = f.player_id
   AND DATEDIFF(DAY, f.first_login, a.event_date) = 1;
