from django.urls import path
from .views import home,articoloDetailView,lista_articoli,queryBase,giornalistaDetailView,index


app_name="news"

urlpatterns=[
    path('home/',home,name="homeview"),
    path('index/',index,name="index"),
    path('articoli/<int:pk>',articoloDetailView,name="articoloDetail"),  #quando digiterò l'url, al posto di <int:pk> dovrò mettere la primary key di articolo
    path('lista_articoli/',lista_articoli,name="lista_articoli"), # quando non digito niente dopo lista_articoli pk=None
    path('lista_articoli/<int:pk>',lista_articoli,name="lista_articoli"),  #quando digiterò l'url, al posto di <int:pk> dovrò mettere la primary key di giornalista
    path('query',queryBase,name="query_base"),
    path('giornalisti/<int:pk>',giornalistaDetailView,name="giornalistaDetail"),  #quando digiterò l'url, al posto di <int:pk> dovrò mettere la primary key di giornalista
    
    
]