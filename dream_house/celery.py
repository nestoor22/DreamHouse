from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DreamHouse.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery(app='dream_house')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()