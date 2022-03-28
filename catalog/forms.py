from django.forms import ModelForm
from .models import Car, Marca

class CreateCar(ModelForm):
    class Meta:
        model = Car
        fields = ['nome', 'marca', 'ano', 'desc', 'photo']


class CreateMarca(ModelForm):
    class Meta:
        model = Marca
        fields = ['nome', 'photo']