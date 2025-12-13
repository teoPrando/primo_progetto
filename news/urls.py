from django.urls import path
from .views import home,articoloDetailView

app_name="news"

urlpatterns=[
    path('',home,name="homeview"),
    path('articoli/<int:pk>',articoloDetailView,name="articoloDetail")  #quando digiterò l'url, al posto di <int:pk> dovrò mettere la primary key 
]