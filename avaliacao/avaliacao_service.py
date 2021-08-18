from rest_framework import viewsets
from .models import Avaliacao
from .serializers import AvaliacaoSerializer
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication


class AvaliacaoViewSet(viewsets.ModelViewSet):
    """
    API de Avaliações WorkBook
    """

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'



