from prova_pratica_1.views import index,differenza,pari_dispari
from django.urls import path

app_name="prova_pratica_1"

urlpatterns=[
    path('',index,name='index'),
    path('differenza',differenza,name='differenza'),
    path('pari_dispari',pari_dispari,name='pari_dispari')
]