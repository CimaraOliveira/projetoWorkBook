from django.db import models
from usuario.models import Usuario, Profissional

class TesteAvaliacao(models.Model):
    descricao = models.CharField('descricao',blank=True, null=True,max_length=250)
    nota = models.IntegerField('nota', blank=True, null=True)
    data_avaliacao = models.CharField(null=True, blank=True, max_length=10)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True, related_name='usuarioCliente')
    #profissional = models.ForeignKey(Usuario, on_delete= models.CASCADE, null=True, blank=True, related_name='usuarioProfissional')
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, null=True, blank=True, related_name='usuarioProfissional')

    class Meta:
        db_table = 'testeAvaliacao'
        verbose_name_plural = 'testeAvaliacao'



