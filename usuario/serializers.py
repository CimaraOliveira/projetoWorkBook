from rest_framework import serializers
from usuario.models import Usuario, Profissional, Categoria

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
      model = Usuario
      fields = ('__all__')

class ProfissionalSerializer(serializers.ModelSerializer):
        class Meta:
              model = Profissional
              fields = ('__all__')

