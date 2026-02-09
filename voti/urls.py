from django.urls import path
from .views import index,lista_materie,voti_assenze,media_voti,max_min_voti


app_name="voti"

urlpatterns=[
    path('',index,name="index"),
    path('lista_materie',lista_materie,name="lista_materie"),
    path('voti_assenze',voti_assenze,name="voti_assenze"),
    path('media_voti',media_voti,name="media_voti"),
    path('max_min_voti',max_min_voti,name="max_min_voti"),

    
    
]