from django.db import models
from django.contrib import admin
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=64)
    pwd=models.CharField(max_length=64)

