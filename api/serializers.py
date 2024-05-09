from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField, ListField


class DatasetSerializer(serializers.ModelSerializer):
    path = CharField(required=True)
    clickhouse_table_name = CharField(required=True)
    #column_names = ListField(child=CharField(), required=True)
    clickhouse_db_name = CharField(required=True)

    #'column_names',
    class Meta:
        model = models.Dataset
        fields = (
            'path',
            'clickhouse_table_name',
            'clickhouse_db_name',
        )