from django.contrib import admin
from .models import Dataset, DataQuery, Insight


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created', 
        'modified', 
        'clickhouse_db_name', 
        'clickhouse_table_name', 
        'column_names',
        'context',
    )

@admin.register(DataQuery)
class DataQueryAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'dataset', 'user_prompt', 'command_query', 'chart_type', 'request_status')

@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'created',
            'dataset',
            'user_prompt',
            'activate_context',
            'gpt_response',
            'request_status',
        )