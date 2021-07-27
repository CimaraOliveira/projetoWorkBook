from django import forms
from django.forms import ModelForm
from usuario.models import Profissional, Usuario

class FormPerfil(ModelForm):
    class Meta:
        model = Profissional
        fields = '__all__'
        exclude = ('slug','user',)

class FormDadosPessoais(ModelForm):
    class Meta:
        model = Usuario
        exclude = ('is_active','is_staff','is_superuser','user_permissions','groups','last_login','password','status', 'date_joined',)
