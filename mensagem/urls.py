from django.urls import path,include
from . import views

urlpatterns = [
   path('enviarMensagem/<id>', views.enviarMensagem, name='enviarMensagem'),
   path('responderMensagem/<int:idRemetente>/<int:idDestinatario>', views.responderMensagem, name='responderMensagem'),
   path('detalheMensagem/<int:idRemetente>/<int:idDestinatario>', views.detalheMensagem, name='detalheMensagem'),
   path('listarMensagem/<int:idDestinatario>', views.listarMensagem, name='listarMensagem'),
   path('teste/', views.teste, name='teste'),

]