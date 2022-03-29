from django.contrib.auth.models import User
from django.db import models
import datetime


class Marca(models.Model):
    nome  = models.CharField(('Nome'),max_length=50, blank = False)
    photo = models.ImageField(('Logo'), default='' ,upload_to='static/assets')
    desc  = models.TextField(('Descrição'), default='')

    def __str__(self):
        return self.nome

class Car(models.Model):
    #So... guys from Unipe's fabrica xD
    # i didn't it as a constructor respecting herachy and stuff cause i was tired... sry
    #Year Options for users :) 
    def yearsField():
        oldestYear = 1930
        actualYear = datetime.datetime.now().year + 1
        yearsOps= []
        for i in range(oldestYear, actualYear):
            yearsOps.append((i,i))

        year = models.IntegerField(('Ano'), choices=yearsOps, default=actualYear)
        return year

    nome = models.CharField(('Nome'),max_length=50, blank = False)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    ano = yearsField()
    desc = models.TextField(('Descrição'), default='')
    photo = models.ImageField(('Foto'),upload_to='static/assets', default='assets/carro.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    def __str__(self):
        return self.nome
