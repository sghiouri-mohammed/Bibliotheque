from django.shortcuts import render, redirect

from elibrary.models import Etudiant


def afficher_index(request):
    return render(request, 'index.html')


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




