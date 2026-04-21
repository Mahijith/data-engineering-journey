# Day 3 — Data Modeling: Star Schema Design

## Category
Data Modeling & Warehouse Design

## Level
Beginner

## Problem Statement
You've just joined a retail company as a data engineer. The analytics team complains that their database queries are too slow and hard to write. Your tech lead suggests redesigning the database using a Star Schema — a common data warehouse pattern built around fact tables and dimension tables.

## Flat Table (Before)
```
| order_id | customer_name | customer_city | product_name | category   | unit_price | quantity | order_date |
|----------|---------------|---------------|--------------|------------|------------|----------|------------|
| 1001     | Alice         | New York      | Laptop       | Electronic | 999.99     | 1        | 2024-01-15 |
| 1002     | Bob           | Chicago       | Phone        | Electronic | 499.99     | 2        | 2024-01-15 |
| 1003     | Alice         | New York      | Desk         | Furniture  | 249.99     | 1        | 2024-01-16 |
| 1004     | Carol         | Houston       | Laptop       | Electronic | 999.99     | 1        | 2024-01-16 |
```

## Task
Redesign this flat table into a Star Schema by:
1. Identifying what the fact table should contain (measurable, numeric events)
2. Identifying the dimension tables (descriptive context around the facts)
3. Writing `CREATE TABLE` SQL statements for `dim_customer`, `dim_product`, `dim_date`, and `fact_orders`
4. Making sure `fact_orders` references all three dimension tables via foreign keys

## Star Schema Structure
```
        dim_customer
             |
dim_date — fact_orders — dim_product
```

## Decision Rule
- "Can I measure or aggregate this?" → fact table (quantity, total_amount)
- "Does this describe something?" → dimension table (customer name, product category)

## Key Concepts Learned
- **Star Schema** — fact table in the center, dimension tables branching out
- **Fact table** — stores measurable events (orders, transactions, clicks)
- **Dimension table** — stores descriptive attributes (who, what, when, where)
- **dim_date** — breaking dates into parts (year, month, quarter) enables fast time-based filtering
- `DECIMAL(10, 2)` — always use for monetary values, never FLOAT
- `total_amount` is calculated in the ETL pipeline before loading — not computed in the table definition
- Star Schema is used in Snowflake, BigQuery, and Redshift every day in the industry

## Solution File
`day03_star_schema.sql`
