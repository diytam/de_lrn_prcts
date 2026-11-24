from datetime import timedelta, datetime
from airflow.sdk import dag, task

default_args = {
    "owner": "tam",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


@dag(
    dag_id="theory_v3",
    default_args=default_args,
    description="modern using dag",
    schedule="@daily",
    start_date=datetime(2026, 11, 11),
    tags=["theory"],
)
def task_flow():

    @task
    def print_hello_world() -> None:
        print("Hello world")

    @task
    def print_my_name(name: str) -> None:
        print(f"My name is {name}")

    @task
    def get_age() -> int:
        return 18

    @task
    def access_age(age: int) -> None:
        print(f"You need to have {age} year to get access to database")

    t1 = print_hello_world()
    t2 = print_my_name("Tam")
    t3 = access_age(get_age())

    t1 >> t2 >> t3


task_flow()
