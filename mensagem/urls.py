from django.urls import path,include
from . import views
from .mensagem_service import MensagemViewSet

urlpatterns = [
   path('enviarMensagem/<id>', views.enviarMensagem, name='enviarMensagem'),
   path('responderMensagem/<int:idRemetente>/<int:idDestinatario>', views.responderMensagem, name='responderMensagem'),
   path('detalheMensagem/<int:idRemetente>/<int:idDestinatario>', views.detalheMensagem, name='detalheMensagem'),
   path('listarMensagem/<int:idDestinatario>', views.listarMensagem, name='listarMensagem'),
   path('teste-chat/', views.test_chat, name='teste_chat'),


]