from django.contrib import admin
from .models import TesteAvaliacao
class TesteAvaliacaoAdmin(admin.ModelAdmin):
    list_display = [
        'id','nota','cliente','cliente_id','profissional_id','profissional', 'data_avaliacao',]

admin.site.register(TesteAvaliacao,TesteAvaliacaoAdmin)


