from django.contrib import admin
from .models import Articolo,Giornalista


admin.site.register(Articolo) #permette la registrazione degli articoli dal pannello admin
admin.site.register(Giornalista) #permette la registrazione dei giornalisti dal pannello admin
# Register your models here.
