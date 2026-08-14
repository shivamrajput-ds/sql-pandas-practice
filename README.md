# SQL & Pandas Practice

A structured, long-term practice repository focused on strengthening **SQL and Pandas problem-solving skills for Data Science, Analytics, and technical interviews**.

The main idea behind this repository is simple:

> **Solve the data problem in SQL, understand the logic, and recreate the same or similar operation in Pandas whenever it adds learning value.**

This repository emphasizes **clean code, strong fundamentals, interview-oriented problem solving, and consistent practice**.

---

## Tech Stack

* **Microsoft SQL Server / T-SQL**
* **Python 3**
* **Pandas**
* **SQL Server Management Studio (SSMS)**
* **Google Colab / Jupyter Notebook**

---

## Practice Routine

My regular practice focuses on:

* 1 SQL problem
* 1 Pandas problem or SQL-to-Pandas recreation
* Clean query/code formatting
* Understanding the underlying data operation
* Reviewing mistakes and edge cases
* Learning equivalent operations across SQL and Pandas

The goal is **not to solve the maximum number of questions**, but to understand each problem well enough to explain and reproduce the solution independently.

---

## Repository Structure

```text
sql-pandas-practice/
│
├── sql/
│   └── 2026/
│       └── 08/
│           └── YYYY-MM-DD-problem-name.sql
│
├── pandas/
│   └── 2026/
│       └── 08/
│           └── YYYY-MM-DD-problem-name.py
│
└── README.md
```

Problems are organized using:

```text
Technology → Year → Month → Problem
```

---

## File Naming Convention

```text
YYYY-MM-DD-problem-name.extension
```

Example:

```text
sql/2026/08/2026-08-14-combine-two-tables.sql

pandas/2026/08/2026-08-14-combine-two-tables.py
```

This keeps the repository easy to navigate as the number of solved problems grows over time.

---

## SQL Focus

SQL solutions are primarily written using **Microsoft SQL Server / T-SQL syntax**.

Topics include:

* `SELECT`
* `DISTINCT`
* `WHERE`
* `ORDER BY`
* Aggregate Functions
* `GROUP BY`
* `HAVING`
* `INNER JOIN`
* `LEFT JOIN`
* `RIGHT JOIN`
* `FULL OUTER JOIN`
* `CASE`
* Subqueries
* Common Table Expressions (CTEs)
* Self Joins
* Set Operations
* Window Functions
* `ROW_NUMBER()`
* `RANK()`
* `DENSE_RANK()`
* `LEAD()`
* `LAG()`
* Date Functions
* String Functions
* NULL Handling
* Duplicate Detection
* Conditional Aggregation

As practice progresses, I also focus on understanding concepts such as **indexes, query execution, and SQL Server execution plans**.

---

## Pandas Focus

Pandas practice focuses on translating data manipulation requirements into clean Python operations.

Topics include:

* DataFrame selection
* Boolean filtering
* `merge()`
* `groupby()`
* Aggregations
* `sort_values()`
* `drop_duplicates()`
* Missing value handling
* Conditional transformations
* String operations
* Date/time operations
* Ranking
* Window-like operations
* Reshaping
* Data cleaning
* Feature creation

---

## SQL ↔ Pandas Mapping

One major objective of this repository is to develop a strong connection between SQL operations and their Pandas equivalents.

| SQL            | Pandas                               |
| -------------- | ------------------------------------ |
| `SELECT`       | Column selection                     |
| `WHERE`        | Boolean filtering                    |
| `LEFT JOIN`    | `merge(how="left")`                  |
| `INNER JOIN`   | `merge(how="inner")`                 |
| `GROUP BY`     | `groupby()`                          |
| `ORDER BY`     | `sort_values()`                      |
| `DISTINCT`     | `drop_duplicates()`                  |
| `COUNT()`      | `count()` / `size()`                 |
| `SUM()`        | `sum()`                              |
| `AVG()`        | `mean()`                             |
| `CASE WHEN`    | Conditional operations               |
| `IS NULL`      | `isna()`                             |
| `IS NOT NULL`  | `notna()`                            |
| `ROW_NUMBER()` | `rank()` / grouping-based operations |

The exact Pandas implementation may differ depending on the problem, but understanding this mapping makes it easier to move between **database querying and Python-based data manipulation**.

---

## Solution Format

### SQL

Each SQL solution follows a clean structure such as:

```sql
-- Problem: Combine Two Tables
-- Platform: LeetCode
-- Date: 2026-08-14
-- Topic: LEFT JOIN

SELECT
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person AS p
LEFT JOIN Address AS a
    ON p.personId = a.personId;
```

### Pandas

```python
"""
Problem: Combine Two Tables
Platform: LeetCode
Date: 2026-08-14
Topic: Merge / Left Join
"""

import pandas as pd


def combine_two_tables(
    person: pd.DataFrame,
    address: pd.DataFrame
) -> pd.DataFrame:
    result = person.merge(
        address,
        how="left",
        on="personId"
    )

    return result[["firstName", "lastName", "city", "state"]]
```

---

## Code Quality Principles

### SQL

I aim to follow:

* Uppercase SQL keywords
* Consistent indentation
* One selected column per line when useful
* Meaningful table aliases
* Clear `JOIN` conditions
* Proper spacing around operators
* Semicolons at the end of queries
* Readability over unnecessarily compressed queries

### Python / Pandas

I focus on:

* PEP 8-style formatting
* Meaningful variable names
* Readable transformations
* Minimal unnecessary comments
* Avoiding overly complex one-liners
* Understanding the operation instead of memorizing syntax

---

## Problem-Solving Workflow

```text
Understand the requirement
        ↓
Identify the required data operation
        ↓
Write the SQL solution
        ↓
Verify the result
        ↓
Understand why it works
        ↓
Recreate useful problems in Pandas
        ↓
Review formatting and mistakes
```

---

## Practice Sources

Problems may come from platforms such as:

* LeetCode
* DataLemur
* Other SQL and data interview practice resources

The repository contains my own solutions written for learning and interview preparation.

---

## Learning Goals

Through consistent practice, I aim to improve my ability to:

* Translate business questions into queries
* Write SQL without relying on memorized solutions
* Choose appropriate joins and aggregations
* Work confidently with complex SQL queries
* Manipulate tabular data efficiently using Pandas
* Translate SQL logic into Python
* Write readable and maintainable code
* Explain my approach clearly during interviews

---

## Core Principle

> **Understand the data. Build the logic. Write clean code. Verify the result. Learn from mistakes. Repeat consistently.**

This repository serves as a record of continuous improvement in **SQL, Pandas, and data problem solving**.
