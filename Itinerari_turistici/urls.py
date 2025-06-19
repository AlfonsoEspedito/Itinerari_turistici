"""
URL configuration for Itinerari_turistici project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from Itinerari import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.benvenuto, name='benvenuto'),
    path('registrazione/', views.registrazione, name='registrazione'),
    path('login_turista/', views.login_turista, name='login_turista'),
    path('login_guida/', views.login_guida, name='login_guida'),
    path('login_amministratore/', views.login_amministratore, name='login_amministratore'),
    path('principale/', views.principale, name='principale'),
]
