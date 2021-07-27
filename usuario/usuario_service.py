from rest_framework import viewsets
from .models import Usuario, Profissional, Categoria
from .serializers import UsuarioSerializer, ProfissionalSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
      Api de Usuarios WorkBook
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ProfissionalViewSet(viewsets.ModelViewSet):
    """
     Api de Profissionais WorkBook
    """
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer


