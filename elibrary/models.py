from django.db import models


class Etudiant(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    pwd = models.CharField(max_length=15)

class Livre(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=20)
    auteur = models.CharField(max_length=15)
    categorie = models.CharField(max_length=15)
    nombre_pages = models.IntegerField()

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    id_etudiant=models.IntegerField()
    id_livre = models.IntegerField()





