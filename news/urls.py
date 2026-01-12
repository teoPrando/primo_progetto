from django.urls import path
from .views import home,articoloDetailView,lista_articoli


app_name="news"

urlpatterns=[
    path('',home,name="homeview"),
    path('articoli/<int:pk>',articoloDetailView,name="articoloDetail"),  #quando digiterò l'url, al posto di <int:pk> dovrò mettere la primary key di articolo
    path('lista_articoli/',lista_articoli,name="lista_articoli"), # quando non digito niente dopo lista_articoli pk=None
    path('lista_articoli/<int:pk>',lista_articoli,name="lista_articoli")  #quando digiterò l'url, al posto di <int:pk> dovrò mettere la primary key di giornalista
    
]