"""
Problem: Combine Two Tables
Platform: LeetCode
Date: 2026-08-14
Topic: Merge / Left Join
"""


import pandas as pd


def combine_two_tables(
    person: pd.DataFrame,
    address: pd.DataFrame
) -> pd.DataFrame:
    result = person.merge(
        address,
        how="left",
        on="personId"
    )

    return result[["firstName", "lastName", "city", "state"]]