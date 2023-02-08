from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from DepensesPerso.models import User

# Send the index and get the users from database.
def index(request):
    users = User.objects.all()
    username = request.POST.get("username")
    return render(request, 'index.html', context={"users": users})

# Add a user with the form
def addUser(request):
    username = request.POST.get("username")
    User.objects.create(useName=username)
    return redirect('index')