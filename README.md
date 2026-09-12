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
| Latest entry | 2026-09-12 |
| Data problems completed | **21** |
| SQL solution files | **21** |
| Pandas recreation files | **21** |
| Primary SQL dialect | **Microsoft SQL Server / T-SQL** |
| Practice style | **Depth-first; consistency with planned breaks for placement preparation** |

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
│   └── 2026/
│       ├── 08/
│       │   ├── 2026-08-14-combine-two-tables.sql
│       │   ├── 2026-08-15-second-highest-salary.sql
│       │   ├── 2026-08-16-nth-highest-salary.sql
│       │   ├── 2026-08-17-rank-scores.sql
│       │   ├── 2026-08-18-consecutive-numbers.sql
│       │   ├── 2026-08-19-employees-earning-more-than-their-managers.sql
│       │   ├── 2026-08-20-duplicate-emails.sql
│       │   ├── 2026-08-21-customers-who-never-order.sql
│       │   ├── 2026-08-22-department-highest-salary.sql
│       │   ├── 2026-08-23-department-top-three-salaries.sql
│       │   ├── 2026-08-24-delete-duplicate-emails.sql
│       │   ├── 2026-08-25-trips-and-users.sql
│       │   ├── 2026-08-26-game-play-analysis-i.sql
│       │   └── 2026-08-31-rising-temperature.sql
│       │
│       └── 09/
│           ├── 2026-09-01-big-countries.sql
│           ├── 2026-09-02-game-play-analysis-iv.sql
│           ├── 2026-09-03-managers-with-at-least-5-direct-reports.sql
│           ├── 2026-09-04-employee-bonus.sql
│           ├── 2026-09-04-find-customer-referee.sql
│           ├── 2026-09-05-investments-in-2016.sql
│           └── 2026-09-12-customer-placing-the-largest-number-of-orders.sql
│
├── pandas/
│   └── 2026/
│       ├── 08/
│       │   ├── 2026-08-14-combine-two-tables.py
│       │   ├── 2026-08-15-second-highest-salary.py
│       │   ├── 2026-08-16-nth-highest-salary.py
│       │   ├── 2026-08-17-rank-scores.py
│       │   ├── 2026-08-18-consecutive-numbers.py
│       │   ├── 2026-08-19-employees-earning-more-than-their-managers.py
│       │   ├── 2026-08-20-duplicate-emails.py
│       │   ├── 2026-08-21-customers-who-never-order.py
│       │   ├── 2026-08-22-department-highest-salary.py
│       │   ├── 2026-08-23-department-top-three-salaries.py
│       │   ├── 2026-08-24-delete-duplicate-emails.py
│       │   ├── 2026-08-25-trips-and-users.py
│       │   ├── 2026-08-26-game-play-analysis-i.py
│       │   └── 2026-08-31-rising-temperature.py
│       │
│       └── 09/
│           ├── 2026-09-01-big-countries.py
│           ├── 2026-09-02-game-play-analysis-iv.py
│           ├── 2026-09-03-managers-with-at-least-5-direct-reports.py
│           ├── 2026-09-04-employee-bonus.py
│           ├── 2026-09-04-find-customer-referee.py
│           ├── 2026-09-05-investments-in-2016.py
│           └── 2026-09-12-customer-placing-the-largest-number-of-orders.py
│
└── README.md
```

### Naming Convention

```text
YYYY-MM-DD-problem-name.extension
```

Examples:

```text
sql/2026/09/2026-09-12-customer-placing-the-largest-number-of-orders.sql
pandas/2026/09/2026-09-12-customer-placing-the-largest-number-of-orders.py
```

Month folders follow the problem date:

```text
2026-08-*  →  08/
2026-09-*  →  09/
```

This keeps the repository chronological, searchable, and easy to scale.

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
| 2026-08-26 | Game Play Analysis I | `GROUP BY`, `MIN()`, `ROW_NUMBER()` | `groupby().min()`, `sort_values()`, `cumcount()` |
| 2026-08-31 | Rising Temperature | Self join, `LAG()`, `DATEDIFF()` | `sort_values()`, `shift()`, `Timedelta`, boolean filtering |
| 2026-09-01 | Big Countries | `WHERE`, `OR`, filtering | `query()`, boolean filtering, column selection |
| 2026-09-02 | Game Play Analysis IV | CTE, `MIN()`, join, `DATEDIFF()`, ratio calculation | `nunique()`, `groupby().min()`, `merge()`, `Timedelta`, boolean mask |
| 2026-09-03 | Managers with at Least 5 Direct Reports | `IN`, `GROUP BY`, `HAVING`, self join | Self `merge()`, `groupby()`, `count()`, `query()`, `isin()` |
| 2026-09-04 | Employee Bonus | `LEFT JOIN`, `IS NULL`, `OR` | `merge(how="left")`, `isna()`, boolean mask |
| 2026-09-04 | Find Customer Referee | `WHERE`, `IS NULL`, `<>`, `OR` | `query()`, `isnull()`, column selection |
| 2026-09-05 | Investments in 2016 | `GROUP BY`, `HAVING`, `IN`, `EXISTS`, `NOT EXISTS`, `SUM()` | `groupby().size()`, `query()`, `isin()`, tuple pairs, boolean mask |
| 2026-09-12 | Customer Placing the Largest Number of Orders | CTE, `COUNT()`, `MAX()`, `DENSE_RANK()`, window function | `groupby().size()`, `reset_index()`, `max()`, `query()` |

---

## Practice Continuity Note

Regular SQL & Pandas practice was paused from **2026-09-06 to 2026-09-11** while I focused on preparation for the **Info Origin placement process**, including Python, DSA, OOP, problem-solving, AI/ML, and interview preparation.

This was a **planned learning shift, not an abandoned practice streak**. SQL & Pandas practice resumed on **2026-09-12** with the same depth-first approach.

---

## Recent Learning Highlights

### Customer Placing the Largest Number of Orders

This problem reinforced two ways to solve a **maximum-after-aggregation** problem.

SQL approach 1:

```text
GROUP BY customer_number
→ COUNT orders per customer
→ MAX(no_of_orders)
→ keep every customer whose count equals the maximum
```

SQL approach 2:

```text
GROUP BY customer_number
→ COUNT orders
→ DENSE_RANK() OVER (ORDER BY no_of_orders DESC)
→ keep ranking = 1
```

The second approach reinforced that `PARTITION BY` is **not compulsory** in a window function. When all rows need to be ranked together, only `ORDER BY` is required inside `OVER(...)`.

Pandas recreation:

```text
groupby()
→ size()
→ reset_index(name="no_of_orders")
→ max()
→ query("no_of_orders == @max_orders")
```

Reusable lesson:

> **Aggregate first, then compare against the aggregate maximum. If ties must be preserved, use equality with the maximum or a tie-aware ranking function such as DENSE_RANK().**

---

### Investments in 2016

This problem reinforced two different ways to express existence and uniqueness conditions.

```text
Condition 1:
same tiv_2015 must exist for another policyholder
Condition 2:
same (lat, lon) must not exist for another policyholder
```

SQL approaches:

```text
GROUP BY + HAVING + IN
or
EXISTS + NOT EXISTS
```

Pandas recreation:

```text
groupby().size()
→ identify duplicate tiv_2015 values
→ identify unique (lat, lon) pairs
→ combine boolean conditions
→ sum tiv_2016
```

Reusable lesson:

> **EXISTS asks whether a matching row is present; NOT EXISTS asks whether a forbidden matching row is absent.**

---

### Employee Bonus

This problem reinforced a very common missing-match pattern.

```text
Keep every employee
        ↓
