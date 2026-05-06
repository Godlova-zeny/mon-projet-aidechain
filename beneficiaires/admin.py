from django.contrib import admin
from .models import Beneficiaire

# Personnalisation de l’affichage dans l’admin
class BeneficiaireAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "genre", "date_naissance", "zone", "type_aide", "numero_identite")
    search_fields = ("nom", "prenom", "numero_identite", "zone")
    list_filter = ("genre", "type_aide", "zone")

# Enregistrement du modèle
admin.site.register(Beneficiaire, BeneficiaireAdmin)
