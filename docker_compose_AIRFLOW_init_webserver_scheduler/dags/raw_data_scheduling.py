from airflow import DAG
import pendulum
from datetime import datetime, timedelta
from google.cloud import storage
import google.cloud.storage
import pandas as pd
import json
import sys
import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from google.cloud import storage
from datetime import datetime
import google.cloud.storage
from io import StringIO  
import pandas as pd
import numpy as np
import json
import sys
import os
import pyarrow.parquet as pq
import gcsfs
#from googletrans import Translator
import time
import os
import pandas as pd

import time 
import requests
import pandas as pd
from airflow.utils import timezone


import pendulum


# now = timezone.utcnow()
# a_date = timezone.datetime(2017, 1, 1)


default_args = {
    'owner':'Zhang_Yuan',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}
local_tz_brazil = pendulum.timezone("America/Sao_Paulo")
def main():
    # Define the URL to which we want to make the request
    url = 'https://jsonplaceholder.typicode.com/posts/1'

    # Make a GET request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    data_list = []
    if response.status_code == 200:
        while True:
        # print("Request was successful!")
        # print("Response JSON data:", response.json())  # Print the response JSON content
            if response.status_code:
                #print(response.json())
                    # Exit the loop after printing the response
                data = response.json()
                data_list.append(data)

                # print('data')
                #df = pd.DataFrame([data])

                time.sleep(180)
                # print(data_list)  

                df = pd.DataFrame([data_list])

                # Optionally save the DataFrame to a CSV file
                #df.to_csv('response_data.csv', mode='a', header=False, index=False)
                df.to_csv('./dags/response_data.csv', mode='a', header=False, index=False)

                # print(df)
            #break
    else:
        print(f"Request failed with status code {response.status_code}")
    return

# Calcula o start_date para 3 minutos no futuro
# start_time = datetime.now() + timedelta(minutes=3)

with DAG(
        default_args = default_args,
        dag_id = 'asdadas3',
        description = 'iasd',
        #start_date = datetime(2022, 1, 1),
        #start_date = datetime(2024, 11, 6, 13, 20),
        start_date=pendulum.datetime(2024, 11, 6, 10, 40, 0, tz=local_tz_brazil),
        #schedule_interval='@daily
        #schedule_interval=None  # Mudança aqui para executar apenas uma vez
        #schedule = '@daily',
        schedule = '*/5 * * * *',
        catchup=False
    ) as dag:
        start_task = DummyOperator(task_id='start_lnd', dag=dag)
        task1 = PythonOperator(task_id = 'NLP_POSTS_UNITED',python_callable = main)
        end_task = DummyOperator(task_id='end_lnd', dag=dag)
                              
start_task >> task1 >> end_task


# local_tz_brazil = pendulum.timezone("America/Sao_Paulo")
# start_date = pendulum.datetime(2024, 11, 6, 0, 0, 0, tz=local_tz_brazil)