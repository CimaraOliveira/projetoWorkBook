from django.db import models
from usuario.models import Usuario
from django.utils import timezone


class Mensagem(models.Model):
    texto = models.CharField('texto', max_length=5000)
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=False,
                                     related_name='destinatario')
    remetente = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=False, related_name='remetente')
    data = models.CharField(null=True, name='data_mensagem', blank=False, max_length=255)

    class Meta:
        db_table = 'Mensagen'
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'


# class Notificacao(models.Model):
#     data_notificacao = models.DateTimeField('Data Notificação', null=True, blank=False, default=timezone.now),
#     notificacao = models.CharField(max_length=255, null=True, blank=False),
#     mensagemRecebida = models.ForeignKey(Mensagem, null=True, blank=False, on_delete=models.CASCADE,
#                                          related_name='mensagemRecebida'),
#
#     class Meta:
#         db_table = 'Notificacao'
#         verbose_name = 'Notificação'
#         verbose_name_plural = 'Notificações'
