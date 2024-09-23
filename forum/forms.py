from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'description', 'tags', 'file']  # Укажите поля, которые хотите включить в форму
