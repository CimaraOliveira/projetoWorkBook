from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    model = Usuario
    list_display = ['id','username', 'status','first_name','last_name','perfil_id','telefone', 'estado', 'email','is_superuser', 'is_active', 'is_staff', ]


