from django.conf import settings
from dream_house.celery import app
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.template import Template, Context


daily_template = Template("""Hello {{user.first_name}} !
 Here is new proposals which may be interesting for you: """)


@app.task
def send_email_for_activation(email, message):
    send_mail('DreamHouse confirm email', message, settings.EMAIL_HOST_USER,
              [email], fail_silently=False)


@app.task
def send_daily_email():
    for user in User.objects.all():
        try:
            if user.profile.account_type == 'Basic':
                send_mail("New proposals", daily_template.render(context=Context({'user': user})),
                          settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
        except AttributeError or TypeError or TimeoutError or ConnectionError:
            continue

