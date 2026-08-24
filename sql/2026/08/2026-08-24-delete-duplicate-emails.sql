-- Problem: Delete Duplicate Emails
-- Platform: LeetCode
-- Date: 2026-08-24

-- Approach 1: Subquery + ROW_NUMBER()
DELETE
FROM Person
WHERE id NOT IN (
    SELECT id
    FROM (
        SELECT
            id,
            email,
            ROW_NUMBER() OVER (
                PARTITION BY email
                ORDER BY id ASC
            ) AS rnk
        FROM Person
    ) AS ranked_person
    WHERE rnk = 1
);

-- =======================================================

-- Approach 2: CTE + ROW_NUMBER()
WITH ranked_person AS (
    SELECT
        id,
        email,
        ROW_NUMBER() OVER (
            PARTITION BY email
            ORDER BY id ASC
        ) AS rnk
    FROM Person
)
DELETE
FROM Person
WHERE id NOT IN (
    SELECT id
    FROM ranked_person
    WHERE rnk = 1
);