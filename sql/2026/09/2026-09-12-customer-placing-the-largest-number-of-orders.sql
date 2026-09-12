-- Problem: Customer Placing the Largest Number of Orders
-- Platform: LeetCode
-- Date: 2026-09-12
-- Topic: GROUP BY / COUNT / CTE / MAX / DENSE_RANK / Window Function
--
-- Goal:
-- Return the customer_number of the customer(s)
-- who placed the largest number of orders.


-- Approach 1: CTE + MAX()

WITH order_count AS (
    SELECT
        customer_number,
        COUNT(*) AS no_of_orders
    FROM Orders
    GROUP BY customer_number
)
SELECT
    customer_number
FROM order_count
WHERE no_of_orders = (
    SELECT
        MAX(no_of_orders)
    FROM order_count
);


-- Approach 2: DENSE_RANK()

WITH order_count AS (
    SELECT
        customer_number,
        COUNT(*) AS no_of_orders
    FROM Orders
    GROUP BY customer_number
)
SELECT
    customer_number
FROM (
    SELECT
        customer_number,
        no_of_orders,
        DENSE_RANK() OVER (
            ORDER BY no_of_orders DESC
        ) AS ranking
    FROM order_count
) AS t
WHERE ranking = 1;
