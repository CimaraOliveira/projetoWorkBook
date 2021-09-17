from django.contrib import admin
from avaliacao.models import Avaliacao

class AvaliacaoAdmin(admin.ModelAdmin):
   list_display = ['id','descricao','nota', 'profissional_id', 'cliente_id', 'profissional', 'cliente',
                   'total_pessoas','media','soma']

admin.site.register(Avaliacao,AvaliacaoAdmin)
