/*
Problem: Rank Scores
Platform: LeetCode
Date: 2026-08-17
Topic: DENSE_RANK / Window Function / Correlated Subquery
*/

-- Approach 1: DENSE_RANK
SELECT
    score,
    DENSE_RANK() OVER (
        ORDER BY score DESC
    ) AS rank
FROM Scores;


-- Approach 2: Correlated Subquery
SELECT
    s1.score,
    (
        SELECT COUNT(DISTINCT s2.score)
        FROM Scores AS s2
        WHERE s2.score >= s1.score
    ) AS rank
FROM Scores AS s1
ORDER BY s1.score DESC;