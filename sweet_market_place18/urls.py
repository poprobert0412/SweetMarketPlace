"""
URL configuration for sweet_market_place18 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #MODIFICARE pentru include ca sa includem url urile in aplicatie
from sweet_market_place18 import settings
from django.conf.urls.static import static #Importam static ul din django sa nu ne dea eroare

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("sweet_market_place18_app.urls")),#Modificare sa includem url urile
    path('', include('django.contrib.auth.urls')),#Modificare sa includem url urile din django
    path('account/', include('account.urls')),
]

if settings.DEBUG: #Verificam daca proiectul nostru ruleaza in DEBUG
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Adaugam url urile pentru media