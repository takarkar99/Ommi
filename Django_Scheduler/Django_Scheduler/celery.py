from __future__ import absolute_import, unicode_literals
import os
import pytz
from celery import Celery
from django.conf import settings
from datetime import datetime
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Scheduler.settings')

app = Celery('Django_Scheduler') 

app.conf.enable_utc = False

local_timezone = datetime.now(pytz.timezone('UTC')).astimezone().tzinfo

app.conf.update(timezone=local_timezone)

# Configure Celery using settings from Django settings.py.
app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {

    'send-greeting-message-at-6' : {
        'task' : 'App1.tasks.Good_morning',
        'schedule': crontab(minute='*'),
        # 'schedule': crontab(hour=6, minute=0)
    }

}
app.autodiscover_tasks()
# Load tasks from all registered Django app configs.


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')