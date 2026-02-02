from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Articolo,Giornalista
import datetime
from django.db.models import Q

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

def index(request):
    return render(request,"news/index.html")
def articoloDetailView(request,pk): #il paramtero pk sta per la primary key che identifica l'articolo
    articolo= get_object_or_404(Articolo,pk=pk) #ritorna l'oggetto nel database Articolo con primary key uguale a quella passata come parametro
    context={"articolo":articolo}
    return render(request,"articolo_detail.html",context)

def giornalistaDetailView(request,pk): #il paramtero pk sta per la primary key che identifica il giornalista
    giornalista= get_object_or_404(Giornalista,pk=pk) #ritorna l'oggetto nel database Articolo con primary key uguale a quella passata come parametro
    articoli_giornalista=Articolo.objects.filter(giornalista=giornalista) #lista di articoli scritti dal giornalista
    context={"giornalista":giornalista,
             "articoli_giornalista":articoli_giornalista}
    return render(request,"giornalista_detail.html",context)

#ritorna articoli di un giornalista, se non specificato mostra tutti gli articoli
def lista_articoli(request,pk=None):  #pk=None: se non viene passato pk mostra tutti gli articoli
    if(pk==None):
        intestazione="Tutti gli articoli:"
        articoli=Articolo.objects.all() #articoli diventa una lista di tutti gli Articoli
    else:
        intestazione="Articoli di un giornalista:"
        articoli = Articolo.objects.filter(giornalista=pk) #filter ritorna una lista di oggetti articolo (differente da get_object sopra)
    context={
        'intestazione': intestazione,
        'articoli': articoli,
    }
    return render(request,'lista_articoli.html',context)

