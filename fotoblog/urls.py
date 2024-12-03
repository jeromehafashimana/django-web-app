from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentification.urls')),  # Inclure les routes de 'myapp'
]
