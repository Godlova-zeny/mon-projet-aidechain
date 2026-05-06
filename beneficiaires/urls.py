from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_beneficiaires, name='liste_beneficiaires'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('agent-terrain/', views.agent_terrain, name='agent_terrain'),
    path('agent_terrain/', views.agent_terrain, name='agent_terrain_underscore'),
    path('verifier-identite/', views.verifier_identite, name='verifier_identite'),
    path('check-identite/', views.check_identite, name='check_identite'),
    path('ajouter/', views.ajouter_beneficiaire, name='ajouter_beneficiaire'),
]
