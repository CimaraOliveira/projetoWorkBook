from django.db.models import Q
from rest_framework import viewsets, status
from datetime import datetime
from rest_framework.decorators import action

from notificacoes.models import Notificacao
from usuario.models import Usuario
from .models import Mensagem
from .serializers import MensagemSerializer
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token


class MensagemViewSet(viewsets.ModelViewSet):
    """
    API de Mensagens WorkBook
    """

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

    def create(self, request, *args, **kwargs):
        mensagemReq = request.data
        mensagem = Mensagem.objects.create(texto=mensagemReq['texto'], destinatario=Usuario.objects.get(id=mensagemReq['destinatario']), remetente=Usuario.objects.get(id=mensagemReq['remetente']), data_mensagem=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        Mensagem.save(mensagem)
        noticacao = Notificacao.objects.create(texto=mensagemReq['texto'], mensagemRecebida=mensagem)
        Notificacao.save(noticacao)
        return Response(status=status.HTTP_201_CREATED,
                        data=MensagemSerializer(instance=mensagem,
                                                context={'request': request}).data)

    @action(methods=['get'], detail=False, url_path='get_by_id')
    def get_by_id(self, request):
        id_str = "id"
        id = self.request.GET.get(id_str) or self.request.session[id_str]
        mensagem = Mensagem.objects.get(id=id)
        if mensagem:
            return Response(status=status.HTTP_200_OK,
                            data=MensagemSerializer(instance=mensagem,
                                                   context={'request': request}).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=False, url_path='get_by_last_messages')
    def get_by_last_messages(self, request):
        token_str = "token"
        token_user = self.request.GET.get(token_str) or self.request.session[token_str]
        query_token = Token.objects.filter(key=token_user).values()[0]
        print('ID USER -> ', query_token['key'])

        def mensagens_por_usuario(id):
            # essa query vai pegar a ultima mensagem feita pelo remetente ou pelo destinatario.

            sql = "select * from usuario u where u.id in (select u2.id from usuario u2" \
                  "	inner join Mensagen m on(u2.id = m.remetente_id) " \
                  "	where u2.id != (select u3.id from usuario u3 where u3.id = %s and u3.id =" \
                  " m.destinatario_id) ORDER by m.id desc)" \
                  "	OR u.id in (" \
                  "	select u4.id from usuario u4 " \
                  "inner join Mensagen m2 on(u4.id = m2.destinatario_id)" \
                  "	where u4.id != (select u5.id from usuario u5 where u5.id =" \
                  " %s and u5.id = m2.remetente_id) ORDER by m2.id DESC) ORDER by u.id DESC"
            usuarios = Usuario.objects.raw(sql, [id, id])

            mensagens = []
            for user in usuarios:
                if user.id != id:
                    mensagem = Mensagem.objects.filter((Q(destinatario__id=user.id) & Q(remetente__id=id)) | (
                            Q(remetente__id=user.id) & Q(destinatario__id=id))).last()
                    if mensagem:
                        mensagens.append(mensagem)

            return mensagens

        return Response(status=status.HTTP_200_OK,
                        data=MensagemSerializer(instance=mensagens_por_usuario(query_token['user_id']), many=True,
                                                context={'request': request}).data)


    @action(methods=['get'], detail=False, url_path='get_by_detalhe_mensagens')
    def get_by_detalhe_mensagens(self, request):
        id_remetente_str = "remetente"
        id_destinatario_str = "destinatario"
        id_remetente = self.request.GET.get(id_remetente_str) or self.request.session[id_remetente_str]
        id_destinatario = self.request.GET.get(id_destinatario_str) or self.request.session[id_destinatario_str]

        mensagens_detalhe = Mensagem.objects.filter(
            (Q(destinatario__id=id_destinatario) & Q(remetente__id=id_remetente)) |
            (Q(destinatario__id=id_remetente) & Q(remetente__id=id_destinatario))).order_by('id')

        return Response(status=status.HTTP_200_OK,
                        data=MensagemSerializer(instance=mensagens_detalhe, many=True,
                                                context={'request': request}).data)
