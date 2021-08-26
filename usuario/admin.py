from django.contrib import admin
from .models import Usuario, Profissional, Categoria

@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    model = Usuario
    list_display = ['id','is_profissional','first_name','username', 'cidade', 'email','telefone','cidade','rua','imagem','is_superuser', 'is_active', 'is_staff', ]

class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ['id','user_id','slug','profissao', 'descricao', 'imagem',]


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nome',]


admin.site.register(Profissional,ProfissionalAdmin)
admin.site.register(Categoria,CategoriaAdmin)


