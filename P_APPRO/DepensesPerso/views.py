from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from DepensesPerso.models import User
from django.contrib import messages
from django.utils.html import escape

# Show pages

# Send the index and get all the users from database.
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', context={"users": users})

# Send the addSpending page and get all the users from database.


def addSpending(request):
    users = User.objects.all()
    return render(request, 'addSpending.html')

def spendings(request):
    return render(request, 'spendings.html')


# Page Functions

# Add a user with the form
def addUser(request):
    MAX_LENGTH_USERNAME = 12  # const for the max number of allowed characters
    username = request.POST.get("username")
    

    # Check for the username's length and if not empty
    if len(username) <= MAX_LENGTH_USERNAME and username:
        # Delete any space at start from the user's input
        username = username.strip()
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