Attach bonus if available
        ↓
Keep:
bonus < 1000
OR
bonus is missing
```

SQL:

```sql
LEFT JOIN Bonus
    ON Employee.empId = Bonus.empId
WHERE bonus IS NULL
   OR bonus < 1000
```

Pandas:

```python
merge(..., how="left")
df["bonus"].isna() | (df["bonus"] < 1000)
```

Reusable lesson:

> **A left join followed by a NULL check is often used when missing matches are meaningful and must remain in the result.**

---

### Find Customer Referee

This problem reinforced SQL NULL logic.

Requirement:

```text
Keep customers whose referee is NOT 2
including customers with no referee
```

The SQL condition must explicitly include NULL:

```sql
WHERE referee_id IS NULL
   OR referee_id <> 2
```

because:

```text
NULL <> 2
```

does not evaluate to `TRUE` in SQL.

Pandas recreation:

```python
customer.query(
    "referee_id.isnull() or referee_id != 2"
)
```

Reusable lesson:

> **When NULL rows should survive a filter, handle them explicitly instead of assuming a normal comparison will include them.**

---

### Managers with at Least 5 Direct Reports

This problem reinforced how a hierarchical relationship inside one table can be solved using:

```text
GROUP BY managerId + HAVING
```

or:

```text
Self Join
```

Pandas used the same self-relationship through:

```text
self merge
→ groupby
→ count
→ query
→ isin
```

---

### Game Play Analysis IV

```text
First login
    ↓
