from django.contrib import admin
from .models import Alumnos, Comentario

from .models import ComentarioContacto


class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')


admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentario(admin.ModelAdmin):
    list_display = ('id','comment','alumnno')
    search_fields = ('comment',)
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    #autocomplete_fields = ('alumnno',)
    #list_editable = ('comment',)
    list_per_page = 5
    #list_filter = ('CREATED',)
    #list_display_links = ('alumno',)
admin.site.register(Comentario, AdministrarComentario)



class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)