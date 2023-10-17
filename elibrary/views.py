from django.shortcuts import render

from elibrary.models import Etudiant


def afficher_index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def registration(request):
    message = ""


    if request.method == "POST":

        firstname = request.POST["firstname"] #fname f:first
        last_name = request.POST["lname"] #lname l:last
        email = request.POST["email"]
        pwd = request.POST["password"]

        etudiant = Etudiant(first_name=firstname, last_name=last_name, email=email, pwd=pwd)

        if etudiant :
            message = "Etudiant ajouté avec success"
            etudiant.save() #c'est pour enregistrer l'etudiant sur la base de donnees
        else:
            message = "Veuillez ressayer"

    return render(request, 'Register.html', context={"abdou":message} )




