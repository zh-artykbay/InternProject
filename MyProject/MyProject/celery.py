import os

from celery import Celery
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')

app = Celery('MyProject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'second-task': {
        'task': 'app.tasks.scrape_One',
        'schedule': crontab(minute='*/60'),
    },
}

"""
'add-every-monday-morning': {
        'task': 'app.tasks.add',
        'schedule': crontab(minute='*/1'),
        'args': (16, 16),
    },
from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery import task
from celery.schedules import crontab

from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')

app = Celery('MyProject')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
#app.config_from_object('django.conf:settings')
#app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



@task
def pp():
 print("OKKK")
"""
"""
app.conf.beat_schedule = {
 "amount_counting": {
 "task": "MyProject.app.task.amount_counting",
 "schedule": crontab(minute='*/60'),
 }
}
"""
#celery -A MyProject worker -l info