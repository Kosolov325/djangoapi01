from django.forms import ModelForm
from .models import Car, Marca
from django.contrib.auth.models import User


class CreateUser(ModelForm):
    class Meta:
        model = User
        help_texts = { 'username': None, }
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class CreateCar(ModelForm):
    class Meta:
        model = Car
        fields = ['nome', 'marca', 'ano', 'desc', 'photo']


class CreateMarca(ModelForm):
    class Meta:
        model = Marca
        fields = ['nome', 'photo', 'desc']