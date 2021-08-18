from django.urls import path
from . import views

urlpatterns = [
    path('avaliacao_teste/<id>', views.avaliacao_teste, name='avaliacao_teste'),
    path('listar/', views.listar, name='listar')

]