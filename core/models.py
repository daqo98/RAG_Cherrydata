from django.conf import settings
from django.db import models as django_models
from clickhouse_backend import models
from utils.model_abstracts import Model, Chart
import uuid
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel
)

#TODO: User

class Dataset(Model):

    class Meta:
        verbose_name_plural = "Datasets"
    
    created = models.DateTime64Field(auto_now_add=True)
    modified = models.DateTime64Field(auto_now=True)
    # models.FileField(upload_to ='uploads/') # file will be uploaded to MEDIA_ROOT / uploads
    path = models.FixedStringField(max_bytes=256)
    clickhouse_db_name = models.FixedStringField(max_bytes=200)
    clickhouse_table_name = models.FixedStringField(max_bytes=200)
    column_names = models.ArrayField(base_field=models.FixedStringField(max_bytes=256), default=list)
    context = models.StringField(null=False, default="")
    # ready = models.BoolField()

    def __str__(self):
        return f'{self.clickhouse_table_name}'

class SummaryData(Model):

    dataset = django_models.OneToOneField(
        Dataset,
        on_delete=django_models.CASCADE,
        primary_key=False,
    )
    
    metrics =  models.ArrayField(base_field=models.FixedStringField(max_bytes=256), default=list)
    values =  models.ArrayField(base_field=models.Float64Field(), default=list)

    def __str__(self):
        return f'{self.id}' #TODO: list of metrics?
    
class DataQuery(Model):

    class Meta:
        verbose_name_plural = "DataQueries"

    created = models.DateTime64Field(auto_now_add=True)
    dataset = django_models.ForeignKey(Dataset, on_delete=django_models.CASCADE)
    user_prompt = models.StringField(null=False)
    command_query = models.StringField(null=False)
    chart_type = models.FixedStringField(max_bytes=50, default="pie")
    request_status = models.FixedStringField(max_bytes=10, choices=settings.REQUEST_STATUS_CHOICES)
    task_id = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return f'{self.id}'

class Insight(Model):

    class Meta:
        verbose_name_plural = "Insights"

    created = models.DateTime64Field(auto_now_add=True)
    dataset = django_models.ForeignKey(Dataset, on_delete=django_models.CASCADE)
    user_prompt = models.StringField(null=False)
    activate_context = models.BoolField(default=False) #TODO
    gpt_response =  models.StringField(null=False)
    request_status = models.FixedStringField(max_bytes=10, choices=settings.REQUEST_STATUS_CHOICES)
    
    def __str__(self):
        return f'{self.id}'

class ExportTable(Model):
    class Meta:
        verbose_name_plural = "ExportTables"

    data_query = django_models.OneToOneField(
        DataQuery,
        on_delete=django_models.CASCADE,
        primary_key=False,
    )

    file_type = models.FixedStringField(max_bytes=10)
    url = models.StringField(null=False)
    request_status = models.FixedStringField(max_bytes=10, choices=settings.REQUEST_STATUS_CHOICES)

    def __str__(self):
        return f'{self.id}'


class StaticChart(Chart):
    class Meta:
        verbose_name_plural = "StaticCharts"
    
    dataset = django_models.OneToOneField(
        Dataset,
        on_delete=django_models.CASCADE,
        primary_key=False,
    )
    
    def __str__(self):
        return f'{self.id}'#TODO: List of graphs

class DynamicChart(Chart):
    # TODO: Reverse relation w/ DataQuery
    data_query = django_models.OneToOneField(
        DataQuery,
        on_delete=django_models.CASCADE,
        primary_key=False,
    )

    chart_type = models.FixedStringField(max_bytes=50)
    is_saved = models.BoolField()

    def __str__(self):
        return f'{self.chart_type}'