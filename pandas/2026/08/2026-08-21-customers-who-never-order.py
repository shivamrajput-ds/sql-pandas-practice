"""
Problem: Customers Who Never Order
Platform: LeetCode
Date: 2026-08-21
Topic: Left Merge / query() / isna() / rename()
"""

import pandas as pd


def find_customers(
    customers: pd.DataFrame,
    orders: pd.DataFrame
) -> pd.DataFrame:
    return (
        pd.merge(
            customers,
            orders,
            left_on="id",
            right_on="customerId",
            how="left"
        )
        .query("id_y.isna()")
        [["name"]]
        .rename(columns={"name": "Customers"})
    )
