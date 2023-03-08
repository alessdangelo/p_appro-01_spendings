from django import forms
# from django.forms import *
from .models import *

class AddSpendingForm(forms.Form):
    users = [(u.pk, u.useName) for u in User.objects.all()]
    model = Spending
    fields = '__all__'
    title = forms.CharField(max_length=20, label="Titre")
    amount = forms.DecimalField(label='Montant')
    date = forms.DateField(label="Date")
    boughtBy = forms.ChoiceField(label="Acheteur", choices=users)
    usersInDebt = forms.MultipleChoiceField(label="Concerne", choices=users)


class UpdateSpendingForm(forms.ModelForm):

    # usersInDebt = forms.MultipleChoiceField(label="Concerne", widget=forms.CheckboxSelectMultiple(), choices=[(u.pk, u.useName) for u in User.objects.all()])

    class Meta:
        users = [(u.pk, u.useName) for u in User.objects.all()]
        model = Spending
        fields = '__all__'
    
        title = forms.CharField(max_length=20)
        amount = forms.DecimalField()
        date = forms.DateField()
        boughtBy = forms.ChoiceField()
        usersInDebt = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=users) # (widget=forms.BooleanField)

        labels = {
            'speName' : 'Titre',
            'speAmount' : 'Montant', 
            'speDate' : 'Date', 
            'speBoughtBy' : 'Acheteur', 
            'speUsersInDebtNew' : 'Concerne',
        }

        widgets = {
            'speBoughtBy' : forms.Select(choices=users),
            # 'speUsersInDebtNew' : forms.SelectMultiple(choices=users),
        }