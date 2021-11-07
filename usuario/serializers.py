from rest_framework import serializers
from usuario.models import Usuario, Profissional, Categoria

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
      extra_kwargs = {
            'email': {'write_only': True}
      }  #seguranca para não aparecer o email na api
      model = Usuario
      fields = ('__all__')

class ProfissionalSerializer(serializers.ModelSerializer):
        class Meta:
              model = Profissional
              fields = ('__all__')

