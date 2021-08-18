from django.contrib import admin
from .models import Notificacao

class NotificacaoAdmin(admin.ModelAdmin):
   list_display = ['id',
                   'data_notificacao',
                   'texto',
                   'mensagemRecebida']

admin.site.register(Notificacao,NotificacaoAdmin)