from django.db import models


class User(models.Model):
    useName = models.CharField(max_length=12)
    useAmountOwed = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.useName}"


class Spending(models.Model):
    speName = models.CharField(max_length=24)
    speAmount = models.DecimalField(max_digits=5, decimal_places=2)
    speDate = models.DateField()
    speBoughtBy = models.PositiveIntegerField()
    speUsersInDebtNew = models.ManyToManyField(User, through='SpendingUserDebt')

    def __str__(self):
        return f"{self.speName} ({self.id})"


class SpendingUserDebt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spending = models.ForeignKey(Spending, on_delete=models.CASCADE)
    amount_owed = models.DecimalField(max_digits=5, decimal_places=2, default =0)

    def __str__(self):
        return f"{self.user} {self.spending} ({self.id})"
