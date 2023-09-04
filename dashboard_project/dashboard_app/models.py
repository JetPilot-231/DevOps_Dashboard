# dashboard_app/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

class Metric(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()

