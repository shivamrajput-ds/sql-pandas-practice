"""
Problem: Consecutive Numbers
Platform: LeetCode
Date: 2026-08-18
Topic: shift() / Boolean Filtering / unique() / DataFrame Construction
"""

import pandas as pd


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs["prev_num"] = logs["num"].shift(1)
    logs["next_num"] = logs["num"].shift(-1)

    data = logs[
        (logs["num"] == logs["prev_num"])
        & (logs["num"] == logs["next_num"])
    ]["num"].unique()

    return pd.DataFrame(
        data,
        columns=["ConsecutiveNums"]
    )
