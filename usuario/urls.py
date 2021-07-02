from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [

   path('cadastro/',views.cadastro, name='cadastro'),
   path('index/', views.index, name='index'),
   path('add_perfil/', views.add_perfil, name='add_perfil'),
   path('home/', views.home, name='home'),
   path('teste/', views.teste, name='teste'),
   path('submit_login/', views.submit_login, name='submit_login'),
   path('logout/', views.logout_user, name='logout_user'),

]