from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from django.http import JsonResponse
from .models import Beneficiaire

# Vue du tableau de bord
def dashboard(request):
    beneficiaires = Beneficiaire.objects.all()
    stats_type = Beneficiaire.objects.values('type_aide').annotate(count=Count('id')).order_by('-count')
    stats_genre = Beneficiaire.objects.values('genre').annotate(count=Count('id')).order_by('-count')
    recent = beneficiaires.order_by('-id')[:5]
    return render(request, 'beneficiaires/dashboard.html', {
        'total': beneficiaires.count(),
        'stats_type': stats_type,
        'stats_genre': stats_genre,
        'recent': recent,
    })

# Vue pour l’agent terrain mobile
def agent_terrain(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        zone = request.POST.get('zone')
        numero_identite = request.POST.get('numero_identite')
        type_aide = request.POST.get('type_aide')

        if Beneficiaire.objects.filter(numero_identite=numero_identite).exists():
            messages.error(request, 'Numéro d’identité déjà enregistré. Doublon détecté.')
            return render(request, 'beneficiaires/agent_terrain.html')

        Beneficiaire.objects.create(
            nom=nom,
            prenom=prenom,
            zone=zone,
            numero_identite=numero_identite,
            type_aide=type_aide,
        )
        messages.success(request, 'Bénéficiaire enregistré avec succès.')
        return redirect('agent_terrain')

    return render(request, 'beneficiaires/agent_terrain.html')

# Endpoint AJAX de vérification de doublon
def check_identite(request):
    numero = request.GET.get('numero')
    if not numero:
        return JsonResponse({'error': 'Numéro d’identité manquant'}, status=400)

    existe = Beneficiaire.objects.filter(numero_identite=numero).exists()
    return JsonResponse({'doublon': existe})

# Page de vérification d'identité pour la démo live
def verifier_identite(request):
    return render(request, 'beneficiaires/verifier_identite.html')

# Vue pour lister les bénéficiaires
def liste_beneficiaires(request):
    beneficiaires = Beneficiaire.objects.all()
    return render(request, 'beneficiaires/liste.html', {'beneficiaires': beneficiaires})

# Vue pour ajouter un bénéficiaire
def ajouter_beneficiaire(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        genre = request.POST.get("genre")
        date_naissance = request.POST.get("date_naissance")
        zone = request.POST.get("zone")
        tuteur = request.POST.get("tuteur")
        numero_identite = request.POST.get("numero_identite")
        type_aide = request.POST.get("type_aide")

        # Vérifier si le numéro d'identité existe déjà
        if Beneficiaire.objects.filter(numero_identite=numero_identite).exists():
            messages.error(request, "Ce numéro d'identité existe déjà.")
            return render(request, "beneficiaires/ajouter.html")

        # Créer et sauvegarder le bénéficiaire
        Beneficiaire.objects.create(
            nom=nom,
            prenom=prenom,
            genre=genre,
            date_naissance=date_naissance,
            zone=zone,
            tuteur=tuteur,
            numero_identite=numero_identite,
            type_aide=type_aide,
        )
        messages.success(request, "Bénéficiaire ajouté avec succès.")
        return redirect("liste_beneficiaires")

    return render(request, "beneficiaires/ajouter.html")
