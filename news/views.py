from django.http import HttpResponse
from .models import Articolo,Giornalista

# Create your views here.
def home(request):
    a=""
    g=""
    for art in Articolo.objects.all(): #itera per tutti gli articoli nel database
        a+=(art.titolo+"<br>")

    for gio in Giornalista.objects.all(): #itera per tutti i giornalisti nel database
        g+=(gio.nome+" "+gio.cognome+"<br>")

    #dopo questi due for, dentro a e g ci sono tutti i titoli degli articoli (a) e tutti i nomi dei giornalisti (g)
    #uno per riga
    response="Articoli: <br>"+a+"<br>Giornalisti: <br>"+g
    return HttpResponse("<h1>"+response+"</h1>")
