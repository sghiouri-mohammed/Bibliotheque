from django.shortcuts import render

from elibrary.models import Etudiant


def afficher_index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def registration(request):
    message = "Salut je suis un message"

    if request.method == "POST":

        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        email = request.POST["email"]
        pwd = request.POST["password"]

        etudiant = Etudiant(first_name=first_name, last_name=last_name, email=email, pwd=pwd)

        if etudiant :
            message = "Etudiant ajouté avec success"
            etudiant.save()
        else:
            message = "Veuillez ressayer"

    return render(request, 'Register.html', context={"abdou":message} )




