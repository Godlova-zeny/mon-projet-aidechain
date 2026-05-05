from django.shortcuts import render

def accueil(request):
    return render(request, 'site_vitrine/accueil.html')

def a_propos(request):
    return render(request, 'site_vitrine/a_propos.html')

def contact(request):
    return render(request, 'site_vitrine/contact.html')

def projet(request):
    return render(request, 'site_vitrine/projet.html')

def impact(request):
    return render(request, 'site_vitrine/impact.html')

def equipe(request):
    return render(request, 'site_vitrine/equipe.html')
