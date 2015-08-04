from django.contrib import admin
from . import models
from django.core.urlresolvers import reverse


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_filter = ['nombre']
    search_fields = ['nombre']


class CiudadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_filter = ['nombre']
    search_fields = ['nombre']


class EmpleoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'ciudad', 'nombre_empresa', 'email_empresa', 'fecha_creado')
    list_filter = ['fecha_creado']
    search_fields = ['titulo', 'ciudad', 'nombre_empresa', 'email_empresa', 'categoria']
    

admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Ciudad, CiudadAdmin)
admin.site.register(models.Empleo, EmpleoAdmin)
