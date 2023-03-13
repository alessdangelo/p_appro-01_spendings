from django.db import models

# Model for the users
class User(models.Model):
    useName = models.CharField(max_length=12)
    useAmountOwed = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.useName}"

# Model for the spendings
class Spending(models.Model):
    speName = models.CharField(max_length=24)
    speAmount = models.DecimalField(max_digits=5, decimal_places=2)
    speDate = models.DateField()
    speBoughtBy = models.PositiveIntegerField()
    # speBoughtBy = models.ManyToManyField(User, through='SpendingUserBought')
    speUsersInDebtNew = models.ManyToManyField(User, through='SpendingUserDebt')

    def __str__(self):
        return f"{self.speName} ({self.id})"

# Model for the link between the user in debt and the spendings
class SpendingUserDebt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spending = models.ForeignKey(Spending, on_delete=models.CASCADE)
    amount_owed = models.DecimalField(max_digits=5, decimal_places=2, default =0)

    def __str__(self):
        return f"{self.user} {self.spending} ({self.id})"
    
# Model for the link between the user that bought something and the spendings
# class SpendingUserBought(models.Model):
#     bouUser = models.ForeignKey(User, on_delete=models.CASCADE)
#     bouSpending = models.ForeignKey(Spending, on_delete=models.CASCADE)
#     amountPaid = models.DecimalField(max_digits=5, decimal_places=2, default =0)

#     def __str__(self):
#         return f"{self.bouUser} {self.bouSpending} ({self.id})"
