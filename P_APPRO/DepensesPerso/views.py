from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from DepensesPerso.models import User

# Send the index and get all the users from database.
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', context = {"users": users})

# Add a user with the form
def addUser(request):
    username = request.POST.get("username")
    if len(username) <= 13:
        User.objects.create(useName = username)
    # else:
    #     render(request, 'index.html', context = {"error": "Veuillez respecter le nombre maximal de caractères autorisés (13)"})

    return redirect('index')


# Delete a user with the link
def deleteUser(request, userId):
    username = get_object_or_404(User, pk = userId)
    username.delete()

    return redirect('index')