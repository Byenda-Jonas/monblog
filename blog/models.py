from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    date_creation = models.DateTimeField(default=timezone.now)
    auteur = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.titre
class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    postenom = models.CharField(max_length=100)
    prénom = models.CharField(max_length=100)
    téléphone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    date_envoi = models.DateTimeField(default=timezone.now)  # ← AJOUT ICI

    def __str__(self):
        return f"{self.nom} - {self.email}"