# Day 5 — ETL: Data Quality Checks Pipeline

## Category
ETL (Extract, Transform, Load)

## Level
Intermediate

## Problem Statement
You're a data engineer at a financial company. Every night a JSON file lands in your system containing bank transactions from multiple branches. Before loading this data into your data warehouse, you are responsible for ensuring data quality is acceptable. Bad data must be quarantined with a clear reason — not silently dropped.

## Data Quality Rules

| Rule | Description |
|------|-------------|
| No duplicate `transaction_id` | Each transaction must be unique |
| `amount` must be positive | No zero or negative amounts allowed |
| `branch_code` must be 3 characters | Exactly 3 uppercase letters e.g. NYC, CHI |
| No missing values in critical columns | `transaction_id`, `amount`, `branch_code` must never be null |

## Raw Data
```json
[
  {"transaction_id": "T001", "branch_code": "NYC", "amount": 1500.00, "date": "2024-01-15"},
  {"transaction_id": "T002", "branch_code": "CHI", "amount": -200.00, "date": "2024-01-15"},
  {"transaction_id": "T003", "branch_code": "NY",  "amount": 850.00,  "date": "2024-01-15"},
  {"transaction_id": "T001", "branch_code": "HOU", "amount": 3200.00, "date": "2024-01-16"},
  {"transaction_id": "T005", "branch_code": "CHI", "amount": 950.00,  "date": "2024-01-16"},
  {"transaction_id": "T006", "branch_code": "NYC", "amount": 0.00,    "date": "2024-01-16"},
  {"transaction_id": "T007", "branch_code": null,  "amount": 1100.00, "date": "2024-01-16"},
  {"transaction_id": "T008", "branch_code": "LAX", "amount": 2200.00, "date": "2024-01-17"}
]
```

## Task
Write a Python script that:
1. **Extracts** — loads the JSON data into a pandas DataFrame
2. **Runs data quality checks** — for each rule, identify rows that failed and why
3. **Separates** the data into two DataFrames:
   - `clean_df` — rows that passed all checks
   - `quarantine_df` — rows that failed at least one check, with a `failure_reason` column
4. **Saves** both DataFrames to CSV without index

## Expected Output
```
Clean rows: 2    (T005, T008)
Quarantined rows: 6

Quarantine failure reasons:
T001 → duplicate transaction_id
T002 → invalid amount
T003 → invalid branch_code
T001 → duplicate transaction_id
T006 → invalid amount
T007 → missing critical value | invalid branch_code
```

## Key Concepts Learned
- **Boolean masks** — pandas Series of True/False used to filter rows
- `df.isnull().any(axis=1)` — True if any column in a row is null
- `df.duplicated(subset=[], keep=False)` — flags ALL duplicate occurrences
- `df['col'] <= 0` — simple comparison creates a boolean mask
- `df['col'].str.len().fillna(0)` — get string length, treat nulls as 0
- `|` operator combines masks with OR logic
- `~` operator flips a mask (True becomes False and vice versa)
- `df.apply(func, axis=1)` — applies a function to each row
- Quarantine pattern — separating bad data with reasons is production best practice

## Solution File
`day05_data_quality_checks.py`
