
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #ici je lui dit de suivre les urls du fichier urls.py de l'application
    path('', include('elibrary.urls')),
]
