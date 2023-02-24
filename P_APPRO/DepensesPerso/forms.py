from django import forms
from .models import Spendings
from django.forms import ModelForm


class AddSpendingForm(forms.Form):
    class Meta: 
        model =Spendings
        fields = '__all__'
        title = forms.CharField()
        amount = forms.DecimalField()
        date = forms.DateField()
        boughtBy = forms.ChoiceField()
        userInDebt = forms.CheckboxSelectMultiple()
