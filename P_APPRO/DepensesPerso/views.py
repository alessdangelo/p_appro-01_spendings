from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from DepensesPerso.models import User
from django.contrib import messages
import string

# Send the index and get all the users from database.
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', context = {"users": users})

# Add a user with the form
def addUser(request):
    MAX_LENGTH_USERNAME = 12 # const for the max allows characters
    username = request.POST.get("username")

    # Check for the username's length and not empty
    if len(username) <= MAX_LENGTH_USERNAME and username:
        # Delete the space charactere at start of the user's input
        username = username.strip() 
        # Add the username's input in the database fiels 'useName'
        User.objects.create(useName = username) 
    else:
        messages.error(request, "Veuillez respecter le nombre de caractères autorisés (minimum 1 et maximum 13)")

    return redirect('index')


# Delete a user with the link
def deleteUser(request, userId):
    username = get_object_or_404(User, pk = userId)
    username.delete()

    return redirect('index')