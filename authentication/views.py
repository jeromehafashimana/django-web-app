from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ConnexionForm

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('page_accueil')  # Redirection après connexion
            else:
                form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect")
    else:
        form = ConnexionForm()
    
    return render(request, 'authentification/connexion.html', {'form': form})
