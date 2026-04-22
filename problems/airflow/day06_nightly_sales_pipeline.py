from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data_engineer',
    'retries': 3,
    'retry_delay': timedelta(minutes=10)
}

def extract():
    print("Extracting sales data...")

def transform():
    print("Transforming sales data...")

def load():
    print("Loading into warehouse...")

with DAG(
    dag_id='nightly_sales_pipeline',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule='0 0 * * *',
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load
    )

    extract_task >> transform_task >> load_task