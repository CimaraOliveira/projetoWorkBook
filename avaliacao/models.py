from django.db import models
from usuario.models import Usuario, Profissional
from django.utils import timezone

class Avaliacao(models.Model):
    descricao = models.CharField('descricao',max_length=250)
    nota = models.IntegerField('nota', blank=True, null=True)
    data = models.CharField(null=True, name='data_avaliacao', blank=True, max_length=10)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, null=True, blank=True, related_name='profissional')
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True, related_name='cliente')

    class Meta:
        db_table = 'avaliacao'
        verbose_name_plural = 'Avaliações'


