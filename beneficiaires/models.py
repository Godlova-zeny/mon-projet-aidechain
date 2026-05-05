from django.db import models

class Beneficiaire(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numero_identite = models.CharField(max_length=50, unique=True)
    zone = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
