from django.db import models
from django.utils import timezone
from mensagem.models import Mensagem

class Notificacao(models.Model):
    data_notificacao = models.DateTimeField('Data Notificação', null=True,
                                            blank=False, default=timezone.now)
    lido = models.BooleanField(name="lido", default=False)
    texto = models.CharField(max_length=255, null=True, blank=False)
    mensagemRecebida = models.ForeignKey(Mensagem, null=True, blank=False, on_delete=models.CASCADE,
                                         related_name='mensagemRecebida')

    class Meta:
        db_table = 'Notificacao'
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'
