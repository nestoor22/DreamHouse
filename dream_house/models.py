from django.db import models
from django.contrib.auth.models import User


class DataToPredict(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField(default=None)
    area = models.FloatField(default=None)
    rooms = models.IntegerField(default=None)
    floor = models.IntegerField(default=None)
    building_type = models.CharField(max_length=40, default=None)
    distance_to_center = models.FloatField(default=None)
    living_area = models.FloatField(default=None)
    kitchen_area = models.FloatField(default=None)
    condition = models.CharField(max_length=40, default=None)
    walls_material = models.CharField(max_length=40, default=None)
    balconies = models.IntegerField(default=None)
    ceiling_height = models.FloatField(default=None)
    floors = models.IntegerField(default=None)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_type = models.CharField(max_length=30, blank=True, default='Not active')
    account_type = models.CharField(max_length=30, blank=True, default='Basic')
