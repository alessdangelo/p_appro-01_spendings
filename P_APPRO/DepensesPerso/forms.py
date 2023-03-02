from django import forms
from .models import *

class AddSpendingForm(forms.Form):
    users = User.objects.values_list()
    model = Spending
    fields = '__all__'
    title = forms.CharField(max_length=20, label="Titre")
    amount = forms.DecimalField(label='Montant')
    date = forms.DateField(label="Date")
    boughtBy = forms.ChoiceField(label="Acheteur", choices=users)
    userInDebt = forms.MultipleChoiceField(label="Concerne", choices=users) 