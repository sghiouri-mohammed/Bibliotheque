from django.shortcuts import render, redirect
from collections import Counter

from elibrary.models import Etudiant, Livre, Reservation
from datetime import datetime, date

def afficher_index(request):

    nom = "abdou"
    prenom = "mohammed"

    return render(request, 'index.html', context={
        "variable1":nom,
        "variable2":prenom
    })



def best_book(ids): # la liste des id_livres dans la table reservation

    # Utiliser un dictionnaire pour compter les occurrences
    id_count = {}
    for id in ids:
        if id in id_count:
            id_count[id] += 1
        else:
            id_count[id] = 1

    # Trouver l'id avec le maximum d'occurrences
    max_id = max(id_count, key=id_count.get) # 3

    return max_id


def dashboard(request):

    # Get today's date
    today = date.today()
    nombre_de_utilisateurs = Etudiant.objects.all().count()
    nombre_livre= Livre.objects.all().count()
    # calculer le nombre de lignes de la table reservations
    nombre_reservations = Reservation.objects.all().count()
    today_reservations_count = Reservation.objects.filter(date_reservation__date=today).count()
    today_etudiants_count = Etudiant.objects.filter(date_inscription__date=today).count()

    # Récupérer la liste des id de livres dans les réservations
    liste_id_livres = Reservation.objects.values_list('id_livre', flat=True)

    # Trouver l'id du livre le plus réservé
    id_best_livre = best_book(liste_id_livres)

    # Récupérer le livre correspondant à cet id
    meilleur_livre = Livre.objects.get(id=id_best_livre)

    # Obtenir le titre du meilleur livre
    nom_livre = meilleur_livre.titre


    return render(request, 'dashboard.html', context={
        # pour passer les variables vers les pages HTML
        "first_name":request.session['fname'],
        "last_name": request.session['lname'],
        "nbr_users": nombre_de_utilisateurs,
        "nbr_livre": nombre_livre,
        "nbr_reser": nombre_reservations,
        "rsvr_auj" : today_reservations_count,
        "inscr_auj": today_etudiants_count,
        "livre":nom_livre,

    })



def registration(request):
    message = ""

    if request.method == "POST":

        firstname = request.POST["firstname"] #fname f:first
        last_name = request.POST["lname"] #lname l:last
        email = request.POST["email"]
        pwd = request.POST["password"]

        etudiant = Etudiant(first_name=firstname, last_name=last_name, email=email, pwd=pwd)

        if etudiant :
            message = "Utilisateur ajouté avec success"
            etudiant.save() #c'est pour enregistrer l'etudiant sur la base de donnees
        else:
            message = "Veuillez ressayer"

    return render(request, 'Register.html', context={"abdou":message} )


def login(request):
    message = ""
    d = 0
    if request.method == "POST":

        mail = request.POST["email"]
        password = request.POST["password"]

        utilisateurs = Etudiant.objects.raw("SELECT * FROM elibrary_Etudiant")

        for utilisateur in  utilisateurs:

            if (utilisateur.email == mail and utilisateur.pwd == password):

                request.session['fname'] = utilisateur.first_name
                request.session['lname'] = utilisateur.last_name
                request.session['mail'] = utilisateur.email

                d = 1

        if d == 1:
            return redirect('dashboard')
        else:
            message = "Ce compte n'existe pas !!!"


    return render(request, 'login.html', context={"message":message})


def logout(request):

    request.session['fname'] = None
    request.session['lname'] = None
    request.session['mail'] = None

    return redirect('login')

def page_creation_livre(request):

    if request.method == "POST": # ici on verifi si l'utilisateur a cliquer sur le boutton submit

        titre = request.POST["titre"]
        auteur = request.POST["auteur"]
        categorie = request.POST["categorie"]
        nbr_pages = request.POST["nbr_pages"]

        livre = Livre(titre=titre, auteur=auteur, categorie=categorie, nombre_pages=nbr_pages)
        livre.save()

    return render(request, 'creer_livre.html', context={"first_name":request.session["fname"],"last_name":request.session["lname"] })

def afficher_livres(request):

    liste_des_livres = Livre.objects.all() #on a recuperer une liste des livrres qui existent sur la table Livre
    return render(request, 'liste_livres.html', context={"livres":liste_des_livres})



