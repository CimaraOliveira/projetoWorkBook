from django.test import TestCase
from django.urls import  reverse

class UsuariViewTestCase(TestCase):

    def test_status_code_200(self):

        response = self.client.get('/home/')
        #print('response', response.status_code)
        self.assertEquals(response.status_code, 200)

    def test_template_usado(self):

        response = self.client.get('/home/')
        self.assertTemplateUsed(response,'usuario/home.html')