"""
Problem: Game Play Analysis I
Platform: LeetCode
Date: 2026-08-26
Topic: GroupBy / Min / Sorting / CumCount

Goal:
Find the first login date for each player.
"""

import pandas as pd


# Approach 1: groupby() + min()

def game_analysis_groupby(activity: pd.DataFrame) -> pd.DataFrame:
    res = activity.groupby("player_id")["event_date"].min()
    res = res.reset_index()
    res = res.rename(columns={"event_date": "first_login"})

    return res


# Approach 2: sort_values() + groupby().cumcount()

def game_analysis_row_number(activity: pd.DataFrame) -> pd.DataFrame:
    res = activity.sort_values(["player_id", "event_date"])

    res["rank"] = (
        res.groupby("player_id").cumcount() + 1
    )

    res = res[res["rank"] == 1]
    res = res[["player_id", "event_date"]]
    res = res.rename(columns={"event_date": "first_login"})

    return res
