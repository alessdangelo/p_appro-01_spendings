from django import forms
from .models import *
from django.forms import ModelForm


class AddSpendingForm(forms.ModelForm):
    class Meta: 
        model = Spending
        fields = '__all__'
        title = forms.CharField(max_length=20, label="Titre")
        amount = forms.DecimalField(label='Montant')
        date = forms.DateField(label="Date")
        boughtBy = forms.ChoiceField(label="Acheteur")
        userInDebt = forms.CheckboxSelectMultiple()
