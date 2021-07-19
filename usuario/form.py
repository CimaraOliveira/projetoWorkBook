from django import forms
from django.forms import ModelForm
from usuario.models import Profissional

class FormPerfil(ModelForm):
    class Meta:
        model = Profissional
        fields = '__all__'
        exclude = ('user',)