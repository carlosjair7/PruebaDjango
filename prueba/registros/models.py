from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Alumnos(models.Model):#Define la estructura de la tabla
    matricula = models.CharField(max_length=12, verbose_name="Clave")
    nombre = models.TextField()#Texto largo
    carrera = models.TextField()  
    turno = models.CharField(max_length=10)
    imagen = models.ImageField(null=True, upload_to="fotos",verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo de creación
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]
    #el menos indica que se ordenara del mas reciente al viejo

    def __str__(self):
        return self.nombre
    #Indica que se mostrara el nombre como valor en la pantalla

class Comentario(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    alumnno = models.ForeignKey(Alumnos,on_delete=models.CASCADE,verbose_name="Alumno")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    comment = RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created"]

    def __str__(self):
        return self.comment


class ComentarioContacto(models.Model):
 id = models.AutoField(primary_key=True,verbose_name="Clave")
 usuario = models.TextField(verbose_name="Usuario")
 mensaje = models.TextField(verbose_name="Comentario") 
 created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado") 

 class Meta:
  verbose_name = "Comentario Contacto"
  verbose_name_plural = "Comentarios Contactos"
  ordering = ["-created"]

def __str__(self):
 return self.mensaje 
 #Indica que se mostrára el mensaje como valor en la tabla

