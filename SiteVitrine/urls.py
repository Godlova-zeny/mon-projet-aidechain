from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('a_propos/', views.a_propos, name='a_propos'),
    path('contact/', views.contact, name='contact'),
    path('projet/', views.projet, name='projet'),
    path('impact/', views.impact, name='impact'),
    path('equipe/', views.equipe, name='equipe'),
]
