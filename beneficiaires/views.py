from django.shortcuts import render, redirect
from .models import Beneficiaire

def liste_beneficiaires(request):
    beneficiaires = Beneficiaire.objects.all()
    return render(request, 'beneficiaires/liste.html', {'beneficiaires': beneficiaires})

def ajouter_beneficiaire(request):
    message = None
    if request.method == "POST":
        numero_identite = request.POST.get("numero_identite")

        if Beneficiaire.objects.filter(numero_identite=numero_identite).exists():
            message = "⚠️ Doublon détecté : bénéficiaire déjà enregistré."
        else:
            Beneficiaire.objects.create(
                nom=request.POST.get("nom"),
                prenom=request.POST.get("prenom"),
                genre=request.POST.get("genre"),
                date_naissance=request.POST.get("date_naissance"),
                zone=request.POST.get("zone"),
                tuteur=request.POST.get("tuteur"),
                numero_identite=numero_identite,
                type_aide=request.POST.get("type_aide"),
            )
            # ✅ Redirection vers la liste après succès
            return redirect('liste_beneficiaires')

    return render(request, 'beneficiaires/ajouter.html', {"message": message})
