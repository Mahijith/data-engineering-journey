# Day 2 — Airflow: Scheduling a Daily Pipeline

## Category
Workflow Orchestration (Apache Airflow)

## Level
Beginner

## Problem Statement
You're a junior data engineer at a marketing company. Your team runs a Python script every day that pulls yesterday's campaign data from a CSV and prints a summary report. Your manager wants you to automate this using Apache Airflow so it runs every day at 7:00 AM without anyone manually triggering it.

## Task
Write an Airflow DAG that:
1. Is named `daily_campaign_report`
2. Starts from `2024-01-01`
3. Runs every day at 7:00 AM
4. Has a single task called `run_report` that uses a `BashOperator` to execute `python report.py`
5. Has retries set to 2 with a retry delay of 5 minutes

## Cron Expression Reference
```
┌─────── minute
│ ┌───── hour
│ │ ┌─── day of month
│ │ │ ┌─ month
│ │ │ │ └ day of week
│ │ │ │ │
0 7 * * *   = Every day at 7:00 AM
0 9 * * 1-5 = Weekdays at 9:00 AM
0 0 1 * *   = First day of every month
```

## Key Concepts Learned
- **DAG** (Directed Acyclic Graph) — the container that holds all tasks in a pipeline
- **Operator** — a single unit of work (BashOperator, PythonOperator, etc.)
- **Task** — an instance of an operator inside a DAG
- **schedule_interval** — cron expression defining when the DAG runs
- **default_args** — shared settings applied to all tasks (retries, owner, etc.)
- **catchup=False** — prevents Airflow from backfilling missed runs since start_date
- **timedelta** — used to express time durations like retry_delay
- Task order is defined using `>>` operator: `task1 >> task2 >> task3`

## Tools Required
- Apache Airflow (install via Astro CLI + Docker for local development)
- Run `astro dev init` and `astro dev start` to get a local Airflow environment

## Solution File
`day02_campaign_dag.py`
