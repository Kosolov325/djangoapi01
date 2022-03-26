from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100, blank = False)
    texto = models.TextField()

    def __str__(self) -> str:
        return self.titulo
