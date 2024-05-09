from django.db import models
from utils.model_abstracts import Model, Chart
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel
)

# key -> value in model, value -> human-readable
REQUEST_STATUS_CHOICES = {
    "SUBMITTED": "Submitted",
    "PROCESSING": "Processing",
    "COMPLETED": "Completed",
    "FAILED": "Failed"
}

class Dataset(TimeStampedModel, Model):

    class Meta:
        verbose_name_plural = "Datasets"
    
    # models.FileField(upload_to ='uploads/') # file will be uploaded to MEDIA_ROOT / uploads
    path = models.CharField(max_length=256)
    clickhouse_table_name = models.CharField(max_length=200)
    #column_names = ArrayField(models.CharField(max_length=256))
    clickhouse_db_name = models.CharField(max_length=200)
    # ready = models.BooleanField()

    def __str__(self):
        return f'{self.clickhouse_table_name}'

class SummaryData(Model):

    dataset = models.OneToOneField(
        Dataset,
        on_delete=models.CASCADE,
        primary_key=False,
    )
    
    #metrics =  models.ArrayField(models.CharField(max_length=256))
    #values =  models.ArrayField(models.FloatField())

    def __str__(self):
        return f'{self.name}'
    
class DataQuery(TimeStampedModel, ActivatorModel, Model):

    class Meta:
        verbose_name_plural = "DataQueries"

    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    user_prompt = models.TextField(null=False)
    command_query = models.TextField(null=False)
    # command_chart = models.CharField(max_length=200)
    request_status = models.CharField(max_length=10, choices=REQUEST_STATUS_CHOICES)
    # Check correspondence of status field of ActivatorModel w/ functionality desired

    def __str__(self):
        return f'{self.name}'

class Insight(TimeStampedModel, ActivatorModel, Model):

    class Meta:
        verbose_name_plural = "Insights"

    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    user_prompt = models.TextField(null=False)
    activate_context = models.BooleanField()
    gpt_response =  models.TextField(null=False)
    request_status = models.CharField(max_length=10, choices=REQUEST_STATUS_CHOICES)
    # Check correspondence of status field of ActivatorModel w/ functionality desired
    
    def __str__(self):
        return f'{self.name}'

#TODO: DataExport, Chart, Summary, User

class ExportTable(Model):
    class Meta:
        verbose_name_plural = "ExportTables"

    data_query = models.OneToOneField(
        DataQuery,
        on_delete=models.CASCADE,
        primary_key=False,
    )

    file_type = models.CharField(max_length=10)
    url = models.TextField(null=False)
    request_status = models.CharField(max_length=10, choices=REQUEST_STATUS_CHOICES)

    def __str__(self):
        return f'{self.name}'


class StaticChart(Chart):
    class Meta:
        verbose_name_plural = "StaticCharts"
    
    dataset = models.OneToOneField(
        Dataset,
        on_delete=models.CASCADE,
        primary_key=False,
    )
    
    def __str__(self):
        return f'{self.dataset}'

class DynamicChart(Chart):

    data_query = models.OneToOneField(
        DataQuery,
        on_delete=models.CASCADE,
        primary_key=False,
    )

    chart_type = models.CharField(max_length=10)
    is_saved = models.BooleanField()

    def __str__(self):
        return f'{self.chart_type}'