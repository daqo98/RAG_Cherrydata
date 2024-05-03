from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel
)

class Dataset(TimeStampedModel, Model):

    class Meta:
        verbose_name_plural = "Datasets"
    
    path = models.FileField(upload_to ='uploads/') # file will be uploaded to MEDIA_ROOT / uploads
    context = models.TextField(null=True, blank=True)
    table_name = models.CharField(max_length=200)
    db_name = models.CharField(max_length=200)
    ready = models.BooleanField()

    def __str__(self):
        return f'{self.title}'
    
class RequestDataQuery(TimeStampedModel, ActivatorModel, Model):

    class Meta:
        verbose_name_plural = "RequestsDataQuery"

    user_prompt = models.TextField(null=False)
    chat_gpt_command_query = models.CharField(max_length=200)
    chat_gpt_command_chart = models.CharField(max_length=200)
    # Check correspondonce of status field of ActivatorModel w/ functionality desired

    def __str__(self):
        return f'{self.title}'

class RequestInsight(TimeStampedModel, ActivatorModel, Model):

    class Meta:
        verbose_name_plural = "RequestsInsight"

    user_prompt = models.TextField(null=False)
    activate_context = models.BooleanField()
    chat_gpt_response =  models.TextField(null=False)
    # Check correspondonce of status field of ActivatorModel w/ functionality desired
    
    def __str__(self):
        return f'{self.title}'

#TODO: DataExport, Chart, Summary, User