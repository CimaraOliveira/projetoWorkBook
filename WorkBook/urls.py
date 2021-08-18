from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from notificacoes.notificacao_service import NotificacaoViewSet
from usuario.usuario_service import UsuarioViewSet, ProfissionalViewSet
from mensagem.mensagem_service import MensagemViewSet
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token


router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet, basename="Usuários")
router.register(r'perfil', ProfissionalViewSet)
router.register(r'mensagem', MensagemViewSet)
router.register(r'notificacao', NotificacaoViewSet)

#pip freeze > requirements.txt
urlpatterns = [

    path('', include('usuario.urls')),
    path('admin/', admin.site.urls),
    path('mensagem/', include('mensagem.urls')),
    path ('avaliacao/', include('avaliacao.urls')),
    path ('notificacoes/', include('notificacoes.urls')),
    path ('teste/', include('teste.urls')),
    path('api/', include(router.urls)),
    path('api-token/', obtain_jwt_token),
    path('api-auth/', include('rest_framework.urls')),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)