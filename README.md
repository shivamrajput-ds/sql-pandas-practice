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
| Latest entry | 2026-08-24 |
| Data problems completed | **11** |
| SQL solution files | **11** |
| Pandas recreation files | **11** |
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
│           └── 2026-08-24-delete-duplicate-emails.sql
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
│           └── 2026-08-24-delete-duplicate-emails.py
│
└── README.md
```

### Naming Convention

```text
YYYY-MM-DD-problem-name.extension
```

Example:

```text
sql/2026/08/2026-08-24-delete-duplicate-emails.sql
pandas/2026/08/2026-08-24-delete-duplicate-emails.py
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

---

## Patterns Learned

This repository focuses on **reusable problem-solving patterns**, not isolated syntax.

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
| Assign ordered row numbers | `ROW_NUMBER()` | Ordered `cumcount() + 1` |
| Find group maximum | `MAX()` / window function | `groupby().max()` |
| Keep rows matching a group maximum | Window rank / max comparison | Aggregate + merge back |
| Top-N distinct values per group | `DENSE_RANK()` + filter | Grouped dense rank + filter |
| Keep one row from each duplicate group | `ROW_NUMBER()` + keep rank 1 | Sort + `drop_duplicates(keep="first")` |
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
| `ROW_NUMBER()` | Ordered `cumcount() + 1` |
| `LAG(column)` | `shift(1)` |
| `LEAD(column)` | `shift(-1)` |
| Self join | Self `merge()` |
| Keep first row per group | `ROW_NUMBER()` + rank filter | Sort + `drop_duplicates(keep="first")` |

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

### Combining Data

- `merge()`
- left / inner merge patterns
- self merge
- merge-back patterns

### Grouping and Aggregation

- `groupby()`
- `size()`
- `count()`
- `sum()`
- `mean()`
- `min()`
- `max()`

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
-- Problem: Delete Duplicate Emails
-- Platform: LeetCode
-- Date: 2026-08-24
-- Topic: ROW_NUMBER / Subquery / CTE / DELETE

-- Approach 1: Subquery + ROW_NUMBER()

DELETE
FROM Person
WHERE id NOT IN (
    SELECT id
    FROM (
        SELECT
            id,
            email,
            ROW_NUMBER() OVER (
                PARTITION BY email
                ORDER BY id ASC
            ) AS rnk
        FROM Person
    ) AS ranked_person
    WHERE rnk = 1
);


-- Approach 2: CTE + ROW_NUMBER()

WITH ranked_person AS (
    SELECT
        id,
        email,
        ROW_NUMBER() OVER (
            PARTITION BY email
            ORDER BY id ASC
        ) AS rnk
    FROM Person
)
DELETE
FROM Person
WHERE id NOT IN (
    SELECT id
    FROM ranked_person
    WHERE rnk = 1
);
```

### Example: Pandas

```python
"""
Problem: Delete Duplicate Emails
Platform: LeetCode
Date: 2026-08-24
Topic: Sorting / Duplicate Removal / In-place Modification
"""

import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(
        "id",
        ascending=True,
        inplace=True
    )

    person.drop_duplicates(
        subset=["email"],
        keep="first",
        inplace=True
    )
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

A problem is valuable not because it increases a solved-question counter, but because it makes the **next unfamiliar problem easier to solve independently**.

---

## Core Principle

> **Understand the data. Build the logic. Verify the result. Explore useful alternatives. Handle edge cases. Translate the pattern. Learn from mistakes. Repeat consistently.**

This repository is a long-term record of continuous improvement in **SQL, Pandas, and practical data problem solving**.
