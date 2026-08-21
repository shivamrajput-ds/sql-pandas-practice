**# SQL & Pandas Practice**

A structured, long-term practice repository focused on strengthening ****SQL and Pandas problem-solving skills for Data Science, Analytics, and technical interviews****.

The main idea behind this repository is simple:

\> ****Solve the data problem in SQL, understand the logic deeply, explore alternative SQL approaches when useful, and recreate the same or similar operation in Pandas whenever it adds learning value.****

This repository emphasizes ****clean code, strong fundamentals, interview-oriented problem solving, edge-case awareness, and consistent practice****.

**---**

**## Tech Stack**

\- ****Microsoft SQL Server / T-SQL****

\- ****Python 3****

\- ****Pandas****

\- ****SQL Server Management Studio (SSMS)****

\- ****Google Colab / Jupyter Notebook****

**---**

**## Practice Routine**

My regular practice focuses on:

\- ****1 SQL problem per day****

\- Solving the SQL problem independently first

\- Exploring a second SQL approach when it provides useful learning

\- Recreating the same or similar problem in Pandas

\- Testing important edge cases

\- Understanding why the solution works

\- Comparing equivalent SQL and Pandas operations

\- Keeping solutions clean and readable

A typical session looks like:

```text

1 SQL Problem

      ↓

Approach 1

      ↓

Verify Result

      ↓

Approach 2 — if useful

      ↓

Check Edge Cases

      ↓

Pandas Recreation

      ↓

Review New Concepts

      ↓

Stop

```

The goal is ****not to solve the maximum number of questions****.

The goal is to understand each problem well enough to:

\- reproduce the solution independently,

\- explain the logic clearly,

\- recognize the underlying pattern,

\- handle edge cases,

\- and apply the same idea to future problems.

**---**

**## Repository Structure**

```text

sql-pandas-practice/

│

├── sql/

│   └── 2026/

│       └── 08/

│           ├── 2026-08-14-combine-two-tables.sql

│           ├── 2026-08-15-second-highest-salary.sql

│           ├── 2026-08-16-nth-highest-salary.sql

│           ├── 2026-08-17-rank-scores.sql

│           ├── 2026-08-18-consecutive-numbers.sql

│           ├── 2026-08-19-employees-earning-more-than-their-managers.sql

│           └── 2026-08-20-duplicate-emails.sql

│

├── pandas/

│   └── 2026/

│       └── 08/

│           ├── 2026-08-14-combine-two-tables.py

│           ├── 2026-08-15-second-highest-salary.py

│           ├── 2026-08-16-nth-highest-salary.py

│           ├── 2026-08-17-rank-scores.py

│           ├── 2026-08-18-consecutive-numbers.py

│           ├── 2026-08-19-employees-earning-more-than-their-managers.py

│           └── 2026-08-20-duplicate-emails.py

│

└── README.md

```

Problems are organized using:

```text

Technology → Year → Month → Problem

```

**---**

**## File Naming Convention**

```text

YYYY-MM-DD-problem-name.extension

```

Examples:

```text

sql/2026/08/2026-08-14-combine-two-tables.sql

pandas/2026/08/2026-08-14-combine-two-tables.py

sql/2026/08/2026-08-15-second-highest-salary.sql

pandas/2026/08/2026-08-15-second-highest-salary.py

sql/2026/08/2026-08-16-nth-highest-salary.sql

pandas/2026/08/2026-08-16-nth-highest-salary.py

sql/2026/08/2026-08-17-rank-scores.sql

pandas/2026/08/2026-08-17-rank-scores.py

sql/2026/08/2026-08-18-consecutive-numbers.sql

pandas/2026/08/2026-08-18-consecutive-numbers.py

sql/2026/08/2026-08-19-employees-earning-more-than-their-managers.sql

pandas/2026/08/2026-08-19-employees-earning-more-than-their-managers.py

sql/2026/08/2026-08-20-duplicate-emails.sql

pandas/2026/08/2026-08-20-duplicate-emails.py

```

This keeps the repository easy to navigate as the number of solved problems grows over time.

**---**

**## Recent Practice**

| Date | Problem | SQL Concepts | Pandas Concepts |

| --- | --- | --- | --- |

| 2026-08-14 | Combine Two Tables | `LEFT JOIN` | `merge()` |

| 2026-08-15 | Second Highest Salary | Subquery, `DENSE_RANK()` | Filtering, `max()` |

