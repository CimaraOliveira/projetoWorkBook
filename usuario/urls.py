from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [


   path('cadastro/',views.cadastro, name='cadastro'),
   path('index/', views.index, name='index'),
   path('add_perfil/<int:id>', views.add_perfil, name='add_perfil'),
   path('', views.home, name='home'),
   path('teste/', views.teste, name='teste'),
   path('submit_login/', views.submit_login, name='submit_login'),
   path('logout/', views.logout_user, name='logout_user'),
   path('listarProfissional', views.listarProfissional, name='listarProfissional'),
   path('buscar', views.buscar, name='buscar'),
   path('teste', views.teste, name='teste'),
   path('dadosPessoais/<int:id>', views.dadosPessoais, name='dadosPessoais'),
   path('dadosProfissional/<int:user_id>', views.dadosProfissional, name='dadosProfissional'),
   #path('profissional_detail/<int:user_id>', views.dadosProfissional, name='dadosProfissional'),
   path('<slug>', views.DetalhesProfissional.as_view(), name='detalhesProfissional'),
   #path('<pk>', views.DetalhesProfissional.as_view(), name='detalhesProfissional'),
   #path('detalhesProfissional/<int:id>', views.detalhesProfissional, name='detalhesProfissional')

]