import logging
from django.conf import settings
from dream_house.celery import app
from django.core.mail import send_mail


@app.task
def send_email_for_activation(email, message):
    send_mail('DreamHouse confirm email', message, settings.EMAIL_HOST_USER,
              [email], fail_silently=False)
