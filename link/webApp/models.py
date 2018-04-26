from django.db import models

# Create your models here.

class LinkModel(models.Model):
    link = models.CharField(max_length=500,unique=True)
