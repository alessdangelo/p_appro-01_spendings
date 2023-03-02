from django.db import models


class User(models.Model):
    useName = models.CharField(max_length=12)
    # class Meta:
    #     db_table = 't_user'

# To do : fonction tostring pour afficher


class Spending(models.Model):
    speName = models.CharField(max_length=24)
    speAmount = models.DecimalField(max_digits=5, decimal_places=2)
    speDate = models.DateField()
    speBoughtBy = models.CharField(max_length=20)
    speUsersInDebt = models.ManyToManyField(User)