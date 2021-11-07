from django.test import TestCase
from ..form import FormDadosPessoais


class UsuarioFormTestCase(TestCase):
        def test_usuario_form_valido(self):
            form = FormDadosPessoais(data={
                'username': "Testando",
                'first_name': "Teste",
                'telefone': "(84) 99999 9999",
                'email': "teste@gmail.com",
                'password': "123",
                'cidade': "Portalegre",
                'rua': "teste123",
                'uf': "RN",
                'bairro': "centro",
                'imagem': 'teste',
                'date_joined': '2021-08-23'
            })
           # print('form', form)
            self.assertTrue(form.is_valid())

        def test_pessoa_form_invalido(self):
            form = FormDadosPessoais(data={})
            self.assertFalse(form.is_valid())

