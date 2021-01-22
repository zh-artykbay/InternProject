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
    # Executes every 1 hour
    'first-task': {
        'task': 'app.tasks.scrape_Technodom',
        'schedule': crontab(minute='*/59'),
    },
    'second-task': {
        'task': 'app.tasks.scrape_Sulpak',
        'schedule': crontab(minute='*/59'),
    },
    'third-task': {
        'task': 'app.tasks.scrape_Shopkz',
        'schedule': crontab(minute='*/59'),
    },
    'forth-task': {
        'task': 'app.tasks.Matching_items',
        'schedule': crontab(hour='*/2'),
    },
}
#celery -A MyProject worker -l info