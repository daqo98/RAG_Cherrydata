from json import JSONDecodeError
from django.conf import settings
from django.http import JsonResponse
from .serializers import DatasetSerializer, DataQuerySerializer, InsightSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from .models import Dataset
from utils.chat_gpt import ChatGPTHandler

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
                print(f"serializer data {serializer.data}")
                return Response(serializer.data)
            else:
                print(f"serializer errors {serializer.errors}")
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

    def post(self, request):
        
        try:
            data = JSONParser().parse(request)
            print(f"data is: {data}")
            serializer = DataQuerySerializer(data=data)
            if serializer.is_valid(raise_exception=True):

                # Extract the prompt from the request data and call Chat-GPT
                user_prompt = data.get("user_prompt", "")
                chat_gpt_handler = ChatGPTHandler(user_prompt)
                data["chart_type"] = getattr(chat_gpt_handler,"chart_type")
                data["request_status"] = list(settings.REQUEST_STATUS_CHOICES.keys())[0]
                data["command_query"] = "[Insert Clickhouse query]" # chat_gpt_handler.generate_response()

                
                serializer = DataQuerySerializer(data=data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                #print(f"serializer data {serializer.data}")

                # TODO: Clickhouse query using Celery job - I should cache the id of the DataQueryRequest
                # in order to update the request status asynchronosuly
 
                return Response(serializer.data)
            else:
                print(f"serializer errors {serializer.errors}")
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

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                print(f"serializer data {serializer.data}")
                return Response(serializer.data)
            else:
                print(f"serializer errors {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)