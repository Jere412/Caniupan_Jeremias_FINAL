"""
URL configuration for Caniupan_Jeremias_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from proyecto_app import views

urlpatterns = [
    path('', views.index),
    path('autor/', views.autor),
    path('agregarInstituciones/', views.A_institucion),
    path('listarInstituciones/', views.L_institucion),
    path('agregarSeminarios/', views.A_seminario),
    path('listarSeminarios/', views.L_seminario),
    path('instituciones/', views.instituciones_list, name='instituciones_list'),
    path('instituciones/<int:pk>/', views.instituciones_detail, name='instituciones_detail'),
    path('seminarios/', views.SeminariosList.as_view(), name='SeminariosList'),
    path('seminarios/<int:pk>/', views.SeminariosDetail.as_view(), name='SeminariosDetail'),
]

