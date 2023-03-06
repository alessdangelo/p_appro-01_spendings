from django.db import models


class User(models.Model):
    useName = models.CharField(max_length=12)
    useAmountOwed = models.DecimalField(max_digits=5, decimal_places=2, default=0)


class Spending(models.Model):
    speName = models.CharField(max_length=24)
    speAmount = models.DecimalField(max_digits=5, decimal_places=2)
    speDate = models.DateField()
    speBoughtBy = models.DecimalField(max_digits=20, decimal_places=0)
    speUsersInDebtNew = models.ManyToManyField(
        User, through='SpendingUserDebt')


class SpendingUserDebt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spending = models.ForeignKey(Spending, on_delete=models.CASCADE)
    amount_owed = models.DecimalField(max_digits=5, decimal_places=2, default =0)
