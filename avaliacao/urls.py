from django.urls import path
from . import views

app_name = 'avaliacao'

urlpatterns = [

   path('avaliacao/<id>', views.avaliacao, name="avaliacao"),
   path('listarAvaliacao/', views.listarAvaliacao, name="listarAvaliacao"),
   path('clientelistarAvaliacoes/<id>', views.clientelistarAvaliacoes, name='clientelistarAvaliacoes'),

   #http://127.0.0.1:8000/avaliacao/clientelistarAvaliacoes/2

]