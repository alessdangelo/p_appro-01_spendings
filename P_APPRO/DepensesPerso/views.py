from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    context = {"message": "Hello World !"}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))

# def index(request):
#     return render(request, 'index.html')