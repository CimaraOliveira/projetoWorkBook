from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.text import slugify


class Categoria(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    LOAN_STATUS = (
        ('assist', 'Assistencia Tecnica'),
        ('eventos', 'Eventos'),
        ('moda', 'Moda'),
        ('beleza', 'Beleza'),
        ('reforma', 'Reforma'),
        ('outros', 'Outros'),
    )
    nome = models.CharField(max_length=20, choices=LOAN_STATUS, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Perfil(models.Model):
    first_name = models.CharField('first_name ', max_length=250)
    telefone = models.CharField('telefone', max_length=15)
    profissao = models.CharField('Profissao',max_length=250)
    categoria = models.ManyToManyField(Categoria)
    slug = models.SlugField('Atalho', unique=True, blank=True, null=True)
    descricao = models.CharField('descricao', max_length=250)
    imagem = models.ImageField(upload_to='fotos/%Y/%m/', blank=True, null=True)
    cidade = models.CharField('cidade', max_length=40)
    rua = models.CharField('rua', max_length=60)
    uf = models.CharField('uf', max_length=2)
    bairro = models.CharField('cidade', max_length=40)
    cep = models.CharField('cep', max_length=10)
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.profissao


    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.user)}'
            self.slug = slug

        super().save(*args, **kwargs)

    """def clean(self):
       model = self.__class__
       if model.objects.count() > 0 and self.user_id != model.objects.get().user_id:
            raise ValidationError("Você já tem um perfil cadastrado.")"""


    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
        ordering = ['id']

class Usuario(AbstractUser):
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
        verbose_name_plural = 'Usuario'

