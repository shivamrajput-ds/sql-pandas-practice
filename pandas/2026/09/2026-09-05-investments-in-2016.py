"""
Problem: Investments in 2016
Platform: LeetCode
Date: 2026-09-05
Topic: groupby() / size() / query() / isin() / zip() / Boolean Mask

Goal:
Sum tiv_2016 for policyholders who:
1. share the same tiv_2015 with at least one other policyholder, and
2. have a unique (lat, lon) location.
Round the result to 2 decimal places.
"""

import pandas as pd


def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    res1 = (
        insurance.groupby("tiv_2015")
        .size()
        .reset_index(name="count")
        .query("count > 1")["tiv_2015"]
    )

    condition1 = insurance["tiv_2015"].isin(res1)

    res2 = (
        insurance.groupby(["lat", "lon"])
        .size()
        .reset_index(name="count")
        .query("count == 1")
    )

    unique_pairs = list(zip(res2["lat"], res2["lon"]))
    insurance_pairs = list(zip(insurance["lat"], insurance["lon"]))

    condition2 = pd.Series(
        insurance_pairs,
        index=insurance.index
    ).isin(unique_pairs)

    mask = condition1 & condition2

    total = round(
        insurance.loc[mask, "tiv_2016"].sum(),
        2
    )

    return pd.DataFrame({
        "tiv_2016": [total]
    })
