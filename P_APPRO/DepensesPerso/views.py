from datetime import date
from io import BytesIO
from itertools import chain

from DepensesPerso.models import *
from django import forms
from django.contrib import messages
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.template.loader import get_template
from django.utils.html import escape
from django.views import View
from xhtml2pdf import pisa

from .forms import AddSpendingForm
from .forms import UpdateSpendingForm

"""Show pages"""

# Send the index and get all the users from database.
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', context={"users": users})

# Send the addSpending page and get all the users from database.
def addSpending(request):
    # Create a new form using forms.py
    form = AddSpendingForm()
    # True if we're using POST and that the form is valid
    if request.method == 'POST':
        form = AddSpendingForm(request.POST)
        if form.is_valid():
            # Clean the data of the form
            data = form.cleaned_data
            users_in_debt = User.objects.filter(pk__in=data['usersInDebt'])
            # The data that will be sent to the model, formatted in a table
            new_spending = Spending.objects.create(
            speName=data['title'],
            speAmount=data['amount'],
            speDate=data['date'],
            speBoughtBy=data['boughtBy']
            )
            # Add and save the formatted data to the model
            new_spending.speUsersInDebtNew.set(users_in_debt)
            # Calculate and update the amount owed for each user
            for user in users_in_debt:
                amount_owed = SpendingUserDebt.objects.create(
                    user=user,
                    spending=new_spending,
                    amount_owed=data['amount'] / len(users_in_debt)
                )
                user.useAmountOwed += amount_owed.amount_owed
            # Save the changes to the database
            new_spending.save()
    return render(request, 'addSpending.html', context = {'form': form})

# Update a spending
def updateSpending(request, spendingId):
    # Get the spending id
    spending = Spending.objects.get(pk=spendingId)
    # Generate the Form
    form = UpdateSpendingForm(instance=spending)

    # True if we're using POST and that the form is valid
    if request.method == 'POST':
        form = UpdateSpendingForm(request.POST, instance=spending)
        if form.is_valid():
            # Update the existing `Spending` in the database
            form.save()
            # Redirect to the listing page to see the result of the update
            return redirect('listSpendings')
        else:
            form = UpdateSpendingForm(instance=spending)

    return render(request, 'updateSpending.html', context = { 'form': form })

# Page where we list every spendings
def listSpendings(request):
    spendings = Spending.objects.all()
    # Dictionary to be sent to the template, with id and name of users
    boughtBy = User.objects.all().values('id', 'useName')

    return render(request, 'listSpendings.html', context={"spendings": spendings, "boughtBy": boughtBy})

"""Page Functions"""

# Add a user with the form
def addUser(request):
    MAX_LENGTH_USERNAME = 12  # const for the max number of allowed characters
    username = request.POST.get("username")

    # Check for the username's length and if not empty
    if len(username) <= MAX_LENGTH_USERNAME and username:
        # Delete any space at start from the user's input
        username = username.strip()
        username = username.lower()
        if username:
            user, created = User.objects.get_or_create(useName=username)
            # Verify if an object was created.
            if not created:
                messages.error(request, "Les doublons ne sont pas autorisés")
        else:
            messages.error(request, "Veuillez ne pas commencer par un espace")
    else:
        messages.error(request, "Veuillez respecter le nombre de caractères autorisés (minimum 1 et maximum 13)")

    return redirect('index')


# Delete a user with the link
def deleteUser(request, userId):
    username = get_object_or_404(User, pk=userId)
    username.delete()

    return redirect('index')

# Delete a spending with the link
def deleteSpending(request, spendingId):
    spend = get_object_or_404(Spending, pk=spendingId)
    spend.delete()

    return redirect('listSpendings')


# Take a template and the infos in the dictionnary to create PDF
def renderToPdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type = 'depensesPerso/download')
    return None

# Class to download as a PDF
class downloadListSpendings(View):

    # Get all the spendings and store it in a dictionnary to create the PDF with the choosen template
    def get(self, request, *args, **kwargs):
        spendings = Spending.objects.all()
        boughtBy = User.objects.all().values('id', 'useName')
        context = {'spendings': spendings, "boughtBy": boughtBy }

        pdf = renderToPdf('pdfListSpendings.html', context)
        response = HttpResponse(pdf, content_type = 'depensesPerso/download')
        filename = "Liste_des_dépenses.pdf"
        content = "attachment; filename=%s" %(filename)
        response['Content-Disposition'] = content

        return response