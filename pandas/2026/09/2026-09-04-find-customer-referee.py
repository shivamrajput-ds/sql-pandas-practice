"""
Problem: Find Customer Referee
Platform: LeetCode
Date: 2026-09-04
Topic: query() / NULL Filtering / Column Selection

Goal:
Return customers who were not referred by customer with id 2,
including customers whose referee_id is missing.
"""

import pandas as pd


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer.query(
        "referee_id.isnull() or referee_id != 2"
    )[["name"]]
