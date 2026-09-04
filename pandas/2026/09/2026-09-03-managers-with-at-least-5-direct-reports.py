"""
Problem: Managers with at Least 5 Direct Reports
Platform: LeetCode
Date: 2026-09-03
Topic: Self Merge / GroupBy / Count / query() / isin()

Goal:
Return the names of managers who have at least 5 direct reports.
"""

import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee[["id", "name", "managerId"]]

    df = pd.merge(
        employee,
        employee,
        left_on="id",
        right_on="managerId",
        how="inner"
    )

    df = (
        df.groupby("id_x")["id_x"]
        .count()
        .reset_index(name="count")
        .query("count >= 5")["id_x"]
    )

    return employee.loc[
        employee["id"].isin(df),
        ["name"]
    ]
