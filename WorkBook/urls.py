from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from usuario.usuario_service import UsuarioViewSet, ProfissionalViewSet
from mensagem.mensagem_service import MensagemViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
router.register(r'perfil', ProfissionalViewSet)
router.register(r'mensagem', MensagemViewSet)


urlpatterns = [

    path('', include('usuario.urls')),
    path('admin/', admin.site.urls),
    path('mensagem/', include('mensagem.urls')),
    path ('avaliacao/', include('avaliacao.urls')),
    path('api/', include(router.urls)),
    #path('api/', include('rest_framework.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)