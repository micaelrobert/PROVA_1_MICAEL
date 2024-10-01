from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Prova Micael Robert Laboratorio Back end</h1>")


# Create your views here.
