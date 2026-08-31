"""
Problem: Rising Temperature

Platform: LeetCode

Date: 2026-08-31

Topic: Sort Values / Shift / Timedelta / Boolean Filtering

Goal:

Find all ids where the temperature is higher than the previous calendar day.
"""

import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values("recordDate")

    weather["prev_date"] = weather["recordDate"].shift(1)
    weather["prev_temp"] = weather["temperature"].shift(1)

    mask = (
        (weather["recordDate"] - weather["prev_date"] == pd.Timedelta(days=1))
        & (weather["temperature"] > weather["prev_temp"])
    )

    return weather.loc[mask, ["id"]]