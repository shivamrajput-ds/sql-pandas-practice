"""
Problem: Nth Highest Salary
Platform: LeetCode
Date: 2026-08-16
Topic: Drop Duplicates / Sorting / iloc / DataFrame Construction
"""


import pandas as pd


def nth_highest_salary(
    employee: pd.DataFrame,
    N: int
) -> pd.DataFrame:
    employee = employee.drop_duplicates(
        subset=["salary"]
    )

    employee = employee.sort_values(
        by="salary",
        ascending=False
    )

    employee = employee.reset_index(
        drop=True
    )

    if N <= 0 or N > len(employee):
        value = None
    else:
        value = employee["salary"].iloc[N - 1]

    return pd.DataFrame(
        [value],
        columns=[f"getNthHighestSalary({N})"]
    )