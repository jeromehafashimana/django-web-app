from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),  # Inclure les URLs de l'application utilisateurs
]

