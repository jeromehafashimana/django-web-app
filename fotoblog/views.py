# fotoblog/views.py

from django.shortcuts import render

def connexion(request):
    return render(request, 'fotoblog/connexion.html')  # Modifiez le chemin selon vos besoins
