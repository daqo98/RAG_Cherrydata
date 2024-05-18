from .models import DataQuery, DynamicChart
from celery import shared_task
from celery.result import AsyncResult
import clickhouse_connect
from django.conf import settings
import json
import sys
from time import sleep


@shared_task(bind=True)
def send_query_clickhouse_task(self, request_id, query):

    print(f"request_id is: {request_id}")

    # Fetch object based on obj_id
    data_query_obj = DataQuery.objects.get(pk=request_id)

    # Update status to PROCESSING
    data_query_obj.request_status = list(settings.REQUEST_STATUS_CHOICES.keys())[1]
    data_query_obj.save()

    try:
        sleep(5)  # Simulate expensive operation(s) that freeze Django
        client = clickhouse_connect.get_client(host="localhost", username="default", password="", database="helloworld")
        result = client.query(query)

        # Update status to COMPLETED
        data_query_obj.request_status = list(settings.REQUEST_STATUS_CHOICES.keys())[2]
        data_query_obj.save()

        sys.stdout.write("query: ["+ query + "] returns:\n\n")
        print(f"column_names: {result.column_names}")
        print(f"result_columns: {result.result_columns}")
        #print(result.result_rows)

        # Creation of DynamicChart object
        DynamicChart.objects.create(
            data_query=data_query_obj,
            title_xaxis="x",
            title_yaxis="y",
            data_xaxis=result.result_columns[0],
            data_yaxis=result.result_columns[1],
            chart_type=data_query_obj.chart_type,
            is_saved=False
            )

    except Exception as e:
        # Update status to FAILED
        data_query_obj.request_status = list(settings.REQUEST_STATUS_CHOICES.keys())[3]
        data_query_obj.save()
        print(e)

    return {'status': 'Task completed', 'result': "DONEEEEE"}


def get_task_status(task_id):
    result = AsyncResult(task_id)
    return {'status': result.status, 'result': result.result}