exact next-day login
    ↓
returning players / total players
```

Key concepts:

```text
SQL:
MIN()
GROUP BY
JOIN
DATEDIFF()
COUNT(DISTINCT)
ROUND()
Pandas:
groupby().min()
merge()
Timedelta
nunique()
boolean mask
round()
```

---

### Big Countries

A reminder that simple problems should stay simple:

```text
Filter rows
→ select required columns
```

SQL:

```sql
WHERE condition1 OR condition2
```

Pandas:

```python
query("condition1 or condition2")
```

---

### Rising Temperature

```text
Previous row ≠ always previous calendar day
```

Therefore:

```text
SQL:
LAG() / self join + DATEDIFF()
Pandas:
shift() + Timedelta comparison
```

---

## Patterns Learned

| Pattern | SQL Thinking | Pandas Thinking |
| --- | --- | --- |
| Preserve every row from the left table | `LEFT JOIN` | `merge(..., how="left")` |
| Find unmatched rows | `LEFT JOIN` + `IS NULL` | Left merge + `isna()` |
| Keep missing matches or low values | `IS NULL OR value < N` | `isna() \\| (value < N)` |
| Match only common rows | `INNER JOIN` | `merge(..., how="inner")` |
| Compare rows in the same table | Self join | Self `merge()` |
| Model parent-child relationships | Self join using parent/child keys | Self merge using `left_on` / `right_on` |
| Detect duplicate values | `GROUP BY` + `HAVING COUNT(*) > 1` | `groupby()` / `duplicated()` |
| Aggregate by group | `GROUP BY` | `groupby()` |
| Filter aggregated results | `HAVING` | Aggregate, then filter / `query()` |
| Find groups meeting minimum count | `HAVING COUNT(*) >= N` | Grouped count + filter |
| Filter rows using a set of IDs | `WHERE ... IN (...)` | `isin()` |
| Find earliest value in a group | `MIN()` | `groupby().min()` |
| Keep first ordered row per group | `ROW_NUMBER()` + rank 1 | Sort + `cumcount() + 1` |
| Compare adjacent rows | `LAG()` / `LEAD()` | `shift()` |
| Validate exact day gaps | `DATEDIFF()` | datetime subtraction + `Timedelta` |
| Rank without gaps | `DENSE_RANK()` | `rank(method="dense")` |
| Rank with gaps | `RANK()` | `rank(method="min")` |
| Assign row numbers | `ROW_NUMBER()` | ordered `cumcount() + 1` |
| Find group maximum | `MAX()` | `groupby().max()` |
| Top-N distinct values per group | `DENSE_RANK()` + filter | grouped dense rank + filter |
| Keep one duplicate row | `ROW_NUMBER()` + rank 1 | sort + `drop_duplicates()` |
| Conditional counting | `SUM(CASE WHEN...)` | mask/filter + grouped count |
| Preserve zero-count groups | Conditional aggregation / outer join | left merge + `fillna(0)` |
| Count unique entities | `COUNT(DISTINCT col)` | `nunique()` |
| Calculate ratios | decimal division | numeric division + `round()` |
| OR filtering | `WHERE ... OR ...` | `query()` / `\\|` |
| NULL filtering | `IS NULL` / `IS NOT NULL` | `isna()` / `notna()` |
| Not-equal with possible NULLs | Explicit `IS NULL OR <>` | `isnull() or !=` |
| Check whether a related row exists | `EXISTS` | Boolean membership / merge-based existence check |
| Ensure no forbidden related row exists | `NOT EXISTS` | Negated membership / anti-match logic |
| Find maximum after aggregation | Aggregate + `MAX()` comparison | Grouped result + `max()` + filter |
| Preserve ties at the maximum | `DENSE_RANK()` / equality with max | Equality filter against grouped maximum |

---

## SQL ↔ Pandas Reference

| SQL | Pandas |
| --- | --- |
| `SELECT` | Column selection |
| `WHERE` | Boolean filtering / `.loc[]` |
| `WHERE ... OR ...` | `query("... or ...")` / `\\|` |
| `WHERE col IN (...)` | `Series.isin(...)` |
| `ORDER BY` | `sort_values()` |
| `DISTINCT` | `drop_duplicates()` |
| `INNER JOIN` | `merge(how="inner")` |
| `LEFT JOIN` | `merge(how="left")` |
| Self join | Self `merge()` |
| `GROUP BY` | `groupby()` |
| `HAVING` | Aggregate first, then filter |
| `COUNT()` | `count()` / `size()` |
| `COUNT(DISTINCT col)` | `nunique()` |
| `SUM()` | `sum()` |
| `AVG()` | `mean()` |
| `MAX()` | `max()` |
| `MIN()` | `min()` |
| `CASE WHEN` | Boolean masks / conditional assignment |
| `IS NULL` | `isna()` / `isnull()` |
| `IS NOT NULL` | `notna()` / `notnull()` |
| `<>` / `!=` | `!=` |
| `DENSE_RANK()` | `rank(method="dense")` |
| `RANK()` | `rank(method="min")` |
| `ROW_NUMBER()` | ordered `cumcount() + 1` |
| `LAG(column)` | `shift(1)` |
| `LEAD(column)` | `shift(-1)` |
| `DATEDIFF(DAY, a, b)` | `b - a` + `pd.Timedelta(...)` |
| First value per group | `MIN()` / `ROW_NUMBER()` | `groupby().min()` / sort + `cumcount()` |
| `HAVING COUNT(*) >= N` | grouped count + filter |
| Conditional aggregation | `SUM(CASE...)` | mask/filter + aggregation |
| `COALESCE()` | `fillna()` |
| `EXISTS` | Matching-row / membership check |
| `NOT EXISTS` | Negated matching-row / anti-match check |
| Aggregate + `MAX()` filter | Grouped result + `max()` + `query()` |

The objective is **not** to force every SQL statement into a literal one-to-one Pandas translation.

The objective is to understand how the **same data requirement** can be expressed naturally in both tools.

---

## SQL Focus

Solutions are primarily written using **Microsoft SQL Server / T-SQL**.

### Core Querying

- `SELECT`

- `DISTINCT`

- `WHERE`

- `IN`

- `AND`

- `OR`

- `<>`

- `ORDER BY`

- aliases

- NULL handling

- date filtering

### Joins

- `INNER JOIN`

- `LEFT JOIN`

- `RIGHT JOIN`

- `FULL OUTER JOIN`

- self joins

- parent-child relationships

- anti-join patterns

- repeated joins to the same lookup table

### Aggregation

- `COUNT()`

- `COUNT(DISTINCT ...)`

- `SUM()`

- `AVG()`

- `MAX()`

- `MIN()`

- `GROUP BY`

- `HAVING`

- conditional aggregation

- count thresholds

- grouped ratios

### Intermediate / Advanced Querying

- subqueries

- correlated subqueries

- Common Table Expressions

- `CASE`

- scalar functions

- `DELETE`

- set operations

### Window Functions

- `ROW_NUMBER()`

- `RANK()`

- `DENSE_RANK()`

- `LAG()`

- `LEAD()`

- partitioned calculations

- global ranking without `PARTITION BY`

- tie-preserving maximum selection

### Date Logic

- `DATEDIFF()`

- exact day-gap validation

- date ranges

- previous-row vs previous-day reasoning

### Future Depth

- indexes

- execution plans

- query optimization

- performance trade-offs

---

## Pandas Focus

### Selection and Filtering

- column selection

- boolean masks

- `.loc[]`

- `.iloc[]`

- `query()`

- `isin()`

- `isna()` / `isnull()`

- `notna()` / `notnull()`

- AND / OR filtering

- date filtering

### Combining Data

- `merge()`

- left / inner merges

- self merge

- parent-child self relationships

- suffix handling

- merge-back patterns

### Grouping and Aggregation

- `groupby()`

- `size()`

- `count()`

- `nunique()`

- `sum()`

- `mean()`

- `min()`

- `max()`

- grouped threshold filtering

- ratios

### Ranking and Row Relationships

- `rank()`

- `shift()`

- `cumcount()`

- grouped ranking

- first-row-per-group logic

### Date and Time Logic

- datetime subtraction

- `pd.Timedelta`

- previous-day validation

- date-range comparisons

### Data Quality and Transformation

- `duplicated()`

- `drop_duplicates()`

- `fillna()`

- `rename()`

- `to_frame()`

- `sort_values()`

- in-place modification

- string operations

- feature creation

Pandas methods are learned **when a problem naturally requires them**, rather than memorized in isolation.

---

## Edge-Case Checklist

Before considering a solution complete, I check cases such as:

- empty input or empty result,

- duplicate values,

- ties,

- SQL `NULL`,

- Pandas `NaN`,

- missing join matches,

- groups with one row,

- multiple rows sharing max/min,

- exact count boundaries,

- employees without managers,

- missing bonus records,

- nullable foreign/reference IDs,

- zero-count groups,

- integer division,

- missing calendar dates,

- unique entities vs row counts,

- filters returning no rows.

### Important NULL lesson

SQL follows three-valued logic.

For example:

```sql
referee_id <> 2
```

does **not** automatically include `NULL`.

If NULL should remain:

```sql
referee_id IS NULL
OR referee_id <> 2
```

This is a reusable interview pattern.

---

## Code Quality Principles

### SQL

- Uppercase keywords

- Consistent indentation

- Meaningful aliases

- Explicit joins

- Clear NULL logic

- Readable window functions

- Safe decimal division

- Semicolons at statement boundaries

- Prefer the simplest correct solution

### Python / Pandas

- PEP 8-style formatting

- Meaningful variable names

- Type hints where useful

- Readable transformations

- Clear boolean masks

- Minimal unnecessary comments

- Avoid overly complex one-liners

- Prefer code that can be clearly explained

---

## Learning Goals

This repository is intended to strengthen my ability to:

- translate requirements into SQL and Pandas,

- solve independently,

- recognize reusable patterns,

- choose correct joins,

- understand self joins,

- use `WHERE`, `IN`, `GROUP BY`, and `HAVING`,

- reason correctly about NULL values,

- use window functions confidently,

- distinguish row-level vs aggregate filtering,

- distinguish row counts vs unique counts,

- reason about date continuity,

- calculate ratios correctly,

- handle duplicates and missing data,

- manipulate DataFrames confidently,

- translate SQL logic into Pandas,

- compare useful alternative approaches,

- choose the simplest appropriate solution,

- write maintainable data code,

- and explain solutions clearly in interviews.

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

On some days, two simple problems may be completed when both are understood and solved independently. Short planned pauses may also be taken when placement or interview preparation requires focused attention.

A problem is valuable not because it increases a solved-question counter, but because it makes the **next unfamiliar problem easier to solve independently**.

---

## Core Principle

> **Understand the data. Build the logic. Verify the result. Explore useful alternatives. Handle edge cases. Translate the pattern. Learn from mistakes. Repeat consistently.**

This repository is a long-term record of continuous improvement in **SQL, Pandas, and practical data problem solving**.
