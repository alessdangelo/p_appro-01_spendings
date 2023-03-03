from django.contrib import admin
from DepensesPerso.models import *

# Register your models here.
admin.site.register(User),
admin.site.register(Spending),
admin.site.register(SpendingUserDebt)