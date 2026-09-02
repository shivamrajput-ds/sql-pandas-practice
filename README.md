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
| Latest entry | 2026-09-02 |
| Data problems completed | **16** |
| SQL solution files | **16** |
| Pandas recreation files | **16** |
| Primary SQL dialect | **Microsoft SQL Server / T-SQL** |
| Practice style | **1 data problem per practice day, depth-first** |

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
│       ├── 08/
│       │   ├── 2026-08-14-combine-two-tables.sql
│       │   ├── 2026-08-15-second-highest-salary.sql
│       │   ├── 2026-08-16-nth-highest-salary.sql
│       │   ├── 2026-08-17-rank-scores.sql
│       │   ├── 2026-08-18-consecutive-numbers.sql
│       │   ├── 2026-08-19-employees-earning-more-than-their-managers.sql
│       │   ├── 2026-08-20-duplicate-emails.sql
│       │   ├── 2026-08-21-customers-who-never-order.sql
│       │   ├── 2026-08-22-department-highest-salary.sql
│       │   ├── 2026-08-23-department-top-three-salaries.sql
│       │   ├── 2026-08-24-delete-duplicate-emails.sql
│       │   ├── 2026-08-25-trips-and-users.sql
│       │   ├── 2026-08-26-game-play-analysis-i.sql
│       │   └── 2026-08-31-rising-temperature.sql
│       │
│       └── 09/
│           ├── 2026-09-01-big-countries.sql
│           └── 2026-09-02-game-play-analysis-iv.sql
│
├── pandas/
│   └── 2026/
│       ├── 08/
│       │   ├── 2026-08-14-combine-two-tables.py
│       │   ├── 2026-08-15-second-highest-salary.py
│       │   ├── 2026-08-16-nth-highest-salary.py
│       │   ├── 2026-08-17-rank-scores.py
│       │   ├── 2026-08-18-consecutive-numbers.py
│       │   ├── 2026-08-19-employees-earning-more-than-their-managers.py
│       │   ├── 2026-08-20-duplicate-emails.py
│       │   ├── 2026-08-21-customers-who-never-order.py
│       │   ├── 2026-08-22-department-highest-salary.py
│       │   ├── 2026-08-23-department-top-three-salaries.py
│       │   ├── 2026-08-24-delete-duplicate-emails.py
│       │   ├── 2026-08-25-trips-and-users.py
│       │   ├── 2026-08-26-game-play-analysis-i.py
│       │   └── 2026-08-31-rising-temperature.py
│       │
│       └── 09/
│           ├── 2026-09-01-big-countries.py
│           └── 2026-09-02-game-play-analysis-iv.py
│
└── README.md
```

### Naming Convention

```text
YYYY-MM-DD-problem-name.extension
```

Examples:

```text
sql/2026/09/2026-09-02-game-play-analysis-iv.sql
pandas/2026/09/2026-09-02-game-play-analysis-iv.py
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
| 2026-08-26 | Game Play Analysis I | `GROUP BY`, `MIN()`, `ROW_NUMBER()` | `groupby().min()`, `sort_values()`, `cumcount()` |
| 2026-08-31 | Rising Temperature | Self join, `LAG()`, `DATEDIFF()` | `sort_values()`, `shift()`, `Timedelta`, boolean filtering |
| 2026-09-01 | Big Countries | `WHERE`, `OR`, filtering | `query()`, boolean filtering, column selection |
| 2026-09-02 | Game Play Analysis IV | CTE, `MIN()`, join, `DATEDIFF()`, ratio calculation | `nunique()`, `groupby().min()`, `merge()`, `Timedelta`, boolean mask |

---

## Recent Learning Highlights

### Game Play Analysis IV

This problem combined multiple concepts into one compact retention-style calculation.

The reusable thinking was:

```text
Find each player's first login
        ↓
Compare all activity with first login
        ↓
Check exact +1 day return
        ↓
Count returning players
        ↓
Divide by total unique players
        ↓
Round to 2 decimal places
```

SQL concepts reinforced:

```text
GROUP BY + MIN()
CTE
JOIN
DATEDIFF()
COUNT(DISTINCT ...)
decimal division
ROUND()
```

Pandas concepts reinforced:

```text
nunique()
groupby().min()
merge()
datetime subtraction
pd.Timedelta(days=1)
boolean mask
round()
```

---

### Big Countries

This problem reinforced a very simple but important pattern:

```text
Filter rows
        ↓
Select only required columns
```

SQL:

```text
WHERE condition1 OR condition2
```

Pandas:

```python
df.query("condition1 or condition2")[["col1", "col2", "col3"]]
```

The lesson is that not every problem needs a complex approach. The simplest correct operation is often the best one.

---

### Rising Temperature

This problem reinforced the difference between:

```text
previous row
```

and:

```text
previous calendar day
```

A row can be previous after sorting without being exactly one day earlier.

Therefore:

```text
SQL
LAG() / self join
+
DATEDIFF(...)=1
```

and:

```text
Pandas
shift(1)
+
datetime subtraction == pd.Timedelta(days=1)
```

