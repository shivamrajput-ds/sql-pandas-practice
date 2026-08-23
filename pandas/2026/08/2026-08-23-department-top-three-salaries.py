"""
Problem: Department Top Three Salaries
Platform: LeetCode
Date: 2026-08-23
Topic: Merge / GroupBy / Dense Rank / Filtering
"""

import pandas as pd


def top_three_salaries(
    employee: pd.DataFrame,
    department: pd.DataFrame
) -> pd.DataFrame:

    merged = employee.merge(
        department,
        left_on="departmentId",
        right_on="id",
        how="inner"
    )

    merged["rnk"] = (
        merged.groupby("name_y")["salary"]
        .rank(method="dense", ascending=False)
    )

    result = merged.loc[
        merged["rnk"] <= 3,
        ["name_y", "name_x", "salary"]
    ].copy()

    result.columns = ["Department", "Employee", "Salary"]

    return result
