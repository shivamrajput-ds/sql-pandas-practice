# SQL & Pandas Practice

A structured, long-term practice repository focused on strengthening **SQL and Pandas problem-solving skills for Data Science, Analytics, and technical interviews**.

The core workflow is simple:

> **Solve the data problem in SQL, understand the logic deeply, explore alternative SQL approaches when useful, and recreate the same or similar operation in Pandas whenever it adds learning value.**

This repository emphasizes **clean code, strong fundamentals, interview-oriented problem solving, edge-case awareness, SQL ↔ Pandas translation, and consistent practice**.

---

## Tech Stack

- **Microsoft SQL Server / T-SQL**
- **Python 3**
- **Pandas**
- **SQL Server Management Studio (SSMS)**
- **Google Colab / Jupyter Notebook**

---

## Practice Routine

My regular practice focuses on:

- **1 SQL problem per day**
- Solving the SQL problem independently first
- Understanding the underlying pattern instead of memorizing syntax
- Exploring a second SQL approach when it provides useful learning
- Recreating the same or similar problem in Pandas
- Comparing equivalent SQL and Pandas operations
- Testing important edge cases
- Reviewing mistakes and new concepts
- Keeping solutions clean and interview-explainable

A typical session looks like:

```text
1 SQL Problem
      ↓
Solve Independently
      ↓
Verify Result
      ↓
Alternative SQL Approach — if useful
      ↓
Check Edge Cases
      ↓
Pandas Recreation
      ↓
Compare SQL ↔ Pandas Logic
      ↓
Review New Concepts
      ↓
Commit Solution
```

The goal is **not to solve the maximum number of questions**.

The goal is to understand each problem well enough to:

