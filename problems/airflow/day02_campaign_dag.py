# Day 2: Airflow DAG — Daily Campaign Report
# Requires Apache Airflow to be installed and running

from airflow import DAG 
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default arguments applied to all tasks
default_args = {
    'owner': 'data_engineer',
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

# DAG definition
with DAG(
    dag_id='daily_campaign_report',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule='0 7 * * *',  # Every day at 7:00 AM
    catchup=False                    # Don't backfill past runs
) as dag:

    # Task: run the report script
    run_report = BashOperator(
        task_id='run_report',
        bash_command='python report.py'
    )

# Cron reference:
# 0 7 * * *   = Every day at 7:00 AM
# 0 9 * * 1-5 = Weekdays at 9:00 AM
# 0 0 1 * *   = First day of every month
