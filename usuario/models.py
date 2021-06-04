from django.db import models
from django.contrib.auth.models import AbstractUser

class Categoria(models.Model):
    nome = models.CharField('nome',max_length=40)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoria'

class Perfil(models.Model):
    nome = models.CharField('nome',max_length=250)
    categorias = models.ManyToManyField(Categoria)
    decricao = models.CharField('descricao', max_length=2000)
    imagem = models.ImageField(upload_to='imagem/%Y/%m/', blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

class Usuario(AbstractUser):
    nome = models.CharField('Nome', max_length=250)
    email = models.EmailField()
    senha = models.CharField('Senha', max_length=250)
    cidade = models.CharField('Cidade', max_length=250)
    estado = models.CharField('Estado', max_length=250)
    telefone = models.CharField('Telefone', max_length=20)
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, null=True, blank=True)
    is_staff = models.BooleanField(default=1)
    is_superuser = models.BooleanField(default=1)
    is_active = models.BooleanField(default=True)
    LOAN_STATUS = (
        ('profissional', 'Profissional'),
        ('cliente', 'Cliente'),

    )
    status = models.CharField(max_length=15, choices=LOAN_STATUS, blank=True)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


