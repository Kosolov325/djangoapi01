from django.forms import ModelForm
from .models import Post

class RegistroPost(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'texto']
