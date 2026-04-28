# Day 7 — PySpark: Your First Spark Job

## Category
Apache Spark & Distributed Processing

## Level
Intermediate

## Problem Statement
You've just been handed your first Spark task at a ride-sharing company. The data team processes millions of trip records daily and uses PySpark instead of pandas because the data is too large to fit in memory on a single machine.

You've been given a sample dataset of trip records and asked to write a PySpark job that analyzes it.

## Raw Data
```
trip_id | driver_id | city     | distance_km | fare_usd | status
T001    | D001      | New York | 5.2         | 12.50    | completed
T002    | D002      | Chicago  | 3.1         | 8.00     | cancelled
T003    | D001      | New York | 8.7         | 21.00    | completed
T004    | D003      | Chicago  | 2.5         | 6.50     | completed
T005    | D002      | New York | 6.3         | 15.00    | cancelled
T006    | D003      | New York | 4.1         | 10.00    | completed
T007    | D001      | Chicago  | 9.2         | 22.50    | completed
T008    | D002      | Chicago  | 1.8         | 5.00     | cancelled
```

## Task
Write a PySpark script that:
1. Creates a Spark session
2. Loads the data into a Spark DataFrame using `spark.createDataFrame()`
3. Filters to keep only completed trips
4. Calculates total fare and average distance per city
5. Sorts results by total fare descending
6. Shows the final result using `.show()`

## Expected Output
```
+--------+----------+------------------+
|    city|total_fare|  avg_distance    |
+--------+----------+------------------+
|New York|     43.50|              6.0 |
| Chicago|     29.00|              5.85|
+--------+----------+------------------+
```

## Key Concepts Learned
- **SparkSession** — the entry point to all Spark functionality
- `spark.createDataFrame(data, schema)` — create a DataFrame from Python data
- `df.filter()` — filter rows based on a condition
- `df.groupBy()` — group rows by a column
- `.agg()` — apply multiple aggregations at once
- `sum()`, `avg()` — must be imported from `pyspark.sql.functions`, not Python built-ins
- `.alias()` — rename a column in the result
- `df.orderBy('col', ascending=False)` — sort results
- `.show()` — display the DataFrame results

## PySpark vs Pandas Comparison
| Operation | Pandas | PySpark |
|-----------|--------|---------|
| Filter | `df[df['col'] == val]` | `df.filter(df['col'] == val)` |
| Group by | `df.groupby('col')` | `df.groupBy('col')` |
| Aggregate | `.agg({'col': 'sum'})` | `.agg(sum('col').alias('total'))` |
| Sort | `df.sort_values('col')` | `df.orderBy('col')` |
| Show | `print(df)` | `df.show()` |

## Why PySpark Over Pandas?
- Pandas loads ALL data into memory on ONE machine
- PySpark distributes data across MANY machines
- Used at Uber, Netflix, Airbnb to process billions of records daily
- When data exceeds ~10GB, pandas struggles — PySpark scales infinitely

## Setup
```python
!pip install pyspark  # in Google Colab
```

## Solution File
`day07_pyspark_trip_analysis.py`
