from json import JSONDecodeError
from django.conf import settings
from django.http import JsonResponse
from .serializers import DatasetSerializer, DataQuerySerializer, InsightSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
import openai
from .models import Dataset

openai.api_key = settings.OPENAI_API_KEY

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


class ChatGPTAPIView(views.APIView):
    def post(self, request): #TODO: GET???
        # Extract the prompt from the request data
        data = JSONParser().parse(request)
        prompt = data.get("prompt", "")
        print(prompt)

        # Check if prompt is provided
        if not prompt:
            return Response({"error": "Prompt is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Call the ChatGPT API
        try:
            #response = self.generate_response(prompt)
            response = "Rome"
            return Response({"response": response}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def generate_response(self, prompt):
        response = openai.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        return response.choices[0].message.content.strip()


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
                serializer.save()
                print(f"serializer data {serializer.data}")
                # TODO: Make async call to Chat-GPT and handle request_status case
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