import uuid, hashlib
from django.db import models

class Beneficiaire(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    genre = models.CharField(
        max_length=10,
        choices=[('Masculin', 'Masculin'), ('Féminin', 'Féminin')],
        null=True, blank=True
    )

    date_naissance = models.DateField(null=True, blank=True)

    zone = models.CharField(max_length=100, null=True, blank=True)
    tuteur = models.CharField(max_length=100, null=True, blank=True)

    numero_identite = models.CharField(max_length=50, unique=True)

    type_aide = models.CharField(
        max_length=20,
        choices=[
            ('Alimentaire', 'Alimentaire'),
            ('Cash', 'Cash'),
            ('Médical', 'Médical'),
            ('WASH', 'WASH'),
            ('Éducation', 'Éducation'),
        ],
        null=True, blank=True
    )

    uuid_blockchain = models.CharField(max_length=64, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.uuid_blockchain:
            data = f"{self.nom}{self.prenom}{self.date_naissance}{self.numero_identite}{uuid.uuid4()}"
            self.uuid_blockchain = hashlib.sha256(data.encode()).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.type_aide}"
