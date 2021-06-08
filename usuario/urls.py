from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [

   path('cadastro/',views.cadastro, name='cadastro'),
   path('submit_login/', views.submit_login, name='submit_login'),
   path('index/', views.index, name='index'),
   path('logout/', views.user_logout,name='user_logout'),
   path('home/', views.index_perfil, name="home"),

]