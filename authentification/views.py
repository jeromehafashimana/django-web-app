from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Bienvenue sur la page d'accueil !")
