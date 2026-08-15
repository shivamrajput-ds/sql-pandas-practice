"""
Problem: Second Highest Salary
Platform: LeetCode
Date: 2026-08-15
Topic: Filtering / Aggregation
"""


import pandas as pd


def second_highest_salary(
    employee: pd.DataFrame
) -> pd.DataFrame:
    max_salary = employee["salary"].max()

    filtered_employee = employee[
        employee["salary"] < max_salary
    ]

    second_salary = filtered_employee["salary"].max()

    return pd.DataFrame(
        [second_salary],
        columns=["SecondHighestSalary"]
    )