- reproduce the solution independently,
- explain the logic clearly,
- recognize the underlying pattern,
- handle edge cases,
- and apply the same idea to future problems.

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
│           └── 2026-08-22-department-highest-salary.sql
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
│           └── 2026-08-22-department-highest-salary.py
│
└── README.md
```

Problems are organized as:

```text
Technology → Year → Month → Problem
```

---

## File Naming Convention

```text
YYYY-MM-DD-problem-name.extension
```

Examples:

```text
sql/2026/08/2026-08-22-department-highest-salary.sql
pandas/2026/08/2026-08-22-department-highest-salary.py
```

This keeps the repository easy to navigate as the number of solved problems grows over time.

---

## Recent Practice

| Date | Problem | SQL Concepts | Pandas Concepts |
| --- | --- | --- | --- |
| 2026-08-14 | Combine Two Tables | `LEFT JOIN` | `merge()` |
| 2026-08-15 | Second Highest Salary | Subquery, `DENSE_RANK()` | Filtering, `max()` |
| 2026-08-16 | Nth Highest Salary | Scalar function, `DENSE_RANK()` | `drop_duplicates()`, `sort_values()`, `iloc[]` |
| 2026-08-17 | Rank Scores | `DENSE_RANK()`, correlated subquery | `rank(method="dense")`, `sort_values()` |
| 2026-08-18 | Consecutive Numbers | `LEAD()`, `LAG()`, self join | `shift()`, boolean filtering, `unique()` |
| 2026-08-19 | Employees Earning More Than Their Managers | Self join, filtering | Self merge, `query()`, `to_frame()` |
| 2026-08-20 | Duplicate Emails | `GROUP BY`, `HAVING`, `COUNT()` | `groupby()`, `size()`, `duplicated()`, `drop_duplicates()` |
| 2026-08-21 | Customers Who Never Order | `LEFT JOIN`, anti-join pattern, `IS NULL` | `merge(how="left")`, `isna()`, filtering, `rename()` |
| 2026-08-22 | Department Highest Salary | `JOIN`, `DENSE_RANK()`, `PARTITION BY` | `merge()`, `groupby()`, `max()`, merge-back pattern |

---

## SQL Focus

SQL solutions are primarily written using **Microsoft SQL Server / T-SQL syntax**.

Topics include:

- `SELECT`
- `DISTINCT`
- `WHERE`
- `ORDER BY`
- Aggregate functions
- `GROUP BY`
- `HAVING`
- `INNER JOIN`
- `LEFT JOIN`
- `RIGHT JOIN`
- `FULL OUTER JOIN`
- Self joins
- Subqueries
- Common Table Expressions (CTEs)
- Set operations
- `CASE`
- Window functions
- `ROW_NUMBER()`
- `RANK()`
- `DENSE_RANK()`
- `LEAD()`
- `LAG()`
- Date functions
- String functions
- NULL handling
- Duplicate detection
- Conditional aggregation

As practice progresses, I also aim to strengthen my understanding of:

- indexes,
- query execution,
- query optimization,
- and SQL Server execution plans.

---

## Pandas Focus

Pandas practice focuses on translating data manipulation requirements into clear Python operations.

Topics include:

- DataFrame selection
- Boolean filtering
- `merge()`
- Self merge / self join patterns
- `query()`
- `groupby()`
- `size()` / `count()`
- Aggregations
- `sort_values()`
- `drop_duplicates()`
- `duplicated()`
- `rename()`
- `isna()` / `notna()`
- Missing value handling
- Conditional transformations
- String operations
- Date/time operations
- Ranking
- Window-like operations
- `shift()`
- Reshaping
- Data cleaning
- Feature creation
- `.loc[]`
- `.iloc[]`
- `to_frame()`

Pandas concepts are learned primarily **through problems when they naturally become useful**, rather than by memorizing methods in isolation.

---

## SQL ↔ Pandas Mapping

One major objective of this repository is to build a strong connection between SQL operations and their Pandas equivalents.

| SQL | Pandas |
| --- | --- |
| `SELECT` | Column selection |
| `WHERE` | Boolean filtering |
| `LEFT JOIN` | `merge(how="left")` |
| `INNER JOIN` | `merge(how="inner")` |
| `GROUP BY` | `groupby()` |
| `HAVING` | Aggregate first, then filter |
| `ORDER BY` | `sort_values()` |
| `DISTINCT` | `drop_duplicates()` |
| `COUNT()` | `count()` / `size()` |
| `SUM()` | `sum()` |
| `AVG()` | `mean()` |
| `MAX()` | `max()` |
| `MIN()` | `min()` |
| `CASE WHEN` | Conditional operations |
| `IS NULL` | `isna()` |
| `IS NOT NULL` | `notna()` |
| `DENSE_RANK()` | `rank(method="dense")` |
| `RANK()` / `ROW_NUMBER()` | `rank()` with suitable method / ordering logic |
| `LAG(column)` | `Series.shift(1)` |
| `LEAD(column)` | `Series.shift(-1)` |
| Self join | Self `merge()` |
| Duplicate detection | `duplicated()` / `drop_duplicates()` |

The exact Pandas implementation may differ depending on the problem.

The objective is not to force a one-to-one translation, but to understand how the **same data requirement can be expressed in SQL and Python**.

---

## Patterns Learned So Far

Instead of memorizing isolated syntax, I track reusable problem-solving patterns.

| Pattern | SQL Thinking | Pandas Thinking |
| --- | --- | --- |
| Keep all rows from the left table | `LEFT JOIN` | `merge(..., how="left")` |
| Find unmatched left-side rows | `LEFT JOIN` + right key `IS NULL` | Left merge + right-side `isna()` |
| Compare rows within the same table | Self join | Self `merge()` |
| Detect repeated values | `GROUP BY` + `HAVING COUNT(*) > 1` | `groupby()` / `duplicated()` |
| Compare neighboring rows | `LAG()` / `LEAD()` | `shift()` |
| Rank without gaps | `DENSE_RANK()` | `rank(method="dense")` |
| Filter after aggregation | `HAVING` | Aggregate first, then filter |
| Find group maximum and retain matching rows | Window rank / max comparison | `groupby().max()` + merge back |

This pattern-first view helps make unfamiliar interview problems easier to recognize and solve independently.

---

## Solution Format

### SQL

Each SQL solution uses a consistent header and clean formatting.

```sql
-- Problem: Department Highest Salary
-- Platform: LeetCode
-- Date: 2026-08-22
-- Topic: JOIN / DENSE_RANK / PARTITION BY

SELECT
    Department,
    Employee,
    Salary
