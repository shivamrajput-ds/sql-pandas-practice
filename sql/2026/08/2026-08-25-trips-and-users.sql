-- Problem: Trips and Users
-- Platform: LeetCode
-- Date: 2026-08-25
-- Topic: CTE / JOIN / Conditional Aggregation / CASE / GROUP BY

;WITH table1 AS (
    SELECT
        t.request_at AS [Day],
        COUNT(*) AS unbanned_req,
        SUM(
            CASE
                WHEN t.status <> 'completed' THEN 1
                ELSE 0
            END
        ) AS cancelled_req
    FROM Trips AS t
    LEFT JOIN Users AS c
        ON t.client_id = c.users_id
    LEFT JOIN Users AS d
        ON t.driver_id = d.users_id
    WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
      AND c.banned = 'No'
      AND d.banned = 'No'
    GROUP BY t.request_at
)

SELECT
    [Day],
    ROUND(
        1.0 * cancelled_req / unbanned_req,
        2
    ) AS [Cancellation Rate]
FROM table1;
