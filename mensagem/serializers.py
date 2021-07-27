from rest_framework import serializers
from .models import Mensagem
from .views import detalheMensagem
from .models import Usuario
from usuario.usuario_service import UsuarioSerializer

class MensagemSerializer(serializers.ModelSerializer):
       class Meta:
        model = Mensagem
        fields = (
                  'id',
                  'texto',
                  'destinatario',
                  'remetente',

                  )