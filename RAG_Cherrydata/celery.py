import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RAG_Cherrydata.settings")
app = Celery("RAG_Cherrydata")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()