from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Contrato, ArchivoUsuario

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Datos adicionales', {
            'fields': ('tipo_documento','numero_documento','fecha_inicio_constancia',
                       'fecha_fin_constancia','tipo_constancia','rol')
        }),
    )
    list_display = ('username','first_name','last_name','numero_documento','rol','is_active','is_staff')
    search_fields = ('username','first_name','last_name','numero_documento')
    list_filter = ('rol','is_active','is_staff')

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('serial_contrato','usuario','fecha_inicio','fecha_fin')
    search_fields = ('serial_contrato','usuario__first_name','usuario__last_name','usuario__numero_documento')
    list_filter = ('fecha_inicio','fecha_fin')

@admin.register(ArchivoUsuario)
class ArchivoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario','archivo','fecha_subida')
    search_fields = ('usuario__first_name','usuario__last_name','usuario__numero_documento')
    list_filter = ('fecha_subida',)