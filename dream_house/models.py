from django.db import models
from django.contrib.auth.models import User


class DataToPredict(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    price = models.FloatField(default=None, null=True, blank=True)
    area = models.FloatField(default=None, null=True,  blank=True)
    rooms = models.IntegerField(default=None, null=True, blank=True)
    floor = models.IntegerField(default=None, null=True)
    building_type = models.CharField(max_length=40, null=True, default=None)
    distance_to_center = models.FloatField(default=None,null=True, blank=True)
    living_area = models.FloatField(default=None, null=True)
    kitchen_area = models.FloatField(default=None, null=True)
    condition = models.CharField(max_length=40,null=True, default=None)
    walls_material = models.CharField(max_length=40,null=True, default=None)
    balconies = models.IntegerField(default=None, null=True)
    ceiling_height = models.FloatField(default=None, null=True)
    floors = models.IntegerField(default=None, null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_type = models.CharField(max_length=30, blank=True, default='Not active')
    account_type = models.CharField(max_length=30, blank=True, default='Basic')
