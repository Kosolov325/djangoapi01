from django.forms import ModelForm
from .models import Car

class CreateCar(ModelForm):
    class Meta:
        model = Car
        fields = ['nome', 'marca', 'ano', 'desc']