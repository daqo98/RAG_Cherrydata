from .celery import app as celery_app

# To make sure that your Celery app is loaded when you start Django
__all__ = ("celery_app",)