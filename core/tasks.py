from .models import DataQuery, DynamicChart, Insight
from celery import shared_task
from celery.result import AsyncResult
import clickhouse_connect
from django.conf import settings
import json
import sys
from time import sleep
from utils.chat_gpt import ChatGPTHandler


@shared_task(bind=True)
def send_data_query_task(self, request_id, user_prompt):

    print(f"request_id is: {request_id}")

    # Fetch object based on obj_id
    data_query_obj = DataQuery.objects.get(pk=request_id)

    data_query_obj.task_id = self.request.id # Save Celery's task_id in data query object

    chat_gpt_handler = ChatGPTHandler(user_prompt)
    data_query_obj.chart_type = chat_gpt_handler.extract_chart_type() #getattr(chat_gpt_handler,"chart_type")
    data_query_obj.command_query = "SELECT max(key), avg(metric) FROM new_table" # chat_gpt_handler.generate_response()

    # Update status to PROCESSING
    data_query_obj.request_status = list(settings.REQUEST_STATUS_CHOICES.keys())[1]
    
    data_query_obj.save()

    try:
        sleep(15)  # Simulate expensive operation(s) that freeze Django
        client = clickhouse_connect.get_client(host="localhost", username="default", password="", database="helloworld")
        result = client.query(data_query_obj.command_query)

        # Update status to COMPLETED
        data_query_obj.request_status = list(settings.REQUEST_STATUS_CHOICES.keys())[2]
        data_query_obj.save()

        sys.stdout.write("query: ["+ data_query_obj.command_query + "] returns:\n\n")
        print(f"column_names: {result.column_names}")
        print(f"result_columns: {result.result_columns}")
        #print(result.result_rows)

        # Creation of DynamicChart object
        # TODO: Check which columns to return as the x- and y-axis
        DynamicChart.objects.create(
            data_query=data_query_obj,
            title_xaxis="x",
            title_yaxis="y",
            data_xaxis=result.result_columns[0],
            data_yaxis=result.result_columns[1],
            chart_type=data_query_obj.chart_type,
            is_saved=False
            )

        table_data = [{'column_name': v1, 'column_values': v2} for v1, v2 in zip(result.column_names, result.result_columns)]

        return {'status': 'Task completed', 'table_data': table_data}

    except Exception as e:
        # Update status to FAILED
        data_query_obj.request_status = list(settings.REQUEST_STATUS_CHOICES.keys())[3]
        data_query_obj.save()
        print(e)

        return {'status': 'Task failed', 'result': e}


@shared_task(bind=True)
def send_insight_query_task(self, request_id, user_prompt):

    print(f"request_id is: {request_id}")

    # Fetch object based on obj_id
    insight_query_obj = Insight.objects.get(pk=request_id)

    insight_query_obj.task_id = self.request.id # Save Celery's task_id in data query object

    chat_gpt_handler = ChatGPTHandler(user_prompt)
    
    # Update status to PROCESSING
    insight_query_obj.request_status = list(settings.REQUEST_STATUS_CHOICES.keys())[1]
    insight_query_obj.save()
    
    try:
        insight_query_obj.gpt_response = "SELECT max(key), avg(metric) FROM new_table" # chat_gpt_handler.generate_response()

        # Update status to COMPLETED
        insight_query_obj.request_status = list(settings.REQUEST_STATUS_CHOICES.keys())[2]
        insight_query_obj.save()
    
    except:
        # Update status to FAILED
        insight_query_obj.request_status = list(settings.REQUEST_STATUS_CHOICES.keys())[3]
        insight_query_obj.save()

    print(f"insight_query_obj.gpt_response: {insight_query_obj.gpt_response}")

def get_task_status(task_id):
    result = AsyncResult(task_id)
    return {'status': result.status, 'result': result.result}