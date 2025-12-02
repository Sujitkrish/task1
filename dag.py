from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Step 1: Extract
def extract_data(**kwargs):
    print("Extracting data from source system...")
    data = {"records": [1, 2, 3, 4, 5]}
    return data

# Step 2: Transform
def transform_data(**kwargs):
    ti = kwargs['ti']
    extracted = ti.xcom_pull(task_ids='extract_task')
    transformed = [x * 10 for x in extracted['records']]
    print(f"Transformed data: {transformed}")
    return transformed

# Step 3: Load
def load_data(**kwargs):
    ti = kwargs['ti']
    transformed = ti.xcom_pull(task_ids='transform_task')
    print(f"Loading data into database: {transformed}")
    # Here you’d insert into SQL/NoSQL DB
    return "Load successful"

# Default DAG arguments
default_args = {
    'owner': 'sujit',
    'depends_on_past': False,
    'email': ['alerts@bankingcompany.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
with DAG(
    dag_id='etl_pipeline_dag',
    default_args=default_args,
    description='Simple ETL pipeline using Airflow',
    schedule_interval='@daily',
    start_date=datetime(2025, 12, 1),
    catchup=False,
    tags=['etl', 'pipeline', 'banking']
) as dag:

    extract_task = PythonOperator(
        task_id='extract_task',
        python_callable=extract_data,
        provide_context=True
    )

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform_data,
        provide_context=True
    )

    load_task = PythonOperator(
        task_id='load_task',
        python_callable=load_data,
        provide_context=True
    )

    # Set task dependencies
    extract_task >> transform_task >> load_task