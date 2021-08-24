from django.test import TestCase
from ..models import Usuario
import unittest


class UsuarioTesteCase(TestCase):

    def setUp(self):
        Usuario.objects.create(username="Testando", first_name="Teste", telefone="(84) 9 9999 9999",
                               email="teste@gmail.com",
                               password="123", cidade="Portalegre", rua="teste123", uf="RN", bairro="centro")

    def test_return_name(self):
        p1 = Usuario.objects.get(first_name="Teste")
