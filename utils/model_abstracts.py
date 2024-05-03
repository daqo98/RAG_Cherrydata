import uuid
from django.db import models


class Model(models.Model):
    # We use the pk when making calls to the API
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True # to inherit from it on other Model classes