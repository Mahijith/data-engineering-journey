# Day 1 — SQL: Relational Schema Design

## Category
SQL & Database Design

## Level
Beginner

## Problem Statement
You've just joined a small e-commerce startup as a data engineer. The team currently stores all their data in spreadsheets. Your first task is to design a simple relational database schema for their order management system.

## Business Requirements
The business tracks the following information:
- **Customers** — name, email, signup date
- **Products** — name, price, category
- **Orders** — which customer placed it, when, total amount
- **Order Items** — which products were in each order, quantity, price at time of purchase

## Task
1. Identify the tables you need
2. Define the columns for each table including data types
3. Identify the primary key for each table
4. Define the foreign keys that link tables together
5. Write it all out as SQL `CREATE TABLE` statements

## Key Concepts Learned
- Primary keys uniquely identify each row in a table
- Foreign keys link tables together and enforce referential integrity
- `DECIMAL(10, 2)` is the correct type for money — never use `FLOAT` for currency
- `DATE` is the correct type for dates — never use `INT`
- `NOT NULL` ensures critical fields can never be empty
- `UNIQUE` ensures no duplicate values in a column (e.g. email)
- Composite primary keys `PRIMARY KEY (col1, col2)` enforce uniqueness across two columns

## Solution File
`day01_schema_design.sql`
