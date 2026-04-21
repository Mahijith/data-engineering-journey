# Day 1 — Python: Cleaning a CSV File

## Category
Python & Pandas

## Level
Beginner

## Problem Statement
You work as a junior data engineer at a retail company. Every morning, the sales team drops a CSV file into a shared folder. The file contains daily transaction records, but it's messy — some rows have missing values, column names have inconsistent spacing, and a date column is stored as plain text instead of a proper date type.

## Raw Data
```
 transaction_id , customer_id , amount , sale_date
1001, C001, 59.99, 2024-01-15
1002, C002, , 2024-01-15
1003, C003, 120.50, not-a-date
1004, , 89.00, 2024-01-16
1005, C005, 45.00, 2024-01-16
1006, C006, 200.00, 2024-01-17
1007, C007, , 2024-01-17
1008, C008, 33.75, bad-date
1009, , 78.00, 2024-01-18
1010, C010, 15.50, 2024-01-18
```

## Task
Write a Python script using pandas that:
1. Loads the CSV into a DataFrame
2. Strips whitespace from all column names
3. Converts `amount` to numeric so empty strings become NaN
4. Drops any rows where `amount` is missing
5. Converts `sale_date` to a proper datetime — rows where the date can't be parsed should become `NaT`
6. Prints the cleaned DataFrame

## Key Concepts Learned
- `df.columns.str.strip()` — strip whitespace from column names
- `pd.to_numeric(errors='coerce')` — convert to number, bad values become NaN
- `df.dropna(subset=[...])` — drop rows with missing values in specific columns
- `pd.to_datetime(errors='coerce')` — convert to datetime, bad values become NaT

## Solution File
`day01_cleaning_csv.py`
