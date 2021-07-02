from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [

   path('cadastro/',views.cadastro, name='cadastro'),
   path('teste/', views.teste, name='teste'),
   path('submit_login/', views.submit_login, name='submit_login'),

]