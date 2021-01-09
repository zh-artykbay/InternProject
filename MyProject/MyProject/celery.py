from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')

app = Celery('MyProject')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)


"""@app.task
def add(x, y):
    return x + y"""

app.conf.beat_schedule = {
 "run-me-every-one-hour": {
 "task": "MyProject.app.task.scrape_One",
 "schedule": crontab(minute='*/60'),
 }
}
#celery -A MyProject worker -l info