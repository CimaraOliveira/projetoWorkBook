from django import forms
from django.forms import ModelForm
from usuario.models import Perfil

class FormPerfil(ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        exclude = ('user',)