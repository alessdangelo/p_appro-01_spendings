from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #Django module letting us load HTML templates

# Create your views here.
def index(request):
    context = {"message": "Hello World !"} #Variable that can be added to the template before loading it
    template = loader.get_template("index.html") #Get template index.html
    return HttpResponse(template.render(context, request)) #request the loading of the template and return it

# def index(request):
#     return render(request, 'index.html')