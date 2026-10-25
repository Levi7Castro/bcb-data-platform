from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="pipeline_bcb",
    schedule="@daily",
    start_date=datetime(2026, 10, 1),
    catchup=False,
) as dag:

    load_bronze = BashOperator(
        task_id="load_bronze",
        bash_command="/usr/local/airflow/venvs/airbyte/bin/python load_bronze.py",
        cwd="/usr/local/airflow/include/airbyte",
    )

    dbt_build = BashOperator(
        task_id="dbt_build",
        bash_command="/usr/local/airflow/venvs/dbt/bin/dbt build",
        cwd="/usr/local/airflow/include/dbt/bcb_analytics",
    )

    load_bronze >> dbt_build
