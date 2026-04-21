# Day 1 — Python: Saving Cleaned Data to Multiple Formats

## Category
Python & Pandas

## Level
Beginner

## Problem Statement
You're the same junior data engineer from the CSV cleaning task. After cleaning the transactions file, your manager asks you to save the cleaned data in two formats for different teams:
- A CSV file for the business team (they use Excel)
- A JSON file for the backend team (they consume it via an API)

## Requirements
- The CSV should NOT include the row index numbers (0, 1, 2...) — they confuse the business team
- The JSON should be formatted so that each row is its own object, oriented by records

## Task
Starting from your already-cleaned DataFrame, write code that:
1. Saves the DataFrame to `cleaned_transactions.csv` without the index
2. Saves the DataFrame to `cleaned_transactions.json` where each row is a separate JSON object

## Key Concepts Learned
- `df.to_csv(filename, index=False)` — save to CSV without row index
- `df.to_json(filename, orient='records')` — save to JSON with each row as an object
- `orient='records'` produces: `[{"col": val, ...}, {"col": val, ...}]`

## Solution File
`day01_saving_formats.py`
