from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DreamHouse.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery(app='dream_house')

app.config_from_object('django.conf:settings', )

app.autodiscover_tasks()
app.conf.update(result_expires=3600, enable_utc=True, timezone='Europe/Minsk')

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'dream_house.tasks.send_daily_email',
        'schedule': crontab(day_of_week='sunday', hour='17', minute=0, month_of_year='*')
    }
}
