"""
Problem: Game Play Analysis IV
Platform: LeetCode
Date: 2026-09-02
Topic: GroupBy / Min / Merge / Timedelta / nunique / Boolean Mask

Goal:
Find the fraction of players who logged in again exactly one day
after their first login, rounded to 2 decimal places.
"""

import pandas as pd


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    total = activity["player_id"].nunique()

    df1 = (
        activity.groupby("player_id")["event_date"]
        .min()
        .reset_index()
        .rename(columns={"event_date": "first_login"})
    )

    df2 = pd.merge(
        activity,
        df1,
        how="left",
        on="player_id"
    )[["player_id", "event_date", "first_login"]]

    mask = (
        df2["event_date"] - df2["first_login"]
        == pd.Timedelta(days=1)
    )

    res = pd.DataFrame({
        "fraction": [round(mask.sum() / total, 2)]
    })

    return res
