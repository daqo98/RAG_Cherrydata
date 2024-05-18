import uuid
#from django.db import models
from clickhouse_backend import models

class Model(models.ClickhouseModel):
    # We use the pk when making calls to the API
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True # to inherit from it on other Model classes

class Chart(Model):
    title_xaxis = models.FixedStringField(max_bytes=50)
    title_yaxis = models.FixedStringField(max_bytes=50)
    data_xaxis = models.ArrayField(base_field=models.Float64Field(), default=list)
    data_yaxis = models.ArrayField(base_field=models.Float64Field(), default=list)

    class Meta:
        abstract = True