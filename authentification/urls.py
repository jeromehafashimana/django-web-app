from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Associe '/' à la vue 'home_view'
]
