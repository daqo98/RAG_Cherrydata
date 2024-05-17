import clickhouse_connect
import sys
import json
from celery import shared_task
from time import sleep


@shared_task()
def send_query_clickhouse_task():
    sleep(20)  # Simulate expensive operation(s) that freeze Django
    client = clickhouse_connect.get_client(host="localhost", username="default", password="", database="helloworld")

    QUERY = "SELECT max(key), avg(metric) FROM new_table"

    result = client.query(QUERY)

    sys.stdout.write("query: ["+QUERY + "] returns:\n\n")
    print(result.result_rows)