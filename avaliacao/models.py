from django.db import models
from usuario.models import Usuario, Perfil

class Avaliacao(models.Model):
    descricao = models.CharField('descricao',max_length=250)
    nota = models.IntegerField('nota', blank=True, null=True)
    data = models.CharField(null=True, name='data_avaliacao', blank=True, max_length=10)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True, related_name='cliente')
    profissional = models.ForeignKey(Perfil, on_delete= models.CASCADE, null=True, blank=True, related_name='profissional')

    class Meta:
        db_table = 'avaliacao'
        verbose_name_plural = 'Avaliações'


