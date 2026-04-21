# Day 4 — SQL: Querying a Star Schema

## Category
SQL & Query Optimization

## Level
Intermediate

## Problem Statement
You're now working with the Star Schema you designed on Day 3. The analytics team comes to you with 3 business questions they need answered. Your job is to write SQL queries that join the fact and dimension tables to produce meaningful insights.

## Schema
```
        dim_customer
             |
dim_date — fact_orders — dim_product
```

## Task
Write SQL queries to answer these 3 business questions:

### Query 1 — Total revenue per product category
> "How much total revenue did each product category generate?"

### Query 2 — Top customer by total spending
> "Which customer spent the most money overall?"

### Query 3 — Monthly revenue trend
> "What was the total revenue for each month in 2024, ordered chronologically?"

## Rules
- You must JOIN fact and dimension tables — don't query just one table
- Use `GROUP BY` and `ORDER BY` appropriately
- Use table aliases to keep queries readable

## Mental Checklist for Writing Queries
```
What do I want to see?        → SELECT
Where is the data?            → FROM + JOIN
How do I group it?            → GROUP BY
How do I filter it?           → WHERE / HAVING
How do I sort it?             → ORDER BY
How many rows do I want?      → LIMIT
```

## Key Concepts Learned
- Always join outward from the fact table to dimension tables
- `SUM()` aggregates revenue across grouped rows
- `GROUP BY` is required whenever you use an aggregate function
- `ORDER BY col DESC` + `LIMIT 1` finds the top record
- `WHERE year = 2024` filters before aggregation
- Table aliases (`fo`, `dp`, `dc`) make multi-join queries readable
- `ORDER BY` always needs a column name — `ORDER BY DESC` alone is invalid

## Solution File
`day04_star_schema_queries.sql`
