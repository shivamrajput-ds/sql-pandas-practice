"""
Problem: Employees Earning More Than Their Managers
Platform: LeetCode
Date: 2026-08-19
Topic: Self Merge / query() / to_frame()
"""

import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(
        employee,
        employee,
        left_on="managerId",
        right_on="id",
        suffixes=("_employee", "_manager")
    )

    df = df.query(
        "salary_employee > salary_manager"
    )

    return df["name_employee"].to_frame(
        name="Employee"
    )
