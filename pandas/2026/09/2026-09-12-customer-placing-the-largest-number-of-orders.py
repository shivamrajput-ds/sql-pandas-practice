"""
Problem: Customer Placing the Largest Number of Orders
Platform: LeetCode
Date: 2026-09-12
Topic: groupby() / size() / max() / query() / Column Selection

Goal:
Return the customer_number of the customer(s)
who placed the largest number of orders.
"""

import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    cust_with_orders = (
        orders.groupby("customer_number")
        .size()
        .reset_index(name="no_of_orders")
    )

    max_orders = cust_with_orders["no_of_orders"].max()

    return (
        cust_with_orders
        .query("no_of_orders == @max_orders")[["customer_number"]]
    )
