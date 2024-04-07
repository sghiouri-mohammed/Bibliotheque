from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path( "", views.login, name="index"),
    path("index/", views.afficher_index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("about/", views.about, name="aboutme"),
    path("reserver_livre/", views.ajouter_reservation, name="reserver"),
    path("Register/", views.registration, name="registration"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("form_livre/", views.page_creation_livre, name="livre"),
    path("livres/", views.afficher_livres, name="livres"),
    path("Supp_livre/<int:id_livre>", views.supprimer_livre, name="supprimer_livre"),
    path("Modifier_livre/<int:id_livre>", views.modifier_livre, name="modifier_livre"),
    path("Modifier_etudiant/<int:id_etudiant>", views.modifier_etudiant, name="modifier_etudiant"),
    path("Supprimer_Etudiante/<int:id_etudiant>", views.supprimer_etudiant, name="supprimer_etudiant"),
    path("etudiants/", views.liste_utilisateurs, name="etudiants"),

]