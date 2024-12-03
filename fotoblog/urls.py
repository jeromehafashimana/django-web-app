from django.contrib import admin
from django.urls import path
from django-web-app.views import home  # Remplacez `your_app_name` par le nom de votre application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]

