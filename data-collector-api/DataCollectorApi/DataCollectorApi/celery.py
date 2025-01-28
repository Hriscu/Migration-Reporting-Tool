from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataCollectorApi.settings')

app = Celery('DataCollectorApi', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

app.conf.update(
    CELERY_TASK_ALWAYS_EAGER=True,
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0',
    CELERY_TIMEZONE='UTC',
    CELERY_ENABLE_UTC=True,
    CELERY_POOL='solo'
)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
