"""
Problem: Duplicate Emails
Platform: LeetCode
Date: 2026-08-20
Topic: groupby() / size() / query() / rename()
"""

import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    email_counts = (
        person.groupby("email")
        .size()
        .reset_index(name="count")
    )

    return (
        email_counts.query("count > 1")[["email"]]
        .rename(columns={"email": "Email"})
    )


# Alternative approach learned during practice:
#
# def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
#     return (
#         person[person["email"].duplicated(keep=False)][["email"]]
#         .drop_duplicates()
#         .rename(columns={"email": "Email"})
#     )
