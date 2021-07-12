from django.urls import path,include
from . import views

urlpatterns = [

   path('enviar/<id>', views.enviar, name='enviar'),
   path('listar/', views.listar, name='listar'),
   path('responder/<int:remetente>', views.responder, name='responder'),
   path('enviarMensagem/<id>', views.enviarMensagem, name='enviarMensagem'),
   path('responderMensagem/<int:idRemetente>/<int:idDestinatario>', views.responderMensagem, name='responderMensagem'),
   path('detalheMensagem/<int:idRemetente>/<int:idDestinatario>', views.detalheMensagem, name='detalheMensagem'),
   path('listarMensagem/<int:idDestinatario>', views.listarMensagem, name='listarMensagem'),

]