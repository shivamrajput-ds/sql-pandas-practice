# LeetCode 184: Department Highest Salary
# Date: 2026-08-22
#
# Approach:
# 1. Merge Employee and Department DataFrames.
# 2. Find the maximum salary for each department using groupby().
# 3. Merge the maximum salaries back with the joined DataFrame.
# 4. Select and rename the required output columns.
#
# Time Complexity: O(n) average for grouping and merging
# Space Complexity: O(n)

import pandas as pd


def department_highest_salary(
    employee: pd.DataFrame,
    department: pd.DataFrame
) -> pd.DataFrame:

    # Join employee data with department data
    df1 = pd.merge(
        employee,
        department,
        left_on="departmentId",
        right_on="id",
        how="inner"
    )

    # Find the highest salary in each department
    df2 = (
        df1.groupby("name_y")["salary"]
        .max()
        .reset_index()
    )

    # Keep employees whose salary is the maximum in their department
    res = pd.merge(
        df1,
        df2,
        on=["name_y", "salary"],
        how="inner"
    )[["name_y", "name_x", "salary"]]

    # Rename columns according to the required output
    res.columns = ["Department", "Employee", "Salary"]

    return res