must be combined when the business rule explicitly says **yesterday**.

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
| Find earliest value in a group | `MIN()` | `groupby().min()` |
| Keep the first ordered row per group | `ROW_NUMBER()` + rank 1 | Sort + `cumcount() + 1` |
| Compare adjacent rows | `LAG()` / `LEAD()` | `shift()` |
| Validate exact calendar-day gaps | `DATEDIFF()` | datetime subtraction + `Timedelta` |
| Rank without gaps | `DENSE_RANK()` | `rank(method="dense")` |
| Rank with gaps | `RANK()` | `rank(method="min")` |
| Assign ordered row numbers | `ROW_NUMBER()` | Ordered `cumcount() + 1` |
| Find group maximum | `MAX()` / window function | `groupby().max()` |
| Keep rows matching a group maximum | Window rank / max comparison | Aggregate + merge back |
| Top-N distinct values per group | `DENSE_RANK()` + filter | Grouped dense rank + filter |
| Keep one row from each duplicate group | `ROW_NUMBER()` + keep rank 1 | Sort + `drop_duplicates(keep="first")` |
| Conditional counting | `SUM(CASE WHEN ... THEN 1 ELSE 0 END)` | Boolean filter + grouped count |
| Preserve zero-count groups | Conditional aggregation / outer join | Left merge + `fillna(0)` |
| Count unique entities | `COUNT(DISTINCT column)` | `nunique()` |
| Calculate ratios safely | Decimal conversion + division | Numeric division + `round()` |
| Filter with OR conditions | `WHERE ... OR ...` | `query()` / boolean mask |
| Remove duplicate rows | `DISTINCT` | `drop_duplicates()` |
| Handle missing values | `IS NULL` / `IS NOT NULL` | `isna()` / `notna()` |

---

## SQL ↔ Pandas Reference

| SQL | Pandas |
| --- | --- |
| `SELECT` | Column selection |
| `WHERE` | Boolean filtering / `.loc[]` |
| `WHERE ... OR ...` | `query("... or ...")` / boolean OR |
| `ORDER BY` | `sort_values()` |
| `DISTINCT` | `drop_duplicates()` |
| `INNER JOIN` | `merge(how="inner")` |
| `LEFT JOIN` | `merge(how="left")` |
| `GROUP BY` | `groupby()` |
| `HAVING` | Aggregate first, then filter |
| `COUNT()` | `count()` / `size()` |
| `COUNT(DISTINCT col)` | `nunique()` |
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
| `DATEDIFF(DAY, a, b)` | `b - a` compared with `pd.Timedelta(days=...)` |
| Self join | Self `merge()` |
| Multiple aliases of same table | Multiple merges + suffixes |
| First value per group | `MIN()` or `ROW_NUMBER()` | `groupby().min()` or sort + `cumcount()` |
| Keep first row per group | `ROW_NUMBER()` + rank filter | Sort + `cumcount()` / `drop_duplicates()` |
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
- `AND`
- `OR`
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
- `COUNT(DISTINCT ...)`
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
- first-row-per-group patterns

### Date Logic

- `DATEDIFF()`
- exact day-gap validation
- date range filtering
- previous-row vs previous-day reasoning

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
- `AND` / `OR` filtering
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
- `nunique()`
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
- first-row-per-group logic
- window-like operations

### Date and Time Logic

- datetime subtraction
- `pd.Timedelta`
- previous-day validation
- date-range comparisons

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

The preferred solution is usually the **simplest correct approach that matches the requirement clearly**.

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
- multiple events occurring on the same earliest date,
- fewer than N values in Top-N problems,
- duplicate groups where only the minimum `id` should survive,
- days or groups with zero matching events,
- integer division when a decimal result is required,
- missing calendar dates when comparing adjacent rows,
- previous row vs actual previous calendar day,
- unique-entity counting vs row counting,
- filters that return no rows.

### Previous row vs previous calendar day

```text
2026-08-01
2026-08-03
```

After sorting, August 1 is the previous row for August 3, but it is **not yesterday**.

Therefore:

```text
SQL:
LAG() + DATEDIFF()

Pandas:
shift() + datetime subtraction + Timedelta
```

may be needed together.

### First value vs first row

```text
Need only the minimum value
→ MIN() / groupby().min()

Need columns from the row containing that value
→ ROW_NUMBER() / sort + cumcount()
```

### Row count vs unique entity count

```text
COUNT(*)
→ number of rows

COUNT(DISTINCT player_id)
→ number of unique players
```

Pandas equivalent:

```text
len(df)
→ rows

df["player_id"].nunique()
→ unique players
```

This distinction matters in retention and user-level metrics.

### Missing aggregate rows

A group may exist but have zero rows in a filtered subset.

Pandas:

```python
left merge + fillna(0)
```

can preserve the group.

SQL conditional aggregation can often avoid losing the group in the first place.

### Empty aggregate behavior

```text
Normal SELECT with no matching rows
→ zero rows

MAX() / MIN() over no matching rows
→ one row containing NULL
```

Pandas:

```python
empty_series.max()
empty_series.min()
```

returns:

```text
NaN
```

---

## Code Quality Principles

### SQL

- Uppercase SQL keywords
- Consistent indentation
- Meaningful aliases
- Explicit join conditions
- Readable window functions
- Clear conditional aggregation
- Safe decimal division for ratios
- Semicolons at statement boundaries
- Clear approach labels when multiple solutions are useful
- Prefer the simplest correct solution when extra complexity adds no value

### Python / Pandas

- PEP 8-style formatting
- Meaningful variable names
- Type hints where useful
- Readable transformations
- Minimal unnecessary comments
- Avoid overly complex one-liners
- Keep transformations aligned with the underlying data logic
- Prefer code that can be clearly explained in an interview

---

## Learning Goals

This repository is intended to strengthen my ability to:

- translate business and data requirements into queries,
- write SQL independently,
- recognize reusable SQL patterns,
- choose the correct join or aggregation strategy,
- use window functions confidently,
- distinguish value-level aggregation from row-level selection,
- distinguish row counts from unique-entity counts,
- use conditional aggregation correctly,
- reason about date continuity,
- calculate ratios correctly,
- handle duplicates and missing data,
- reason about zero-count and empty-result cases,
- manipulate DataFrames confidently,
- translate SQL logic into Pandas,
- compare multiple valid approaches when useful,
- choose the simplest appropriate approach,
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
