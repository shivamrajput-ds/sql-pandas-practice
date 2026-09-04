"""
Problem: Big Countries
Platform: LeetCode
Date: 2026-09-01
Topic: query() / Boolean Filtering / Column Selection
"""

import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world.query(
        "area >= 3000000 or population >= 25000000"
    )[["name", "population", "area"]]
