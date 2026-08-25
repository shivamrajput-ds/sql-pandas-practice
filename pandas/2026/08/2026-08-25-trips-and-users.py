"""
Problem: Trips and Users
Platform: LeetCode
Date: 2026-08-25
Topic: Merge / Filtering / GroupBy / Aggregation / Missing Values
"""

import pandas as pd


def trips_and_users(
    trips: pd.DataFrame,
    users: pd.DataFrame
) -> pd.DataFrame:

    trips = trips[
        (trips["request_at"] >= "2013-10-01")
        & (trips["request_at"] <= "2013-10-03")
    ]

    res = pd.merge(
        trips,
        users[["users_id", "banned"]],
        left_on="client_id",
        right_on="users_id",
        how="left"
    )

    res = pd.merge(
        res,
        users[["users_id", "banned"]],
        left_on="driver_id",
        right_on="users_id",
        how="left",
        suffixes=("_client", "_driver")
    )

    res = res[
        (res["banned_client"] == "No")
        & (res["banned_driver"] == "No")
    ]

    ans1 = (
        res.groupby("request_at")["id"]
        .count()
        .reset_index(name="total_request")
    )

    ans2 = (
        res[res["status"] != "completed"]
        .groupby("request_at")["id"]
        .count()
        .reset_index(name="cancelled_request")
    )

    data = pd.merge(
        ans1,
        ans2,
        on="request_at",
        how="left"
    )

    data["cancelled_request"] = data["cancelled_request"].fillna(0)

    data["Cancellation Rate"] = (
        data["cancelled_request"] / data["total_request"]
    ).round(2)

    data = data.rename(columns={"request_at": "Day"})

    return data[["Day", "Cancellation Rate"]]