FROM (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (
            PARTITION BY d.id
            ORDER BY e.salary DESC
        ) AS rnk
    FROM Employee AS e
    INNER JOIN Department AS d
        ON e.departmentId = d.id
) AS ranked
WHERE rnk = 1;
```

When a problem has multiple useful solutions, they can be kept in the same file with clear approach labels.

---

### Pandas

Each Pandas solution follows the same documentation style.

```python
"""
Problem: Department Highest Salary
Platform: LeetCode
Date: 2026-08-22
Topic: Merge / GroupBy / Aggregation
"""

import pandas as pd


def department_highest_salary(
    employee: pd.DataFrame,
    department: pd.DataFrame
) -> pd.DataFrame:

    merged = employee.merge(
        department,
        left_on="departmentId",
        right_on="id",
        how="inner"
    )

    max_salary = (
        merged.groupby("name_y")["salary"]
        .max()
        .reset_index()
    )

    result = merged.merge(
        max_salary,
        on=["name_y", "salary"],
        how="inner"
    )[["name_y", "name_x", "salary"]]

    result.columns = ["Department", "Employee", "Salary"]

    return result
```

---

## Edge-Case Practice

A solution is not considered fully understood until important edge cases have been checked.

Examples include:

- empty results,
- duplicate values,
- `NULL` values in SQL,
- `NaN` values in Pandas,
- multiple rows sharing the same maximum or minimum,
- missing matches during joins,
- groups containing only one record,
- and filters that return no rows.

For example, while solving **Second Highest Salary**, an important distinction is:

```text
No matching SQL rows + normal SELECT
→ zero rows

No matching SQL rows + MAX()
→ NULL
```

Similarly, in Pandas:

```python
empty_series.max()
```

returns:

```text
NaN
```

Understanding these behaviors is part of the practice, not just getting the expected answer.

---

## Code Quality Principles

### SQL

I aim to follow:

- Uppercase SQL keywords
- Consistent indentation
- One selected column per line when useful
- Meaningful table aliases
- Clear `JOIN` conditions
- Proper spacing around operators
- Semicolons at the end of queries
- Descriptive approach labels when multiple solutions exist
- Readability over unnecessarily compressed queries

### Python / Pandas

I focus on:

- PEP 8-style formatting
- Meaningful variable names
- Type hints where useful
- Readable DataFrame transformations
- Minimal unnecessary comments
- Avoiding overly complex one-liners
- Understanding operations instead of memorizing syntax
- Writing code that I can explain during an interview

---

## Problem-Solving Workflow

```text
Understand the requirement
        ↓
Inspect the input structure
        ↓
Identify the required data operation
        ↓
Write SQL independently
        ↓
Verify the result
        ↓
Check edge cases
        ↓
Try another SQL approach when useful
        ↓
Recreate useful logic in Pandas
        ↓
Compare SQL ↔ Pandas
        ↓
Review mistakes and new methods
        ↓
Commit the solution
```

---

## Practice Sources

Problems may come from platforms such as:

- LeetCode
- DataLemur
- Other SQL and data interview practice resources

The repository contains my own solutions written for learning, consistency, and technical interview preparation.

---

## Learning Goals

Through consistent practice, I aim to improve my ability to:

- Translate business questions into queries
- Write SQL without relying on memorized solutions
- Recognize common SQL problem patterns
- Choose appropriate joins and aggregations
- Use subqueries and window functions confidently
- Handle duplicates and missing values correctly
- Identify important edge cases
- Work confidently with Pandas DataFrames
- Translate SQL logic into Python
- Manipulate tabular data efficiently
- Compare multiple valid approaches
- Write readable and maintainable code
- Explain my reasoning clearly during interviews

---

## Practice Philosophy

This repository follows a **depth-over-volume** approach.

```text
One Problem
    ↓
SQL Logic
    ↓
Alternative Approach
    ↓
Edge Cases
    ↓
Pandas Equivalent
    ↓
SQL ↔ Pandas Mapping
    ↓
New Methods
    ↓
Stronger Pattern Recognition
```

A problem is valuable not because it increases a solved-question counter, but because it improves the ability to solve the next problem independently.

---

## Core Principle

> **Understand the data. Build the logic. Explore useful alternatives. Handle edge cases. Write clean code. Verify the result. Learn from mistakes. Repeat consistently.**

This repository serves as a long-term record of continuous improvement in **SQL, Pandas, and data problem solving**.
