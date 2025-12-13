from django.db import models

# Create your models here.
class Giornalista (models.Model):
    nome=models.CharField(max_length=20) #stringhe di lunghezza massima 20
    cognome=models.CharField(max_length=20)

    def __str__(self): #metodo toString
        return self.nome + " "+self.cognome
    
class Articolo(models.Model):
    titolo=models.CharField(max_length=100) #stringhe di lunghezza massima 100
    contenuto=models.TextField()
    giornalista=models.ForeignKey(Giornalista,on_delete=models.CASCADE,related_name="articoli")#foreign key che si collega alla tabella Giornalisti
    #Se viene eliminato un giornalista, vengono eliminati tutti i suoi articoli (ON DELETE CASCADE)

    def __str__(self): #metodo toString
        return self.titolo
    