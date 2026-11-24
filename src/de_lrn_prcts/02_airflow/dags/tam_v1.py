from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

default_args = {"owner": "tam", "retries": 1, "retry_delay": timedelta(minutes=5)}

dag = DAG(
    "dag_by_tam_v1",
    default_args=default_args,
    description="DAG, v1, created by tam",
    schedule="@daily",
    start_date=datetime(2026, 11, 22),
    tags=["theory"],
)


def print_text(text: str) -> None:
    print(f"Text is: {text}")


print_some_text = PythonOperator(
    task_id="print_text_v1",
    python_callable=print_text,
    op_kwargs={"text": "created first dag"},
    dag=dag,
)
