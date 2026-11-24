from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator

default_args = {"owner": "tam", "retries": 1, "retry_delay": timedelta(minutes=5)}

with DAG(
    "theory_v2",
    default_args=default_args,
    description="dag version 2 created by tam",
    schedule=timedelta(minutes=5),
    start_date=datetime(2026, 11, 20),
    tags=["theory"],
) as dag:
    print_hello_world_bash = BashOperator(
        task_id="print_hello_world_bash", bash_command="echo 'Hello, world'"
    )

    def print_hello_world():
        print("Hello, world (from .py)")

    print_hello_world_py = PythonOperator(
        task_id="print_hello_world_py",
        python_callable=print_hello_world,
    )

    print_hello_world_py.set_downstream(print_hello_world_bash)
