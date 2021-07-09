from django.contrib import admin
from .models import Usuario, Perfil, Categoria

@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    model = Usuario
    list_display = ['id','username', 'email','is_superuser', 'is_active', 'is_staff', ]

class PerfilAdmin(admin.ModelAdmin):
    list_display = ['id','user_id','first_name','slug','telefone','cidade','rua','profissao',  'descricao', 'imagem',]


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nome','user',]


admin.site.register(Perfil,PerfilAdmin)
admin.site.register(Categoria,CategoriaAdmin)


