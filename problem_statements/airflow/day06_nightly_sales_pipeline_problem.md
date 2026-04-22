# Day 6 — Airflow: Multi-Step Pipeline with PythonOperator

## Category
Workflow Orchestration (Apache Airflow)

## Level
Intermediate

## Problem Statement
You're a data engineer at an e-commerce company. Every night at midnight, three things need to happen in order:
1. Raw sales data is extracted from an API and saved to a CSV
2. That CSV is cleaned and transformed
3. The cleaned data is loaded into a data warehouse table

Your manager wants this automated in Airflow as a proper multi-step pipeline where each step only runs if the previous one succeeded.

## Task
Write an Airflow DAG that:
1. Is named `nightly_sales_pipeline`
2. Runs every day at midnight (`0 0 * * *`)
3. Starts from `2024-01-01` with `catchup=False`
4. Has 3 tasks using `PythonOperator`:
   - `extract_data` — prints "Extracting sales data..."
   - `transform_data` — prints "Transforming sales data..."
   - `load_data` — prints "Loading into warehouse..."
5. Tasks must run in order — extract → transform → load
6. Retries set to 3 with retry delay of 10 minutes

## Task Dependency Diagram
```
extract_data >> transform_data >> load_data
```

## Key Concepts Learned
- **PythonOperator** — runs a Python function as an Airflow task
- `python_callable` — points to the function the task should execute
- `>>` operator — chains tasks in order, task2 only runs if task1 succeeds
- Multi-step pipelines model real production ETL workflows
- Each task is independently retried if it fails
- `schedule` replaces `schedule_interval` in newer Airflow versions (2.4+)

## Difference from Day 2
| Day 2 | Day 6 |
|-------|-------|
| Single task | Multiple dependent tasks |
| BashOperator | PythonOperator |
| Runs a shell command | Runs a Python function |
| No task dependencies | Tasks chained with >> |

## Tools Required
- Docker Desktop
- Astro CLI (`astro dev start`)
- Airflow UI at `http://localhost:8080`
- Default credentials: admin / admin

## Solution File
`day06_nightly_sales_pipeline.py`
