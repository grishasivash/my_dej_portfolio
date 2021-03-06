from airflow import DAG
from airflow.utils.dates import days_ago

from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from g_sivash_4_plugins.g_sivash_4_top3_operator import SivashTopFromRickAndMorty

GP_TABLE_NAME = 'g_sivash_4_ram_location'
GP_CONN_ID = 'conn_greenplum_write'

DEFAULT_ARGS = {
    'owner': 'g-sivash-4',
    'start_date': days_ago(2),
    'poke_interval': 600
}

dag = DAG("g-sivash-4-hw3",
          schedule_interval='@daily',
          default_args=DEFAULT_ARGS,
          max_active_runs=1
          )

start = DummyOperator(task_id='start', dag=dag)

create_table = PostgresOperator(
    task_id='create_table',
    sql=f"""CREATE TABLE IF NOT EXISTS {GP_TABLE_NAME} (
            id  SERIAL4 PRIMARY KEY,
            name VARCHAR NOT NULL,
            type VARCHAR NOT NULL,
            dimension VARCHAR NOT NULL,
            resident_count INT4 NOT NULL);""",
    postgres_conn_id=GP_CONN_ID,
    dag=dag
    )

delete_rows = PostgresOperator(
    task_id='delete_rows',
    postgres_conn_id=GP_CONN_ID,
    sql=f"DELETE FROM {GP_TABLE_NAME};",
    autocommit=True,
    dag=dag
)

load_top_locations = SivashTopFromRickAndMorty(
    task_id='load_top_locations',
    table_name=GP_TABLE_NAME,
    dag=dag
)

end = DummyOperator(task_id='end', dag=dag)

start >> create_table >> delete_rows>> load_top_locations >> end
