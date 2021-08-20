from django.contrib import admin
from .models import TesteAvaliacao
from django.contrib.admin.filters import SimpleListFilter


class CustomFilter(SimpleListFilter):
    parameter_name = 'user_id'

    def lookups(self, request, model_admin):
        return (
            ("value", "user_id")
        )
    def queryset(self, request, queryset):
        return queryset


class TesteAvaliacaoAdmin(admin.ModelAdmin):
    list_display = [
        'id','nota','cliente','cliente_id','profissional_id','profissional', 'data_avaliacao',]

admin.site.register(TesteAvaliacao,TesteAvaliacaoAdmin)


