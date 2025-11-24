#from django.shortcuts import render
import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"prova_pratica_1/index.html")

def differenza(request):
    n1=int(random.random()*20+1)
    n2=int(random.random()*20+1)
    diff=0 
    if(n1>n2):
        diff=n1-n2
    elif(n1<n2):
        diff=n2-n1
    #se i due numeri sono uguali, diff rimane 0
    numeri_random={
        'num1': n1,
        'num2': n2,
        'diff': diff
    }
    return render(request,"prova_pratica_1/diff.html",numeri_random)

def pari_dispari(request):
    lista_random=[]
    cont_pari=0
    cont_dispari=0
    for i in range(15):
        n=int(random.random()*20+1)
        lista_random.append(n)
        if(n%2==0):
            cont_pari+=1
        else:
            cont_dispari+=1
    numeri={
        "lista": lista_random,
        "n_pari": cont_pari,
        "n_dispari": cont_dispari
    } 
    return render(request,"prova_pratica_1/pari.html",numeri)



