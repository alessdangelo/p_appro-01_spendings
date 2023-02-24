from django import forms
from .models import *
from django.forms import ModelForm


class AddSpendingForm(forms.ModelForm):
    class Meta: 
        model = Spending
        fields = '__all__'
        title = Spending.speName
        amount = forms.DecimalField()
        date = forms.DateField()
        boughtBy = forms.ChoiceField()
        userInDebt = forms.CheckboxSelectMultiple()
