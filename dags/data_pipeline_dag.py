from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from datetime import datetime, timedelta

default_args = {
    'owner': 'abhay',
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
}

def failure_callback(context):
    print(f"Task failed: {context['task_instance_key_str']}")


with DAG(
    dag_id='data_pipeline_project',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    on_failure_callback=failure_callback
) as dag:

    extract = BashOperator(
        task_id='extract_task',
        bash_command='python3 /mnt/c/Users/abhay/data-pipeline-project/scripts/extract.py'
    )

    transform = BashOperator(
        task_id='transform_task',
        bash_command='python3 /mnt/c/Users/abhay/data-pipeline-project/scripts/transform.py'
    )

    load = BashOperator(
        task_id='load_task',
        bash_command='python3 /mnt/c/Users/abhay/data-pipeline-project/scripts/load.py'
    )

    extract >> transform >> load
