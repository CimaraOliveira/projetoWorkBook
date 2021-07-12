from django.contrib import admin
from .models import Mensagem

class MensagemAdmin(admin.ModelAdmin):
    list_display = ['id','texto','destinatario','remetente',]

admin.site.register(Mensagem,MensagemAdmin)

