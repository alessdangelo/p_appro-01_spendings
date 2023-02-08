from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from DepensesPerso.models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', context={"user": users})

# def index(request):
#     return render(request, 'index.html')