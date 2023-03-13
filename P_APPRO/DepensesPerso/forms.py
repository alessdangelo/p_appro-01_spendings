from django import forms
from .models import *

# Add form for the spendings
class AddSpendingForm(forms.Form):
    
    model = Spending
    fields = '__all__'
    title = forms.CharField(max_length=20, label="Titre")
    amount = forms.DecimalField(label='Montant')
    date = forms.DateField(label="Date", widget=forms.widgets.DateInput(attrs={
                'type': 'date', 
                'class': 'dateForm'
                }))
    boughtBy = forms.ModelChoiceField(label="Acheteur", queryset=User.objects.all())
    usersInDebt = forms.ModelMultipleChoiceField(label="Concerne", queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple()) 


# Update model form for the spendings
class UpdateSpendingForm(forms.ModelForm):

    class Meta:
        users = [(u.pk, u.useName) for u in User.objects.all()]
        model = Spending
        fields = '__all__'
    
        title = forms.CharField(max_length=20)
        amount = forms.DecimalField()
        date = forms.DateField(input_formats='%d-%m-%Y')
        boughtBy = forms.ChoiceField()
        usersInDebt = forms.MultipleChoiceField() 

        # Name correctly the label with the wanted text label
        labels = {
            'speName' : 'Titre',
            'speAmount' : 'Montant', 
            'speDate' : 'Date', 
            'speBoughtBy' : 'Acheteur', 
            'speUsersInDebtNew' : 'Concerne',
        }

        # Alle the needed widget for the model form fields
        widgets = {
            'speBoughtBy' : forms.Select(choices=users),
            'speUsersInDebtNew' : forms.CheckboxSelectMultiple(),
            'speDate' : forms.DateInput(attrs={'type': 'date', 'class': 'dateForm' })
        }

    # Make sure the speBoughtBy is a model choice field
    # def __init__(self, *args, **kwargs):
    #      super().__init__(*args, **kwargs)
    #      self.fields['speBoughtBy'] = forms.ModelChoiceField(queryset=User.objects.all(), label='Acheteur')