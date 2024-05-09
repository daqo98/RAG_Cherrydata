import uuid
from django.db import models


class Model(models.Model):
    # We use the pk when making calls to the API
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True # to inherit from it on other Model classes

class Chart(models.Model):
    title_xaxis = models.CharField(max_length=50)
    title_yaxis = models.CharField(max_length=50)
    #data_xaxis = models.ListField(models.FloatField())
    #data_yaxis = models.ArrayField(models.TextField(null=false))

    class Meta:
        abstract = True