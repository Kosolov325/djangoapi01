from django.db import models
import datetime

class Car(models.Model):
    #So... guys from Unipe's fabrica xD
    # i didn't it as a constructor respecting herachy and stuff cause i was tired... sry
    #Year Options for users :) 
    def yearsField():
        oldestYear = 1900
        actualYear = datetime.datetime.now().year + 1
        yearsOps= []
        for i in range(oldestYear, actualYear):
            yearsOps.append((i,i))

        year = models.IntegerField(('Ano'), choices=yearsOps, default=actualYear)
        return year
    
    #Marcas list from database
    def marcasField():
        marcas = ['Nizan', 'Wolkswaggen', 'Forde', 'Macetes-Bens', 'Seburu', 'Heundie', 'Fito', 'Cheyvroule']
        marcasList = []
        for m in marcas:
            marcasList.append((m,m))
        marca = models.CharField(('Marca'),max_length=50, choices=marcasList, default=marcasList[3])
        return marca     


    nome = models.CharField(('Nome'),max_length=50, blank = False)
    marca = marcasField()
    ano = yearsField()
    desc = models.TextField(('Descrição'))
    def __str__(self) -> str:
        return self.nome
