from django.shortcuts import render, redirect

from elibrary.models import Etudiant, Livre


def page_creation_livre(request):

    if request.method == "POST":
        a = request.POST["titre"]  # fname f:first
        b = request.POST["auteur"]  # fname f:first
        c = request.POST["categorie"]  # fname f:first
        d = request.POST["nbr_pages"]  # fname f:first
        livre= Livre(titre=a, auteur=b, categorie=c, nombre_pages=d)
        livre.save()

    return render(request, 'creer_livre.html')

def afficher_index(request):

    nom = "abdou"
    prenom = "mohammed"

    return render(request, 'index.html', context={"variable1":nom, "variable2":prenom})



def dashboard(request):
    return render(request, 'dashboard.html', context={
        "first_name":request.session['fname'],
        "last_name": request.session['lname']
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


def afficher_livres(request):
    liste_des_livres = Livre.objects.all() #on a recuperer une liste des livrres qui existent sur la table Livre
    return render(request, 'liste_livres.html', context={"livres":liste_des_livres})


def supprimer_livre(request):

    Livre.delete(id=3)

    redirect('livres')


