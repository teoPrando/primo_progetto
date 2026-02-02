from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator #permette di controllare i valori minimi e massimi(es: visualizzazioni >0)
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Giornalista (models.Model):
    nome=models.CharField(max_length=20) #stringhe di lunghezza massima 20
    cognome=models.CharField(max_length=20)
    anno_di_nascita=models.DateField(null=True,validators=[MaxValueValidator(limit_value=timezone.now().date(), message="La data di nascita non può essere nel futuro.")])

    def __str__(self): #metodo toString
        return self.nome + " "+self.cognome
    
    #serve per modificare il nome di default (Giornalistas --> Giornalisti)
    class Meta:
        verbose_name="Giornalista"
        verbose_name_plural="Giornalisti"

class Articolo(models.Model):
    titolo=models.CharField(max_length=100) #stringhe di lunghezza massima 100
    contenuto=models.TextField()
    giornalista=models.ForeignKey(Giornalista,on_delete=models.CASCADE,related_name="articoli")#foreign key che si collega alla tabella Giornalisti 
    #Se viene eliminato un giornalista, vengono eliminati tutti i suoi articoli (ON DELETE CASCADE)
    #con related_name, posso accedere agli articoli scritti dal giornalista con (oggetto_giornalista).articoli.all()
    visualizzazioni=models.IntegerField(MinValueValidator(0),default=0) #controlla che sia >=0
    data=models.DateField(null=True,validators=[MaxValueValidator(limit_value=timezone.now().date(), message="La data non può essere nel futuro.")])

    def __str__(self): #metodo toString
        return self.titolo
    
    #serve per modificare il nome di default (Articolos --> Articolo)
    class Meta:
        verbose_name="Articolo"
        verbose_name_plural="Articoli"