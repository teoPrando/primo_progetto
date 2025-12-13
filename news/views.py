from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Articolo,Giornalista

# Create your views here.
def home(request):
    """ LETTURA OGGETTI IN STRINGHE
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
    """
    """LETTURA OGGETTI IN ARRAY DI STRINGHE
    a=[]
    g=[]
    for art in Articolo.objects.all(): #itera per tutti gli articoli nel database
        a.append(art.titolo)

    for gio in Giornalista.objects.all(): #itera per tutti i giornalisti nel database
        g.append(gio.nome)

    response=str(a) + "<br>" + str(g)
    print(response)
    return HttpResponse("<h1>"+response+"</h1>")
    """
    articoli=Articolo.objects.all() #articoli diventa una lista di Articoli
    giornalisti=Giornalista.objects.all() #giornalisti diventa una lista di Giornalisti
    context={"articoli":articoli,"giornalisti":giornalisti}
    print(context)
    return render(request,"news/homepage.html",context)

def articoloDetailView(request,pk): #il paramtero pk sta per la primary key che identifica l'articolo
    articolo= get_object_or_404(Articolo,pk=pk) #ritorna l'oggetto nel database Articolo con primary key uguale a quella passata come parametro
    context={"articolo":articolo}
    return render(request,"articolo_detail.html",context)

