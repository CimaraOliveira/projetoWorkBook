from django.urls import path
from . import views

app_name = 'avaliacao'

urlpatterns = [

   path('avaliacao/<user_id>', views.avaliar, name='avaliar'),
   path('listAvaliacao/', views.listAvaliacao, name='listAvaliacao'),
   path('<user_id>', views.avaliacao, name='avaliacao'),
   path('listar/', views.avaliacao, name='avaliacao'),

]