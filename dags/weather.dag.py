# weather.dag.py (versão com imports diretos)
from datetime import datetime, timedelta
from airflow.decorators import dag, task
import logging

# Import direto - mesmos arquivos na pasta dags/
from extract_data import extract_weather_data
from transform_data import data_transformations
from load_data import load_weather_data

# ============================================
# CONFIGURAÇÃO DA DAG
# ============================================

default_args = {
    'owner': 'marielle',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

@dag(
    dag_id='weather_pipeline',
    default_args=default_args,
    description='Pipeline de dados meteorológicos',
    schedule_interval='0 */6 * * *',
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=['weather', 'etl'],
)
def weather_pipeline():

    @task(task_id='extract_weather')
    def extract():
        API_KEY = '7ecc4e957b421d2f09504c3e30ec90bf'
        url = f'https://api.openweathermap.org/data/2.5/weather?q=Sao Paulo,BR&units=metric&appid={API_KEY}'
        return extract_weather_data(url)

    @task(task_id='transform_weather')
    def transform():
        return data_transformations()

    @task(task_id='load_weather')
    def load(df):
        load_weather_data('sp_weather', df)

    # Extract → Transform → Load
    raw_data = extract()
    transformed_data = transform()
    load(transformed_data)

dag = weather_pipeline()