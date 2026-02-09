from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "voti/index.html")

def lista_materie(request):
    context={
        'materie' : ["Matematica","Italiano","Inglese","Storia","Geografia"]
    }
    return render(request, "voti/lista_materie.html",context)

def voti_assenze(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]
           }
    context={
        'voti':voti
    }
    return render(request, "voti/voti_assenze.html",context)

def media_voti(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]
            }
    media_voti={}
    for studente in voti.keys():
        media=0
        for materia,voto,assenze in voti[studente]:
            media+=voto
        media/=len(voti[studente])
        media_voti[studente]=media
    
    context={
        'media_voti' : media_voti
    }
    return render(request,"voti/media_voti.html",context)

"""passa al template un dizionario context con due valori:
'max': [voto_max, [materie_max], [studenti_max]],
'min': [voto_min, [materie_min], [studenti_min]]"""
def max_min_voti(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]
            }
    
    max=0
    min=11
    materie_max=[]
    materie_min=[]
    studenti_max=[]
    studenti_min=[]
    #trovo massimo e minimo
    for studente in voti.keys():
        for materia,voto,assenze in voti[studente]:
            if(voto>max):
                max=voto
            if voto<min:
                min=voto
    #trovo le materie in cui sono stati presi i voti max e min e gli studenti che gli hanno presi
    for studente in voti.keys():
        for materia,voto,assenze in voti[studente]:
            #voto MAX
            if(voto==max): # quando trovo il voto migliore
                if materia not in materie_max: #se lo studente non è ancora stato aggiunto in quelli che hanno preso il voto più alto
                    materie_max.append(materia) #aggiungo la materia alla lista di materie massime
                if studente not in studenti_max: #se lo studente non è ancora stato aggiunto in quelli che hanno preso il voto più alto
                    studenti_max.append(studente) #viene aggiunto
            
            #voto MIN
            if(voto==min): # quando trovo il voto peggiore
                    if materia not in materie_min: #se lo studente non è ancora stato aggiunto in quelli che hanno preso il voto più BASSO
                        materie_min.append(materia) #aggiungo la materia alla lista di materie minime
                    if studente not in studenti_min: #se lo studente non è ancora stato aggiunto in quelli che hanno preso il voto più basso
                        studenti_min.append(studente) #viene aggiunto

    context={
        'max': {
            'voto': max, 
            'materie': materie_max, 
            'studenti': studenti_max
        },
        'min': {
            'voto': min, 
            'materie': materie_min, 
            'studenti': studenti_min
            }
    }
    return render(request, "voti/max_min_voti.html",context)