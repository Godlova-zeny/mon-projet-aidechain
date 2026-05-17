from django_distill import distill_path
from . import views

def get_no_parameters():
    return None

urlpatterns = [
    distill_path('', views.accueil, name='accueil', distill_func=get_no_parameters),
    distill_path('a_propos/', views.a_propos, name='a_propos', distill_func=get_no_parameters),
    distill_path('contact/', views.contact, name='contact', distill_func=get_no_parameters),
    distill_path('projet/', views.projet, name='projet', distill_func=get_no_parameters),
    distill_path('impact/', views.impact, name='impact', distill_func=get_no_parameters),
    distill_path('equipe/', views.equipe, name='equipe', distill_func=get_no_parameters),
]
