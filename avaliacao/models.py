from django.db import models
from usuario.models import Usuario, Profissional
from django.utils import timezone

class Avaliacao(models.Model):
    descricao = models.CharField('descricao',max_length=250,blank=True, null=True)
    nota = models.IntegerField('nota', blank=True, null=True)
    data_created = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True, related_name='cliente')
    profissional = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True, related_name='profissional')

    class Meta:
        db_table = 'avaliacao'
        verbose_name_plural = 'Avaliações'




