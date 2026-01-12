from django.db import models

# Create your models here.
class Giornalista (models.Model):
    nome=models.CharField(max_length=20) #stringhe di lunghezza massima 20
    cognome=models.CharField(max_length=20)

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

    def __str__(self): #metodo toString
        return self.titolo
    
    #serve per modificare il nome di default (Articolos --> Articolo)
    class Meta:
        verbose_name="Articolo"
        verbose_name_plural="Articoli"