from django_distill import distill_path
from . import views

def get_no_parameters():
    return None

urlpatterns = [
    distill_path('', views.liste_beneficiaires, name='liste_beneficiaires', distill_func=get_no_parameters),
    distill_path('dashboard/', views.dashboard, name='dashboard', distill_func=get_no_parameters),
    distill_path('agent-terrain/', views.agent_terrain, name='agent_terrain', distill_func=get_no_parameters),
    distill_path('agent_terrain/', views.agent_terrain, name='agent_terrain_underscore', distill_func=get_no_parameters),
    distill_path('verifier-identite/', views.verifier_identite, name='verifier_identite', distill_func=get_no_parameters),
    distill_path('check-identite/', views.check_identite, name='check_identite', distill_func=get_no_parameters),
    distill_path('ajouter/', views.ajouter_beneficiaire, name='ajouter_beneficiaire', distill_func=get_no_parameters),
    distill_path('service-worker.js', views.service_worker, name='service_worker', distill_func=get_no_parameters),
]
