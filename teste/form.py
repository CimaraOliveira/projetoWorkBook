from django.forms import ModelForm
from .models import TesteAvaliacao

class AvaliacaoForm(ModelForm):
    class Meta:
        model = TesteAvaliacao
        fields = '__all__'
        #exclude = ('cliente',)
        #exclude = ('profissional',)
        #exclude = ('cliente', 'profissional',)
