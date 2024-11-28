from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('accueil')  # Assurez-vous de définir une vue d'accueil
            else:
                return HttpResponse("Identifiants invalides")
    else:
        form = AuthenticationForm()

    return render(request, 'comptes/connexion.html', {'form': form})
