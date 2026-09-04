"""
Problem: Employee Bonus
Platform: LeetCode
Date: 2026-09-04
Topic: merge() / isna() / Boolean Mask / Column Selection

Goal:
Return employees whose bonus is less than 1000
or who do not have a bonus record.
"""

import pandas as pd


def employee_bonus(
    employee: pd.DataFrame,
    bonus: pd.DataFrame
) -> pd.DataFrame:
    df = pd.merge(
        employee,
        bonus,
        on="empId",
        how="left"
    )

    mask = df["bonus"].isna() | (df["bonus"] < 1000)

    return df.loc[mask, ["name", "bonus"]]
