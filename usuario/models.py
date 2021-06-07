from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    cidade = models.CharField('cidade', max_length=250,null=True, blank=True)
    estado = models.CharField('estado', max_length=250,null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=20,null=True, blank=True)
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

