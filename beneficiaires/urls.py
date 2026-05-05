from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_beneficiaires, name='liste_beneficiaires'),
    path('ajouter/', views.ajouter_beneficiaire, name='ajouter_beneficiaire'),
]
