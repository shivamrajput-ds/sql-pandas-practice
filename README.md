# SQL & Pandas Practice

![SQL](https://img.shields.io/badge/SQL-T--SQL-336791?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-Practice-150458?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![Focus](https://img.shields.io/badge/Focus-Depth%20over%20Volume-orange?style=flat-square)

A structured practice repository for strengthening **SQL and Pandas problem-solving skills** for **Data Science, Analytics, and technical interviews**.

The core workflow is simple:

> **Solve the data problem independently in SQL first, understand the pattern, explore another SQL approach only when it adds learning value, and then recreate the same or similar logic in Pandas.**

The goal is not to maximize the number of solved questions. The goal is to build enough depth to **recognize patterns, reason independently, handle edge cases, translate SQL logic into Pandas, and explain solutions clearly.**

---

## Current Progress

| Metric | Current Status |
| --- | --- |
| Practice started | 2026-08-14 |
| Latest entry | 2026-08-25 |
| Data problems completed | **12** |
| SQL solution files | **12** |
| Pandas recreation files | **12** |
| Primary SQL dialect | **Microsoft SQL Server / T-SQL** |
| Practice style | **1 data problem per day, depth-first** |

---

## Practice Method

```text
Understand the problem
        ↓
Solve independently in SQL
        ↓
Verify the result
        ↓
Check important edge cases
        ↓
Try another SQL approach — only if useful
        ↓
Recreate the logic in Pandas
        ↓
Compare SQL ↔ Pandas thinking
        ↓
Review mistakes / new concepts
        ↓
Commit to GitHub
```

### What "done" means

A problem is considered properly completed when I can:

- solve it without copying a memorized answer,
- explain why the approach works,
- recognize the reusable pattern,
- handle important edge cases,
- understand the equivalent Pandas operations,
- and reproduce the logic later with minimal help.

---

## Repository Structure

```text
sql-pandas-practice/
│
├── sql/
│   └── 2026/
│       └── 08/
│           ├── 2026-08-14-combine-two-tables.sql
│           ├── 2026-08-15-second-highest-salary.sql
│           ├── 2026-08-16-nth-highest-salary.sql
│           ├── 2026-08-17-rank-scores.sql
│           ├── 2026-08-18-consecutive-numbers.sql
│           ├── 2026-08-19-employees-earning-more-than-their-managers.sql
│           ├── 2026-08-20-duplicate-emails.sql
│           ├── 2026-08-21-customers-who-never-order.sql
│           ├── 2026-08-22-department-highest-salary.sql
│           ├── 2026-08-23-department-top-three-salaries.sql
│           ├── 2026-08-24-delete-duplicate-emails.sql
│           └── 2026-08-25-trips-and-users.sql
│
├── pandas/
│   └── 2026/
│       └── 08/
│           ├── 2026-08-14-combine-two-tables.py
│           ├── 2026-08-15-second-highest-salary.py
│           ├── 2026-08-16-nth-highest-salary.py
│           ├── 2026-08-17-rank-scores.py
│           ├── 2026-08-18-consecutive-numbers.py
│           ├── 2026-08-19-employees-earning-more-than-their-managers.py
│           ├── 2026-08-20-duplicate-emails.py
│           ├── 2026-08-21-customers-who-never-order.py
│           ├── 2026-08-22-department-highest-salary.py
│           ├── 2026-08-23-department-top-three-salaries.py
│           ├── 2026-08-24-delete-duplicate-emails.py
│           └── 2026-08-25-trips-and-users.py
│
└── README.md
```

### Naming Convention

```text
YYYY-MM-DD-problem-name.extension
```

Example:

```text
sql/2026/08/2026-08-25-trips-and-users.sql
pandas/2026/08/2026-08-25-trips-and-users.py
```

This keeps the repository chronological, searchable, and easy to scale over long-term practice.

---

## Practice Log

| Date | Problem | SQL Concepts | Pandas Concepts |
| --- | --- | --- | --- |
| 2026-08-14 | Combine Two Tables | `LEFT JOIN` | `merge()` |
| 2026-08-15 | Second Highest Salary | Subquery, aggregation, `DENSE_RANK()` | Filtering, `max()` |
| 2026-08-16 | Nth Highest Salary | Scalar function, `DENSE_RANK()` | `drop_duplicates()`, `sort_values()`, `iloc[]` |
| 2026-08-17 | Rank Scores | `DENSE_RANK()`, correlated subquery | `rank(method="dense")`, `sort_values()` |
| 2026-08-18 | Consecutive Numbers | `LEAD()`, `LAG()`, self join | `shift()`, boolean filtering, `unique()` |
| 2026-08-19 | Employees Earning More Than Their Managers | Self join, filtering | Self merge, `query()`, `to_frame()` |
| 2026-08-20 | Duplicate Emails | `GROUP BY`, `HAVING`, `COUNT()` | `groupby()`, `size()`, `duplicated()`, `drop_duplicates()` |
| 2026-08-21 | Customers Who Never Order | `LEFT JOIN`, anti-join, `IS NULL` | Left `merge()`, `isna()`, filtering, `rename()` |
| 2026-08-22 | Department Highest Salary | Join, `DENSE_RANK()`, `PARTITION BY` | `merge()`, `groupby()`, `max()`, merge-back |
| 2026-08-23 | Department Top Three Salaries | Join, `DENSE_RANK()`, partitioned ranking | `merge()`, `groupby()`, `rank(method="dense")`, filtering |
| 2026-08-24 | Delete Duplicate Emails | `ROW_NUMBER()`, subquery, CTE, `DELETE` | `sort_values()`, `drop_duplicates()`, in-place modification |
| 2026-08-25 | Trips and Users | CTE, double join, conditional aggregation, `CASE`, date filtering | Double `merge()`, filtering, `groupby()`, `fillna()`, rate calculation |

---

## Patterns Learned

This repository focuses on **reusable problem-solving patterns**, not isolated syntax.

| Pattern | SQL Thinking | Pandas Thinking |
| --- | --- | --- |
| Preserve every row from the left table | `LEFT JOIN` | `merge(..., how="left")` |
| Find unmatched rows | `LEFT JOIN` + `IS NULL` | Left merge + `isna()` |
| Match only common rows | `INNER JOIN` | `merge(..., how="inner")` |
| Compare rows in the same table | Self join | Self `merge()` |
| Join one lookup table for multiple roles | Join same table with separate aliases | Merge same DataFrame multiple times with suffixes |
| Detect duplicate values | `GROUP BY` + `HAVING COUNT(*) > 1` | `groupby()` / `duplicated()` |
| Aggregate by group | `GROUP BY` | `groupby()` |
| Filter aggregated results | `HAVING` | Aggregate, then filter |
| Compare adjacent rows | `LAG()` / `LEAD()` | `shift()` |
| Rank without gaps | `DENSE_RANK()` | `rank(method="dense")` |
| Rank with gaps | `RANK()` | `rank(method="min")` |
| Assign ordered row numbers | `ROW_NUMBER()` | Ordered `cumcount() + 1` |
| Find group maximum | `MAX()` / window function | `groupby().max()` |
| Keep rows matching a group maximum | Window rank / max comparison | Aggregate + merge back |
| Top-N distinct values per group | `DENSE_RANK()` + filter | Grouped dense rank + filter |
| Keep one row from each duplicate group | `ROW_NUMBER()` + keep rank 1 | Sort + `drop_duplicates(keep="first")` |
| Conditional counting | `SUM(CASE WHEN ... THEN 1 ELSE 0 END)` | Boolean filter + grouped count |
| Preserve zero-count groups | Conditional aggregation / outer join | Left merge + `fillna(0)` |
| Calculate ratios safely | Decimal conversion + division | Numeric division + `round()` |
| Remove duplicate rows | `DISTINCT` | `drop_duplicates()` |
| Handle missing values | `IS NULL` / `IS NOT NULL` | `isna()` / `notna()` |

---

## SQL ↔ Pandas Reference

| SQL | Pandas |
| --- | --- |
| `SELECT` | Column selection |
| `WHERE` | Boolean filtering / `.loc[]` |
| `ORDER BY` | `sort_values()` |
| `DISTINCT` | `drop_duplicates()` |
| `INNER JOIN` | `merge(how="inner")` |
| `LEFT JOIN` | `merge(how="left")` |
| `GROUP BY` | `groupby()` |
| `HAVING` | Aggregate first, then filter |
| `COUNT()` | `count()` / `size()` |
| `SUM()` | `sum()` |
| `AVG()` | `mean()` |
| `MAX()` | `max()` |
| `MIN()` | `min()` |
| `CASE WHEN` | Boolean masks / conditional assignment |
| `IS NULL` | `isna()` |
| `IS NOT NULL` | `notna()` |
| `DENSE_RANK()` | `rank(method="dense")` |
| `RANK()` | `rank(method="min")` |
| `ROW_NUMBER()` | Ordered `cumcount() + 1` |
| `LAG(column)` | `shift(1)` |
| `LEAD(column)` | `shift(-1)` |
| Self join | Self `merge()` |
| Multiple aliases of same table | Multiple merges + suffixes |
| Keep first row per group | `ROW_NUMBER()` + rank filter | Sort + `drop_duplicates(keep="first")` |
| Conditional aggregation | `SUM(CASE...)` | Filter / mask + grouped aggregation |
| Replace missing aggregate with zero | `COALESCE()` | `fillna(0)` |

The objective is **not** to force every SQL statement into a literal one-to-one Pandas translation.

The objective is to understand how the **same data requirement** can be expressed naturally in both tools.

---

## SQL Focus

Solutions are primarily written using **Microsoft SQL Server / T-SQL**.

### Core Querying

- `SELECT`
- `DISTINCT`
- `WHERE`
- `ORDER BY`
- aliases
- date filtering
- NULL handling

### Joins

- `INNER JOIN`
- `LEFT JOIN`
- `RIGHT JOIN`
- `FULL OUTER JOIN`
- self joins
- anti-join patterns
- multiple joins to the same lookup table

### Aggregation

- `COUNT()`
- `SUM()`
- `AVG()`
- `MAX()`
- `MIN()`
- `GROUP BY`
- `HAVING`
- conditional aggregation
- grouped ratios

### Intermediate / Advanced Querying

- subqueries
- correlated subqueries
- Common Table Expressions (CTEs)
- set operations
- `CASE`
- scalar functions
- `DELETE`

### Window Functions

- `ROW_NUMBER()`
- `RANK()`
- `DENSE_RANK()`
- `LAG()`
- `LEAD()`
- partitioned calculations

### Future Depth

- indexes
- query execution
- execution plans
- query optimization
- performance trade-offs

---

## Pandas Focus

Pandas practice develops the ability to translate tabular requirements into readable DataFrame operations.

### Selection and Filtering

- column selection
- boolean masks
- `.loc[]`
- `.iloc[]`
- `query()`
- date-range filtering

### Combining Data

- `merge()`
- left / inner merge patterns
- self merge
- repeated merges against the same lookup DataFrame
- suffix handling
- merge-back patterns

### Grouping and Aggregation

- `groupby()`
- `size()`
- `count()`
- `sum()`
- `mean()`
- `min()`
- `max()`
- ratio calculations

### Ranking and Row Relationships

- `rank()`
- `shift()`
- `cumcount()`
- grouped ranking
- window-like operations

### Data Quality and Transformation

- `duplicated()`
- `drop_duplicates()`
- `isna()`
- `notna()`
- `fillna()`
- `rename()`
- `to_frame()`
- `sort_values()`
- in-place modification
- reshaping
- string operations
- date/time operations
- feature creation

Pandas methods are learned **when a problem naturally requires them**, rather than being memorized in isolation.

---

## Solution Standards

Every solution should be:

- **independently reasoned**
- **correct for the required output**
- **readable**
- **properly formatted**
- **easy to explain**
- **aware of important edge cases**
- **free from unnecessary complexity**

Multiple SQL approaches are included **only when the alternative teaches a useful pattern or trade-off**.

### Example: SQL

```sql
-- Problem: Trips and Users
-- Platform: LeetCode
-- Date: 2026-08-25
-- Topic: CTE / JOIN / Conditional Aggregation / CASE / GROUP BY

;WITH table1 AS (
    SELECT
        t.request_at AS [Day],
        COUNT(*) AS unbanned_req,
        SUM(
            CASE
                WHEN t.status <> 'completed' THEN 1
                ELSE 0
            END
        ) AS cancelled_req
    FROM Trips AS t
    LEFT JOIN Users AS c
        ON t.client_id = c.users_id
    LEFT JOIN Users AS d
        ON t.driver_id = d.users_id
    WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
      AND c.banned = 'No'
      AND d.banned = 'No'
    GROUP BY t.request_at
)

SELECT
    [Day],
    ROUND(
        1.0 * cancelled_req / unbanned_req,
        2
    ) AS [Cancellation Rate]
FROM table1;
```

### Example: Pandas

```python
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
```

---

## Edge-Case Checklist

Before considering a solution complete, I check cases such as:

- empty input or empty result,
- duplicate values,
- ties in ranking problems,
- `NULL` values in SQL,
- `NaN` values in Pandas,
- missing join matches,
- groups with a single row,
- multiple rows sharing the same maximum or minimum,
- fewer than N values in Top-N problems,
- duplicate groups where only the minimum `id` should survive,
- days or groups with zero matching events,
- integer division when a decimal result is required,
- filters that return no rows.

### Example: Missing aggregate rows

A useful lesson from cancellation-rate style problems:

```text
A day can have valid trips
but zero cancelled trips.
```

If the cancelled subset is grouped separately, that day may disappear completely.

In Pandas:

```python
left_merge + fillna(0)
```

can preserve the day and restore the missing cancellation count as zero.

In SQL, conditional aggregation can avoid creating a separate missing group in the first place.

### Example: Empty aggregate behavior

```text
Normal SELECT with no matching rows
→ zero rows

MAX() over no matching rows
→ one row containing NULL
```

Pandas equivalent:

```python
empty_series.max()
```

returns:

```text
NaN
```

Knowing these behaviors is part of understanding the problem.

---

## Code Quality Principles

### SQL

- Uppercase SQL keywords
- Consistent indentation
- Meaningful aliases
- Explicit join conditions
- Readable window functions
- Clear conditional aggregation
- Semicolons at statement boundaries
- Clear approach labels when multiple solutions are useful
- Readability over clever but unnecessary compression

### Python / Pandas

- PEP 8-style formatting
- Meaningful variable names
- Type hints where useful
- Readable transformations
- Minimal unnecessary comments
- Avoid overly complex one-liners
- Prefer code that can be clearly explained in an interview

---

## Learning Goals

This repository is intended to strengthen my ability to:

- translate business and data requirements into queries,
- write SQL independently,
- recognize reusable SQL patterns,
- choose the correct join or aggregation strategy,
- use window functions confidently,
- use conditional aggregation correctly,
- handle duplicates and missing data,
- reason about zero-count and empty-result cases,
- manipulate DataFrames confidently,
- translate SQL logic into Pandas,
- compare multiple valid approaches when useful,
- write maintainable data code,
- and explain my reasoning clearly in technical interviews.

---

## Practice Philosophy

This repository follows a **depth-over-volume** approach.

```text
One Data Problem
      ↓
Independent SQL Solution
      ↓
Correctness + Edge Cases
      ↓
Useful Alternative — if any
      ↓
Pandas Recreation
      ↓
SQL ↔ Pandas Mapping
      ↓
Pattern Recognition
      ↓
Stronger Problem Solving
```

A problem is valuable not because it increases a solved-question counter, but because it makes the **next unfamiliar problem easier to solve independently**.

---

## Core Principle

> **Understand the data. Build the logic. Verify the result. Explore useful alternatives. Handle edge cases. Translate the pattern. Learn from mistakes. Repeat consistently.**

This repository is a long-term record of continuous improvement in **SQL, Pandas, and practical data problem solving**.
