from django.contrib import admin
from .models import Alumnos, Comentario

from .models import ComentarioContacto

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno', 'created')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')

    def get_readonly_fields(self, request, obj=None):
        # Si el usuario pertenece al grupo de permisos "Usuarios"
        if request.user.groups.filter(name="Usuarios").exists():
            # Bloquea estos campos
            return (
                'matricula',
                'carrera',
                'turno'
            )
        # Si el usuario pertenece al grupo "Editores"
        elif request.user.groups.filter(name="Editores").exists():
            
            return (
                'matricula',
                'turno',
                'created',
                'updated'
            )
        else:
            # Cualquier otro usuario que no pertenezca al grupo "Usuarios"
            # solo tendrá bloqueados estos campos
            return (
                'created',
                'updated'
            )



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
    list_display = ('id', 'mensaje', 'created')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)