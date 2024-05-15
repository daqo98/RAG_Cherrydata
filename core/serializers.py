from .models import Dataset, DataQuery, Insight
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField, ListField, ChoiceField, BooleanField
from collections import OrderedDict
from rest_framework.exceptions import APIException
from django.conf import settings


class DatasetSerializer(serializers.ModelSerializer):
    path = CharField(required=True)
    clickhouse_db_name = CharField(required=True)
    clickhouse_table_name = CharField(required=True)
    #column_names = ListField(child=CharField(), required=True)

    #'column_names',
    class Meta:
        model = Dataset
        fields = (
            'created',
            'modified',
            'path',
            'clickhouse_db_name',
            'clickhouse_table_name',
            'column_names',
            'context',
        )

class DataQuerySerializer(serializers.ModelSerializer):
    #dataset = serializers.PrimaryKeyRelatedField(queryset=Dataset.objects.all(), many=False)
    dataset = serializers.SlugRelatedField(
        queryset=Dataset.objects.all(), 
        slug_field="clickhouse_table_name", 
        many=False
        )
    command_query = CharField(required=False)
    request_status = ChoiceField(choices=settings.REQUEST_STATUS_CHOICES, required=False)


    #'column_names',
    class Meta:
        model = DataQuery
        fields = (
            'created',
            'dataset',
            'user_prompt',
            'command_query',
            'chart_type',
            'request_status',
        )

class InsightSerializer(serializers.ModelSerializer):
    dataset = serializers.SlugRelatedField(
            queryset=Dataset.objects.all(), 
            slug_field="clickhouse_table_name", 
            many=False
        )
    activate_context = BooleanField(required=False) #TODO: Double-check
    gpt_response = CharField(required=False)
    request_status = ChoiceField(choices=settings.REQUEST_STATUS_CHOICES, required=False)

    class Meta:
        model = Insight
        fields = (
            'created',
            'dataset',
            'user_prompt',
            'activate_context',
            'gpt_response',
            'request_status',
        )