def supprimer_livre(request,id_livre):

    liste_des_livres = Livre.objects.all()

    livre_a_supprimer = Livre.objects.get(id=id_livre)#select * from Livre where id=id_livre
    livre_a_supprimer.delete()

    return render(request, 'liste_livres.html', context={"livres":liste_des_livres})


def supprimer_resrvation(request,id_reservation):

    liste_des_livres = Reservation.objects.all()

    livre_a_supprimer = Reservation.objects.get(id=id_reservation)#select * from Livre where id=id_livre

    livre_a_supprimer.delete()

    redirect('liste_reservation.html')

    return render(request, 'liste_reservation.html', context={"reservations":liste_des_livres})


def supprimer_etudiant(request, id_etudiant):

    liste_utilisateurs = Etudiant.objects.all()

    etudiant_a_supprimer = Etudiant.objects.get(id=id_etudiant)  # select * from Etudiant where id=id_etudiant
    etudiant_a_supprimer.delete()

    return render(request, 'liste_utilisateurs.html', context={'etudiants': liste_utilisateurs})


def modifier_livre(request,id_livre):

    livre = Livre.objects.get(id=id_livre)

    if request.method == "POST":

        nouveau_titre = request.POST["titre"]
        nouveau_auteur = request.POST["auteur"]
        nouvelle_categ = request.POST["categorie"]
        nouveau_nbr_page = request.POST["nbr_pages"]

        livre.titre = nouveau_titre
        livre.auteur = nouveau_auteur
        livre.categorie = nouvelle_categ
        livre.nombre_pages = nouveau_nbr_page

        livre.save()# enregistrer les modifications

    return render(request, 'modifier_livre.html', context={"livre":livre})


def liste_utilisateurs(request):
    # pour recuperer tous les lignes de la table
    liste_utilisateurs= Etudiant.objects.all()
    return render(request, 'liste_utilisateurs.html', context={'etudiants':liste_utilisateurs})


def modifier_etudiant(request, id_etudiant):

    etudiants = Etudiant.objects.all()

    etudiant = Etudiant.objects.get(id=id_etudiant)

    if request.method == "POST":

        nouveau_nom = request.POST["fname"]
        nouveau_prenom = request.POST["lname"]
        nouvelle_email = request.POST["email"]

        etudiant.first_name = nouveau_nom
        etudiant.last_name = nouveau_prenom
        etudiant.email = nouvelle_email

        etudiant.save()  # enregistrer les modifications

    return render(request, 'modifier_etudiant.html', context={"etudiants": etudiants})

def about(request):

    return render(request, 'about.html' ,
                  context={
                        "first_name":request.session['fname'],
                        "last_name": request.session['lname'],
                        "email":request.session['mail'],
                  })



def ajouter_reservation(request):

    liste_des_etudiant = Etudiant.objects.all()
    liste_des_livres = Livre.objects.all()

    #ici on verifie que l'utilisateur a cliqué sur le boutton submit
    if (request.method == "POST"):

        #On récupère les valeurs des champs des input (select) choisit par l'utilisateur
        etudiant= request.POST["etudiant"]
        livre=request.POST["livre"]

        #On insère la reservation
        #id_etudiant : c'est le nom de la colonne de la table Reservation
        #id_livre : c'est le nom de la colonne de la table Reservation
        reservation = Reservation(id_etudiant=etudiant, id_livre=livre)

        #enregisterer la reservation
        reservation.save()

    return render(request, 'reserver_livre.html' ,
                  context={
                        "etudiants":liste_des_etudiant,
                        "livres":liste_des_livres,
                        "first_name":request.session['fname'],
                        "last_name": request.session['lname'],
                        "email":request.session['mail'],
                  })


def afficher_liste_reservations(request):

    liste_des_reservations = Reservation.objects.all()

    return render(request, 'liste_reservation.html',
                  context={
                      "reservations": liste_des_reservations,
                      "first_name": request.session['fname'],
                      "last_name": request.session['lname'],
                      "email": request.session['mail'],
                  })


def info_etudiant(request, id_etudiant):

    etudiant = Etudiant.objects.get(id=id_etudiant)

    return render(request, 'info_tudin.html',
                  context={
                      "etudiant": etudiant,
                      "first_name": request.session['fname'],
                      "last_name": request.session['lname'],
                  })


def info_livre(request, id_livre):

    livre = Livre.objects.get(id=id_livre)

    return render(request, 'info_livre.html',
                  context={
                      "livre": livre,
                      "first_name": request.session['fname'],
                      "last_name": request.session['lname'],
                  })


