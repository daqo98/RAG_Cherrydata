from django.contrib import admin
from .models import Dataset, DataQuery


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'modified', 'clickhouse_table_name', 'clickhouse_db_name')

@admin.register(DataQuery)
class DataQueryAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'dataset', 'user_prompt', 'command_query', 'chart_type', 'request_status')

