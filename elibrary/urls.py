from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("abdou/", views.afficher_index, name="index"),
    path("dash/", views.dashboard, name="dashbaord"),
    path("Register/", views.registration, name="registration"),

]