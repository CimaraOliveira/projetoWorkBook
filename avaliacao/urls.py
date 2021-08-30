from django.urls import path
from . import views

app_name = 'avaliacao'

urlpatterns = [

   path('avaliacao/<id>', views.avaliacao, name="avaliacao"),
   path('listarAvaliacao/>', views.listarAvaliacao, name="listarAvaliacao"),
   path('clientelistarAvaliacoes/', views.clientelistarAvaliacoes, name='clientelistarAvaliacoes'),


]