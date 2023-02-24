from django.db import models

# Create your models here.
class User(models.Model):
    useName = models.CharField(max_length = 12)
    
class Spending(models.Model):
    speName = models.CharField(max_length = 24)
    speAmount = models.DecimalField(max_digits = 5, decimal_places = 2)
    speDate = models.DateField()
    speBoughtBy = models.ManyToManyField(User)
    speUsersInDebt = models.CharField(max_length = 20)
    