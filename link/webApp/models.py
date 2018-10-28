from django.db import models

# Create your models here.

class LinkModel(models.Model):
    link = models.CharField(max_length=500)
    key = models.CharField(unique=True,max_length=50)

class NameModel(models.Model):
    name = models.CharField(max_length=50)
