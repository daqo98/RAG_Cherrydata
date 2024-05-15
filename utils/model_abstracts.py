import uuid
#from django.db import models
from clickhouse_backend import models

class Model(models.ClickhouseModel):
    # We use the pk when making calls to the API
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True # to inherit from it on other Model classes

class Chart(models.ClickhouseModel):
    title_xaxis = models.FixedStringField(max_bytes=50)
    title_yaxis = models.FixedStringField(max_bytes=50)
    #data_xaxis = models.ListField(models.FloatField())
    #data_yaxis = models.ArrayField(models.TextField(null=false))

    class Meta:
        abstract = True