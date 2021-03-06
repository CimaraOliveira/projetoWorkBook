from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from rest_framework.authtoken.models import Token

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']



class Usuario(AbstractUser):
    telefone = models.CharField('telefone', max_length=15)
    imagem = models.ImageField(upload_to='fotosperfil/%Y/%m/', blank=True, null=True)
    cidade = models.CharField('cidade', max_length=40)
    rua = models.CharField('rua', max_length=60)
    uf = models.CharField('uf', max_length=2)
    bairro = models.CharField('bairro', max_length=40)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_profissional = models.BooleanField(default=False)



    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuario'

class Profissional(models.Model):
            profissao = models.CharField('Profissão', max_length=250)
            categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria')
            slug = models.SlugField('Atalho', unique=True, blank=True, null=True)
            descricao = models.CharField('Descrição', max_length=250)
            imagem = models.ImageField(upload_to='fotos/%Y/%m/', blank=True, null=True)
            user = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='usario',
                                        error_messages={
                                            "unique": "Já existe um profissional cadastrado para este usuário."
                                        }
                                       )
            acesso_permitido = models.BooleanField(default=True)


            def __str__(self):
                return self.profissao

            def save(self, *args, **kwargs):
                if not self.slug:
                    slug = f'{slugify(self.user)}'
                    self.slug = slug
                super().save(*args, **kwargs)

            """def clean(self):
                error_messages = {}
                if not valida_cpf(self.cpf):
                    error_messages['cpf'] = 'Digite um cpf Válido!'

                if error_messages:
                    raise ValidationError(error_messages)"""

            class Meta:
                verbose_name = 'Profissional'
                verbose_name_plural = 'Profissional'
                ordering = ['id']