| 2026-08-16 | Nth Highest Salary | Scalar function, `DENSE_RANK()` | `drop_duplicates()`, `sort_values()`, `iloc[]` |

| 2026-08-17 | Rank Scores | `DENSE_RANK()`, correlated subquery | `rank(method="dense")`, `sort_values()` |

| 2026-08-18 | Consecutive Numbers | `LEAD()`, `LAG()`, self join | `shift()`, boolean filtering, `unique()` |

| 2026-08-19 | Employees Earning More Than Their Managers | Self join, filtering | Self merge, `query()`, `to_frame()` |

| 2026-08-20 | Duplicate Emails | `GROUP BY`, `HAVING`, `COUNT()` | `groupby()`, `size()`, `duplicated()`, `drop_duplicates()`, `rename()` |
| 2026-08-21 | Customers Who Never Order | `LEFT JOIN`, anti-join pattern, `IS NULL` | `merge(how="left")`, `query()`, `isna()`, `rename()` |

**---**

**## SQL Focus**

SQL solutions are primarily written using ****Microsoft SQL Server / T-SQL syntax****.

Topics include:

\- `SELECT`

\- `DISTINCT`

\- `WHERE`

\- `ORDER BY`

\- Aggregate Functions

\- `GROUP BY`

\- `HAVING`

\- `INNER JOIN`

\- `LEFT JOIN`

\- `RIGHT JOIN`

\- `FULL OUTER JOIN`

\- `CASE`

\- Subqueries

\- Common Table Expressions (CTEs)

\- Self Joins

\- Set Operations

\- Window Functions

\- `ROW_NUMBER()`

\- `RANK()`

\- `DENSE_RANK()`

\- `LEAD()`

\- `LAG()`

\- Date Functions

\- String Functions

\- NULL Handling

\- Duplicate Detection

\- Conditional Aggregation

As practice progresses, I also aim to strengthen my understanding of:

\- indexes,

\- query execution,

\- query optimization,

\- and SQL Server execution plans.

**---**

**## Pandas Focus**

Pandas practice focuses on translating data manipulation requirements into clear Python operations.

Topics include:

\- DataFrame selection

\- Boolean filtering

\- `merge()`

\- Self merge / self join patterns

\- `query()`

\- `to_frame()`

\- `groupby()`

\- `size()` / `count()` for grouped counts

\- `duplicated()` for duplicate detection

\- Aggregations

\- `sort_values()`

\- `drop_duplicates()`

\- `rename()` for column renaming

\- Missing value handling

\- `isna()` / `notna()`

\- Conditional transformations

\- String operations

\- Date/time operations

\- Ranking

\- Window-like operations

\- `shift()` for previous/next-row comparisons

\- Reshaping

\- Data cleaning

\- Feature creation

\- `.loc[]`

\- `.iloc[]`

Pandas concepts are learned primarily ****through problems when they naturally become useful****, instead of memorizing a large number of methods in isolation.

**---**

**## SQL ↔ Pandas Mapping**

One major objective of this repository is to develop a strong connection between SQL operations and their Pandas equivalents.

| SQL | Pandas |

| --- | --- |

| `SELECT` | Column selection |

| `WHERE` | Boolean filtering |

| `LEFT JOIN` | `merge(how="left")` |

| `INNER JOIN` | `merge(how="inner")` |

| `GROUP BY` | `groupby()` |

| `HAVING` | Filter grouped/aggregated results |

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

| `RANK()` / `ROW_NUMBER()` | `rank()` with appropriate method / ordering logic |

| `LAG(column)` | `Series.shift(1)` |

| `LEAD(column)` | `Series.shift(-1)` |

| Self join | Self `merge()` |

| Duplicate detection | `duplicated()` / `drop_duplicates()` |

| Single selected Series → result table | `to_frame()` when a DataFrame is required |

The exact Pandas implementation may differ depending on the problem.

The objective is not to force a one-to-one translation, but to understand how the ****same data requirement can be expressed in SQL and Python****.

**---**

**## Solution Format**

**### SQL**

Each SQL solution uses a consistent header and clean formatting.

```sql

\-- Problem: Combine Two Tables

\-- Platform: LeetCode

\-- Date: 2026-08-14

\-- Topic: LEFT JOIN

SELECT

    p.firstName,

    p.lastName,

    a.city,

    a.state

FROM Person AS p

LEFT JOIN Address AS a

    ON p.personId = a.personId;

```

