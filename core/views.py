from celery.result import AsyncResult
from django.conf import settings
from django.http import JsonResponse
from json import JSONDecodeError
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from utils.chat_gpt import ChatGPTHandler
from .models import Dataset, DataQuery, DynamicChart, Insight
from .serializers import DatasetSerializer, DataQuerySerializer, InsightSerializer, DynamicChartSerializer
from .tasks import send_data_query_task, send_insight_query_task

class DatasetAPIView(views.APIView):
    """
    A simple APIView for creating Dataset entries.
    """
    serializer_class = DatasetSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = DatasetSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)

class DataQueryAPIView(views.APIView):
    """
    A simple APIView for creating DataQuery entries.
    """
    serializer_class = DataQuerySerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def get(self, request, pk, *args, **kwargs):
        try:
            data_query = DataQuery.objects.get(id=pk)
        except DataQuery.DoesNotExist:
            raise NotFound(detail=f"No data query with id={pk} matches")

        # Get the result using the Celery's task ID
        task_id = str(data_query.task_id)
        result = AsyncResult(task_id)
        
        if result.ready():
            table_data = result.result
            dyn_chart = DynamicChartSerializer(data_query.dynamicchart).data
            return Response({'result': table_data | dyn_chart}, status=status.HTTP_200_OK)
        else:
            return Response({'status': data_query.request_status}, status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            # Extract the prompt from the request data and call Chat-GPT
            user_prompt = data.get("user_prompt", "")
            data["request_status"] = list(settings.REQUEST_STATUS_CHOICES.keys())[0] # SUBMITTED
            serializer = DataQuerySerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()

                # Pass the id of the DataQueryRequest in order to update the request status async
                task = send_data_query_task.apply_async(args=(instance.id, user_prompt))
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)

class InsightAPIView(views.APIView):
    """
    A simple APIView for creating Insight entries.
    """
    serializer_class = InsightSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def get(self, request, pk, *args, **kwargs):
        try:
            insight_query = Insight.objects.get(id=pk)
            return Response(InsightSerializer(insight_query).data)
        except:
            raise NotFound(detail=f"There is no insight query with id={pk}")

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            # Extract the prompt from the request data and call Chat-GPT
            user_prompt = data.get("user_prompt", "")
            chat_gpt_handler = ChatGPTHandler(user_prompt)
            data["request_status"] = list(settings.REQUEST_STATUS_CHOICES.keys())[0] # SUBMITTED
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)

        
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            # TODO: Pass the id of the InsightQueryRequest in order to update the request status async
            task = send_insight_query_task.apply_async(args=(instance.id, user_prompt))
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class PersonalDashboardAPIView(views.APIView):
    """
    A simple APIView for obtaining the Dynamic Charts saved.
    """
    serializer_class = DynamicChartSerializer

    def get(self, request, *args, **kwargs):

        try:
            dyn_chart = DynamicChart.objects.filter(is_saved=True)
            serializer = DynamicChartSerializer(dyn_chart, many=True)
            return Response(serializer.data)
        except DynamicChart.DoesNotExist:
            raise NotFound(detail="No dynamic chart has been saved")
            #return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class TaskResultAPIView(views.APIView):
    def get(self, request, task_id, *args, **kwargs):
        result = AsyncResult(task_id)
        if result.ready():
            return Response({'result': result.result}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'Pending'}, status=status.HTTP_202_ACCEPTED)
