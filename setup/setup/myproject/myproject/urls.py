from django.contrib import admin
from django.urls import path, include  # Inclui 'include' para poder incluir URLs de outros apps

# Definindo as URLs principais
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('setup.urls')),  # Incluindo as URLs do app 'setup'
]
