from django import forms
from .models import *

class AddSpendingForm(forms.Form):
    users = [(u.pk, u.useName) for u in User.objects.all()]
    model = Spending
    fields = '__all__'
    title = forms.CharField(max_length=20, label="Titre")
    amount = forms.DecimalField(label='Montant')
    date = forms.DateField(label="Date", widget=forms.widgets.DateInput(attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }))
    boughtBy = forms.ChoiceField(label="Acheteur", choices=users)
    usersInDebt = forms.MultipleChoiceField(label="Concerne", choices=users, widget=forms.CheckboxSelectMultiple()) 

class UpdateSpendingForm(forms.ModelForm):

    class Meta:
        users = [(u.pk, u.useName) for u in User.objects.all()]
        model = Spending
        fields = '__all__'
    
        title = forms.CharField(max_length=20)
        amount = forms.DecimalField()
        date = forms.DateField()
        boughtBy = forms.ChoiceField()
        usersInDebt = forms.MultipleChoiceField() 

        labels = {
            'speName' : 'Titre',
            'speAmount' : 'Montant', 
            'speDate' : 'Date', 
            'speBoughtBy' : 'Acheteur', 
            'speUsersInDebtNew' : 'Concerne',
        }

        widgets = {
            'speBoughtBy' : forms.Select(choices=users),
            'speUsersInDebtNew' : forms.CheckboxSelectMultiple(),
        }
