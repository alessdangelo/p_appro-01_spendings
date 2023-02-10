from django.db import models

# Create your models here.
class User(models.Model):
    useName = models.CharField(max_length = 12)