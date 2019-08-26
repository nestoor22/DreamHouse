from django.contrib.auth.models import User


def check_user_not_exist(person_email):
    try:
        User.objects.get(email=person_email)
        return 0
    except User.DoesNotExist:
        return 1