When a problem has multiple useful solutions, they are kept in the same file.

Example:

```sql

\-- Problem: Second Highest Salary

\-- Platform: LeetCode

\-- Date: 2026-08-15

\-- Topic: Subquery / Window Function / Aggregation

\-- Approach 1: MAX + Subquery

SELECT

    MAX(salary) AS SecondHighestSalary

FROM Employee

WHERE salary < (

    SELECT MAX(salary)

    FROM Employee

);

\-- Approach 2: DENSE_RANK

SELECT

    MAX(salary) AS SecondHighestSalary

FROM (

    SELECT

        salary,

        DENSE_RANK() OVER (

            ORDER BY salary DESC

        ) AS ranking

    FROM Employee

) AS ranked_salaries

WHERE ranking = 2;

```

**---**

**### Pandas**

Each Pandas solution follows the same clean documentation style.

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

    return result[

        ["firstName", "lastName", "city", "state"]

    ]

```

Another example:

```python

"""

Problem: Second Highest Salary

Platform: LeetCode

Date: 2026-08-15

Topic: Filtering / Aggregation

"""

import pandas as pd


def second_highest_salary(

    employee: pd.DataFrame

) -> pd.DataFrame:

    max_salary = employee["salary"].max()

    filtered_employee = employee[

        employee["salary"] < max_salary

    ]

    second_salary = filtered_employee["salary"].max()

    return pd.DataFrame(

        [second_salary],

        columns=["SecondHighestSalary"]

    )

```

**---**

**## Patterns Learned So Far

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

This pattern-first view is intended to make unfamiliar interview problems easier to recognize and solve independently.

---

## Edge-Case Practice**

A solution is not considered fully understood until important edge cases have been checked.

Examples include:

\- empty results,

\- duplicate values,

\- `NULL` values in SQL,

\- `NaN` values in Pandas,

\- multiple rows sharing the same maximum or minimum,

\- missing matches during joins,

\- groups containing only one record,

\- and filters that return no rows.

For example, while solving ****Second Highest Salary****, an important distinction is:

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

**---**

**## Code Quality Principles**

**### SQL**

I aim to follow:

\- Uppercase SQL keywords

\- Consistent indentation

\- One selected column per line when useful

\- Meaningful table aliases

\- Clear `JOIN` conditions

\- Proper spacing around operators

\- Semicolons at the end of queries

\- Descriptive approach labels when multiple solutions exist

\- Readability over unnecessarily compressed queries

**### Python / Pandas**

I focus on:

\- PEP 8-style formatting

\- Meaningful variable names

\- Type hints where useful

\- Readable DataFrame transformations

\- Minimal unnecessary comments

\- Avoiding overly complex one-liners

\- Understanding operations instead of memorizing syntax

\- Writing code that I can explain during an interview

**---**

**## Problem-Solving Workflow**

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

Explore new methods encountered

        ↓

Review mistakes

        ↓

Commit the solution

```

**---**

**## Practice Sources**

Problems may come from platforms such as:

\- LeetCode

\- DataLemur

\- Other SQL and data interview practice resources

The repository contains my own solutions written for learning, consistency, and technical interview preparation.

**---**

**## Learning Goals**

Through consistent practice, I aim to improve my ability to:

\- Translate business questions into queries

\- Write SQL without relying on memorized solutions

\- Recognize common SQL problem patterns

\- Choose appropriate joins and aggregations

\- Use subqueries and window functions confidently

\- Handle duplicates and missing values correctly

\- Identify important edge cases

\- Work confidently with Pandas DataFrames

\- Translate SQL logic into Python

\- Manipulate tabular data efficiently

\- Compare multiple valid approaches

\- Write readable and maintainable code

\- Explain my reasoning clearly during interviews

**---**

**## Practice Philosophy**

This repository follows a ****depth-over-volume**** approach.

Solving one problem carefully can expose multiple concepts:

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

New Methods

    ↓

Stronger Pattern Recognition

```

A problem is valuable not because it increases a solved-question counter, but because it improves the ability to solve the next problem independently.

**---**

**## Core Principle**

Q

\> ****Understand the data. Build the logic. Explore useful alternatives. Handle edge cases. Write clean code. Verify the result. Learn from mistakes. Repeat consistently.****

This repository serves as a long-term record of continuous improvement in ****SQL, Pandas, and data problem solving****.