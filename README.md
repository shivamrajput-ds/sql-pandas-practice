# SQL & Pandas Practice

![SQL](https://img.shields.io/badge/SQL-T--SQL-336791?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-Practice-150458?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![Focus](https://img.shields.io/badge/Focus-Depth%20over%20Volume-orange?style=flat-square)

A structured practice repository for building strong **SQL + Pandas problem-solving skills** for **Data Science, Analytics, and technical interviews**.

The repository follows one simple rule:

> **Solve the data problem independently in SQL first, understand the pattern, explore another SQL approach only when it adds learning value, then recreate the same or similar logic in Pandas.**

The focus is not on collecting solved-question counts.  
The focus is on becoming able to **recognize patterns, build the logic independently, handle edge cases, translate between SQL and Pandas, and explain the solution clearly.**

---

## Current Progress

| Metric | Current Status |
| --- | --- |
| Practice started | 2026-08-14 |
| Latest entry | 2026-08-23 |
| Data problems completed | **10** |
| SQL solutions | **10** |
| Pandas recreations | **10** |
| Primary SQL dialect | **Microsoft SQL Server / T-SQL** |
| Practice style | **1 problem per day, depth-first** |

---

## Practice Method

Each practice session follows this workflow:

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
- identify the underlying pattern,
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
│           └── 2026-08-23-department-top-three-salaries.sql
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
│           └── 2026-08-23-department-top-three-salaries.py
│
└── README.md
```

### Naming convention

```text
YYYY-MM-DD-problem-name.extension
```

Example:

```text
sql/2026/08/2026-08-23-department-top-three-salaries.sql
pandas/2026/08/2026-08-23-department-top-three-salaries.py
```

This structure keeps the repository chronological, searchable, and easy to scale over long-term practice.

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

---

## Patterns Learned

The repository is organized around **reusable data patterns**, not isolated syntax.

| Pattern | SQL Thinking | Pandas Thinking |
| --- | --- | --- |
| Preserve every row from the left table | `LEFT JOIN` | `merge(..., how="left")` |
| Find unmatched rows | `LEFT JOIN` + `IS NULL` | Left merge + `isna()` |
| Match only common rows | `INNER JOIN` | `merge(..., how="inner")` |
| Compare rows in the same table | Self join | Self `merge()` |
| Detect duplicate values | `GROUP BY` + `HAVING COUNT(*) > 1` | `groupby()` / `duplicated()` |
| Aggregate by group | `GROUP BY` | `groupby()` |
| Filter aggregated results | `HAVING` | Aggregate, then filter |
| Compare adjacent rows | `LAG()` / `LEAD()` | `shift()` |
| Rank without gaps | `DENSE_RANK()` | `rank(method="dense")` |
| Rank with gaps | `RANK()` | `rank(method="min")` |
| Assign ordered row numbers | `ROW_NUMBER()` | Ordered `groupby().cumcount() + 1` |
| Find group maximum | `MAX()` / window function | `groupby().max()` |
| Keep rows matching a group maximum | Window rank / max comparison | Aggregate + merge back |
| Top-N distinct values per group | `DENSE_RANK()` + filter | Grouped dense rank + filter |
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
| `CASE WHEN` | Conditional assignment / masking |
| `IS NULL` | `isna()` |
| `IS NOT NULL` | `notna()` |
| `DENSE_RANK()` | `rank(method="dense")` |
| `RANK()` | `rank(method="min")` |
| `ROW_NUMBER()` | `cumcount() + 1` after ordering |
| `LAG(column)` | `shift(1)` |
| `LEAD(column)` | `shift(-1)` |
| Self join | Self `merge()` |

The goal is **not** to force every SQL statement into a literal one-to-one Pandas translation.  
The goal is to understand how the **same data requirement** can be expressed naturally in both tools.

---

## SQL Focus

Solutions are primarily written using **Microsoft SQL Server / T-SQL**.

Current and planned coverage includes:

### Core querying
- `SELECT`
- `DISTINCT`
- `WHERE`
- `ORDER BY`
- aliases
- NULL handling

### Joins
- `INNER JOIN`
- `LEFT JOIN`
- `RIGHT JOIN`
- `FULL OUTER JOIN`
- self joins
- anti-join patterns

### Aggregation
- `COUNT()`
- `SUM()`
- `AVG()`
- `MAX()`
- `MIN()`
- `GROUP BY`
- `HAVING`
- conditional aggregation

### Intermediate / advanced querying
- subqueries
- correlated subqueries
- CTEs
- set operations
- `CASE`
- scalar functions

### Window functions
- `ROW_NUMBER()`
- `RANK()`
- `DENSE_RANK()`
- `LAG()`
- `LEAD()`
- partitioned calculations

### Future depth
- indexes
- query execution
- execution plans
- query optimization
- performance trade-offs

---

## Pandas Focus

Pandas practice develops the ability to translate tabular requirements into readable DataFrame operations.

Current and planned coverage includes:

### Selection and filtering
- column selection
- boolean masks
- `.loc[]`
- `.iloc[]`
- `query()`

### Combining data
- `merge()`
- left / inner merge patterns
- self merge
- merge-back patterns

### Grouping and aggregation
- `groupby()`
- `size()`
- `count()`
- `sum()`
- `mean()`
- `min()`
- `max()`

### Ranking and row relationships
- `rank()`
- `shift()`
- `cumcount()`
- grouped ranking
- window-like operations

### Data quality and reshaping
- `duplicated()`
- `drop_duplicates()`
- `isna()`
- `notna()`
- `rename()`
- `to_frame()`
- sorting
- reshaping
- string operations
- date/time operations
- feature creation

Pandas methods are learned **when a problem naturally requires them**, instead of being memorized in isolation.

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

### SQL file style

```sql
-- Problem: Department Top Three Salaries
-- Platform: LeetCode
-- Date: 2026-08-23
-- Topic: JOIN / DENSE_RANK / PARTITION BY

SELECT
    Department,
    Employee,
    Salary
FROM (
    SELECT
        DENSE_RANK() OVER (
            PARTITION BY d.name
            ORDER BY e.salary DESC
        ) AS rnk,
        e.name AS Employee,
        e.salary AS Salary,
        d.name AS Department
    FROM Employee AS e
    JOIN Department AS d
        ON e.departmentId = d.id
) AS ranked
WHERE rnk <= 3;
```

### Pandas file style

```python
"""
Problem: Department Top Three Salaries
Platform: LeetCode
Date: 2026-08-23
Topic: Merge / GroupBy / Dense Rank / Filtering
"""

import pandas as pd


def top_three_salaries(
    employee: pd.DataFrame,
    department: pd.DataFrame
) -> pd.DataFrame:

    merged = employee.merge(
        department,
        left_on="departmentId",
        right_on="id",
        how="inner"
    )

    merged["rank"] = (
        merged.groupby("name_y")["salary"]
        .rank(method="dense", ascending=False)
    )

    result = merged.loc[
        merged["rank"] <= 3,
        ["name_y", "name_x", "salary"]
    ].copy()

    result.columns = ["Department", "Employee", "Salary"]

    return result
```

Multiple SQL approaches are included **only when the alternative teaches a useful pattern or trade-off**.

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
- filters that return no rows.

Example:

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
- Semicolons at the end of queries
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

- translate business/data requirements into queries,
- write SQL independently,
- recognize reusable SQL patterns,
- choose the correct join or aggregation strategy,
- use window functions confidently,
- handle duplicates and missing data correctly,
- reason about edge cases,
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

A problem is valuable not because it increases a counter, but because it makes the **next unfamiliar problem easier to solve independently**.

---

## Core Principle

> **Understand the data. Build the logic. Verify the result. Explore useful alternatives. Handle edge cases. Translate the pattern. Learn from mistakes. Repeat consistently.**

This repository is a long-term record of continuous improvement in **SQL, Pandas, and practical data problem solving**.
