from django.contrib import auth
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Usuario, Profissional, Categoria
from .serializers import UsuarioSerializer, ProfissionalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class UsuarioViewSet(viewsets.ModelViewSet):
    """
      Api de Usuarios WorkBook
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(methods=['get'], detail=False, url_path='get_by_id')
    def get_by_id(self, request):
        id_str = "id"
        id = self.request.GET.get(id_str) or self.request.session[id_str]
        usuario = Usuario.objects.get(id=id)
        if usuario:
            return Response(status=status.HTTP_200_OK,
                            data=UsuarioSerializer(instance=usuario,
                                                context={'request': request}).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=False, url_path='get_by_auth_key')
    def get_by_auth_key(self, request):
        auth_key_str = "key"
        auth_key_user = self.request.GET.get(auth_key_str) or self.request.session[auth_key_str]
        query_token = Token.objects.filter(key=auth_key_user).values()[0]
        print('Token',query_token)
        return Response(status=status.HTTP_200_OK,
                        data={"id": query_token['user_id']})

    @action(methods=['get'], detail=False, url_path='get_by_username_password')
    def get_by_username_password(self, request):
        username_str = "username"
        password_str = "password"
        username_user = self.request.GET.get(username_str) or self.request.session[username_str]
        password_user = self.request.GET.get(password_str) or self.request.session[password_str]
        print(username_user, password_user)
        user = auth.authenticate(username=username_user, password=password_user)
        if user is not None:
            query_token = Token.objects.filter(user_id=user.id).values()[0]
            print('Token', query_token)
            return Response(status=status.HTTP_200_OK,
                            data={"key": query_token['key']})
        return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Usuário nao encontrado!"})

class ProfissionalViewSet(viewsets.ModelViewSet):
    """
     Api de Profissionais WorkBook
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer


