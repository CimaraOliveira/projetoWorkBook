import json

from django.core import serializers
from django.db.models import base
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response

from avaliacao.models import Avaliacao
from mensagem.models import Mensagem
from usuario.models import Usuario
from .models import Notificacao
from .serializers import NotificacaoSerializer

from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication


class NotificacaoViewSet(viewsets.ModelViewSet):
    """
    API de Avaliações WorkBook
    """

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Avaliacao.objects.all()
    serializer_class = NotificacaoSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

    @action(methods=['put'], detail=False, url_path='atualizar_status')
    def atualizar_status(self, request, *args, **kwargs):
        id_str = "id"
        notificacao_id = self.request.GET.get(id_str) or self.request.session[id_str]
        # Notificacao._do_update(update_fields=['lido'], base_qs=Notificacao, forced_update=True, values=[True], pk_val=notificacao_id)
        # base.Model._do_update(self=self, base_qs=Notificacao.objects, using=None, pk_val=notificacao_id, values=[True], update_fields=['lido'], forced_update=False)
        # return Response(status=status.HTTP_200_OK, data=NotificacaoSerializer(instance=None,
        #    context={'request': request}).data)
        notificacao = Notificacao.objects.filter(id=notificacao_id).update(lido=True)
        return Response(status=status.HTTP_200_OK, data=NotificacaoSerializer(instance=notificacao,
                                                                              context={'request': request}).data)

    @action(methods=['get'], detail=False, url_path='get_status')
    def get_status(self, request):
        token_str = "token"
        token_user = self.request.GET.get(token_str) or self.request.session[token_str]
        query_token = Token.objects.filter(key=token_user).values()[0]
        print('ID USER -> ', query_token['key'])

        def len_por_usuario(destinatario, remetente):
            sql = "select * from Notificacao n2 " \
                  "where n2.lido = 0 and n2.id in ( " \
                  "SELECT n3.id FROM Mensagen m2 " \
                  "inner join Notificacao n3 on m2.id = n3.mensagemRecebida_id " \
                  "inner join usuario u2 on m2.destinatario_id = u2.id " \
                  "inner join usuario u3 on m2.remetente_id = u3.id " \
                  "where u2.id = %s and u3.id = %s )"
            notificacoes = Notificacao.objects.raw(sql, [destinatario, remetente])
            return len(notificacoes)

        def notificacoes_por_usuario(id):
            # essa query vai pegar as notificacoes nao lida.

            sql = "select * from Notificacao n " \
                  "WHERE n.id in ( " \
                  " select n2.id from Notificacao n2 inner join Mensagen m on m.id = n2.mensagemRecebida_id " \
                  " inner join usuario u on m.destinatario_id = u.id " \
                  " where u.id = %s and n.lido = 0 GROUP by m.remetente_id HAVING max(n2.id) " \
                  " ) ORDER by n.id DESC"
            notificacoes = Notificacao.objects.raw(sql, [id])
            obj = []
            for notificacao in notificacoes:
                remetente = notificacao.mensagemRecebida.remetente
                jsonNotificacoes = {
                    "notificacao": NotificacaoSerializer(instance=notificacao, context={'request': request}).data,
                    "size": len_por_usuario(id, remetente.id)
                }
                obj.append(jsonNotificacoes)
            return json.dumps(obj)

        return HttpResponse(notificacoes_por_usuario(query_token['user_id']))

