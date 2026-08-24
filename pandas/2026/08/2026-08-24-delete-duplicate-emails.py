"""
Problem: Delete Duplicate Emails
Platform: LeetCode
Date: 2026-08-24
Topic: Sorting / Duplicate Removal / In-place Modification
"""

import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(
        "id",
        ascending=True,
        inplace=True
    )

    person.drop_duplicates(
        subset=["email"],
        keep="first",
        inplace=True
    )