#funzione per le query
def queryBase(request):
    #1.Tutti gli articoli scritti da un giornalista di un certo cognome
    articoli_cognome=Articolo.objects.filter(giornalista__cognome='Rossi') #ritorna una lista di tutti gli oggetti contenuti nel db con cognome='Rossi'
    #2.Totale degli articoli
    numero_totale_articoli=Articolo.objects.count()
    #3.Contare il numero di articoli scritti da un giornalista specifico
    try:
        giornalista_1=Giornalista.objects.get(id=1) #ritorna l'oggetto con id=1 (se non lo trova lancia un eccezione DoesNotExixst)
        numero_articoli_giornalista_1=Articolo.objects.filter(giornlista=giornalista_1).count() #conta la lunghezza della lista ritornata dalla funzione filter
    except Giornalista.DoesNotExist: #se il giornalista non esiste
        numero_articoli_giornalista_1=0
    # 4. Ordinare gli articoli per numero di visualizzazioni in ordine decrescente
    articoli_ordinati = Articolo.objects.order_by('-visualizzazioni') 
    # 5. Tutti gli articoli che non hanno visualizzazioni
    articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni=0) #ritorna una lista di oggetti articolo dove il campo visualizzaizioni=0
    # 6. Articolo più visualizzato
    articolo_piu_visualizzato = Articolo.objects.order_by('-visualizzazioni').first() #utilizzando la stessa funzione di prima, ritorna con .first() il primo elemento (se non ci sono articoli è None)
    # 7. Tutti i giornalisti nati dopo una certa data
    giornalisti_data = Giornalista.objects.filter(anno_di_nascita__gt=datetime.date(1990, 1, 1)) #__gt sta per greater than (quindi ritorna un lista di giornalisti nati dopo una certa data)
    # 8. Tutti gli articoli pubblicati in una data specifica
    articoli_del_giorno = Articolo.objects.filter(data=datetime.date(2023, 1, 1)) #ritorna una lista di articoli scritti il 1 gennaio 2023
    # 9. Tutti gli articoli pubblicati in un intervallo di date
    articoli_periodo = Articolo.objects.filter(data__range=(datetime.date(2023, 1, 1),datetime.date(2023, 12, 31))) #ritorna una lista di articoli scritti nel 2023
    # 10. Gli articoli scritti da giornalisti nati prima del 1980
    giornalisti_nati = Giornalista.objects.filter(anno_di_nascita__lt=datetime.date(1980, 1, 1)) #__lt indica quelli nati prima (contrario di __gt)
    articoli_giornalisti_nati = Articolo.objects.filter(giornalista__in=giornalisti_nati) 
    # 11. Il giornalista più giovane
    giornalista_giovane = Giornalista.objects.order_by('-anno_di_nascita').first()#ordine decrescente (dal + giovane al + anziano)
    # 12. Il giornalista più anziano
    giornalista_anziano = Giornalista.objects.order_by('anno_di_nascita').first()#ordine crescente (dal + anziano al + giovane)
    # 13. Gli ultimi 5 articoli pubblicati
    ultimi = Articolo.objects.order_by('-data')[:5] #prende i primi 5 articoli della lista di articoli ordianta dal + recente al meno recente
    # 14. Tutti gli articoli con un certo numero minimo di visualizzazioni
    articoli_minime_visualizzazioni = Articolo.objects.filter(visualizzazioni__gte=100) #__gte sta per greater than or equals (visualizzaizzioni >=100)
    # 15. Tutti gli articoli che contengono una certa parola nel titolo
    articoli_parola = Articolo.objects.filter(titolo__icontains='importante') #__icontains serve per verificare che nel campo titolo ci sia la parola 'importante'
    # 16. Articoli pubblicati in un certo mese di un anno specifico
    articoli_mese_anno = Articolo.objects.filter(data__month=1, data__year=2023) #due condizioni separate dalla virgola corrispondono all' AND
    # 17. Giornalisti con almeno un articolo con + di 100 visualizzazioni
    giornalisti_con_articoli_popolari = Giornalista.objects.filter(articoli__visualizzazioni__gte=100).distinct() #.distinct fa in modo di non prendere due volte lo stesso giornalista
    # 18. Articoli scritti da giornalisti nati dopo il 1/1/1990 E (AND) con almeno 50 visualizzazioni
    articoli_con_and= Articolo.objects.filter(giornalista__anno_di_nascita__gte=datetime.date(1990,1,1), visualizzazioni__gte=50)
    # 19. Articoli scritti da giornalisti nati dopo il 1/1/1990 O (OR) con meno di 50 visualizzazioni
    articoli_con_or = Articolo.objects.filter(Q(giornalista__anno_di_nascita__gte=datetime.date(1990,1,1)) | Q(visualizzazioni__lte=50)) #per l' OR viene utilizzato l'operatore Q davanti alle condizioni separate da |
    # 20. Articoli scritti da giornalisti nati dopo l'1/1/1990 
    articoli_con_not=Articolo.objects.filter(~Q(giornalista__anno_di_nascita__lt=datetime.date(1990, 1, 1))) #nega la condizione (ovvero quelli nati prima del 1/1/1990)
    #oppure
    # articoli_con_not=Articolo.objects.exclude(giornalista__anno_di_nascita__lt=datetime.date(1990, 1, 1)) esclude quelli nati prima

    #dizionario context
    context = {
        'articoli_cognome': articoli_cognome,
        'numero_totale_articoli': numero_totale_articoli,
        'numero_articoli_giornalista_1': numero_articoli_giornalista_1,
        'articoli_ordinati': articoli_ordinati,
        'articoli_senza_visualizzazioni': articoli_senza_visualizzazioni,
        'articolo_piu_visualizzato': articolo_piu_visualizzato,
        'giornalisti_data': giornalisti_data,
        'articoli_del_giorno': articoli_del_giorno,
        'articoli_periodo': articoli_periodo,
        'articoli_giornalisti_nati': articoli_giornalisti_nati,
        'giornalista_giovane': giornalista_giovane,
        'giornalista_anziano': giornalista_anziano,
        'ultimi': ultimi,
        'articoli_minime_visualizzazioni': articoli_minime_visualizzazioni,
        'articoli_parola': articoli_parola,
        'articoli_mese_anno': articoli_mese_anno,
        'giornalisti_con_articoli_popolari':giornalisti_con_articoli_popolari,
        'articoli_con_and':articoli_con_and,
        'articoli_con_or':articoli_con_or,
        'articoli_con_not':articoli_con_not
    }
    return render(request,"query.html",context=context)
