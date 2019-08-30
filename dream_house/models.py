from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class DataToPredict(models.Model):
#     pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_type = models.CharField(max_length=30, blank=True, default='Not active')
