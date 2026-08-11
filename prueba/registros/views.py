import datetime

from django.shortcuts import render
from .models import Alumnos, ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Alumnos, ComentarioContacto, Archivos
from .forms import ComentarioContactoForm, FormArchivos
from django.contrib import messages
    
def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {"alumnos": alumnos})
#Iniciamos el lugar en donde se renderiza el resultado de esta vista 

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():#si los datos recibidos son correctos
            form.save()#insertamos los datos
            comentarios = ComentarioContacto.objects.all()
            return render(request, "registros/consultaContacto.html", {"comentarios": comentarios})
        #si algo sale mal se reenvian al formulario los datos ingresados
        return render(request, 'registros/contacto.html', {'form': form})
    
    form = ComentarioContactoForm()
    return render(request, 'registros/contacto.html', {'form': form})
    
def contacto(request):
    return render(request,'registros/contacto.html')
#Funcion de visalizacion de Contacto

def consultaContacto(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/consultaContacto.html", {"comentarios": comentarios})
#Funcion de consulta de comentarios registrados

def eliminarComentarioContacto(request,id,confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request,"registros/consultaContacto.html",{"comentarios": comentarios})
    return render(request,confirmacion,{'object':comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    #Referenciamos que el elemento del formulario pertenece al comentario ya existente
    if form.is_valid():
        form.save()#si el registro ya existe se modifica
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})
    #si el formulario no es valido nos regresamos al formulario para verificar los datos
    return render(request, 'registros/formEditarComentario.html', {'comentario': comentario})


def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    #get permite establecer un condicionante a la consulta y recupera el objeto del modelo que cumple
    #la condicion (registro de la tabla de ComentariosContacto.html)
    #get se emplea cuando se sabe que solo hay un objeto que coincide con su consulta
    return render(request,'registros/formEditarComentario.html',
    {'comentario':comentario})



def consultas(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar1(request):
    alumnos = Alumnos.objects.filter(carrera='TI')
    return render(request, "registros/consultas.html", {"alumnos": alumnos})


def consultar2(request):
    alumnos = Alumnos.objects.filter(carrera='TI').filter(turno='Matutino')
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar3(request):
    alumnos = Alumnos.objects.all().only('matricula','nombre','carrera','turno','imagen')
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar4(request):
    # __startswith: el campo empieza con cierto texto (LIKE 'texto%')
     # __endswith: el campo termina con cierto texto (LIKE '%texto')
    alumnos = Alumnos.objects.filter(turno__startswith="Vesp")
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar5(request):
    
    alumnos = Alumnos.objects.filter(nombre__icontains="Jair").filter(matricula__endswith="TI")
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar6(request):
    alumnos = Alumnos.objects.filter(nombre__in=["Juan","Ana"])
    return render(request, "registros/consultas.html",{"alumnos": alumnos})

def consultar7(request):
    fechaInicio = datetime.date(2026,6,20)
    fechaFin = datetime.date(2026,8,4)
    alumnos = Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html",{"alumnos": alumnos})

def consultar8(request):
    #Consultando entre modelos
    alumnos = Alumnos.objects.filter(comentario__comment__contains="No inscrito")
    return render(request, "registros/consultas.html",{"alumnos": alumnos})

def consultasSQL(request):
    alumnos = Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request, "registros/consultas.html",{"alumnos": alumnos})

#CONSULTAS COMENTARIOS CONTACTO - ORM

def consultar9(request):
    # Comentarios creados entre el 20 de junio y el 4 de agosto
    fechaInicio = datetime.date(2026, 6, 20)
    fechaFin = datetime.date(2026, 8, 4)
    comentarios = ComentarioContacto.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/formConsultaContacto.html", {"comentarios": comentarios})


def consultar10(request):
    # Consulta que busca una expresión dentro del mensaje
    comentarios = ComentarioContacto.objects.filter(mensaje__icontains="gracias")
    return render(request, "registros/formConsultaContacto.html", {"comentarios": comentarios})


def consultar11(request):
    # Consulta que pertenezcan a un usuario
    comentarios = ComentarioContacto.objects.filter(usuario="Carlos")
    return render(request, "registros/formConsultaContacto.html", {"comentarios": comentarios})


def consultar12(request):
    # Expresión: usuario cuyo nombre empieza con cierta letra
    comentarios = ComentarioContacto.objects.filter(usuario__startswith="C")
    return render(request, "registros/formConsultaContacto.html", {"comentarios": comentarios})


def consultar13(request):
    # Expresión: mensaje que termina con cierto texto
    comentarios = ComentarioContacto.objects.filter(mensaje__endswith="o")
    return render(request, "registros/formConsultaContacto.html", {"comentarios": comentarios})



#CONSULTAS COMENTARIOS CONTACTO - SQL

def consultar9SQL(request):
    comentarios = ComentarioContacto.objects.raw('SELECT id, usuario, mensaje, created FROM registros_comentariocontacto ' \
    'WHERE created BETWEEN "2026-06-20" AND "2026-08-04"')
    return render(request, "registros/formConsultaContacto.html", {"comentarios": comentarios})


def consultar10SQL(request):
    comentarios = ComentarioContacto.objects.raw('SELECT id, usuario, mensaje, created FROM registros_comentariocontacto WHERE mensaje LIKE "%gracias%"')
    return render(request, "registros/formConsultaContacto.html", {"comentarios": comentarios})


def consultar11SQL(request):
    comentarios = ComentarioContacto.objects.raw('SELECT id, usuario, mensaje, created ' \
    'FROM registros_comentariocontacto WHERE usuario = "Carlos"')
    return render(request, "registros/formConsultaContacto.html", {"comentarios": comentarios})


def consultar12SQL(request):
    comentarios = ComentarioContacto.objects.raw('SELECT id, usuario, mensaje, created ' \
    'FROM registros_comentariocontacto WHERE usuario LIKE "C%"')
    return render(request, "registros/formConsultaContacto.html", {"comentarios": comentarios})


def consultar13SQL(request):
    comentarios = ComentarioContacto.objects.raw('SELECT id, usuario, mensaje, created FROM registros_comentariocontacto WHERE mensaje LIKE "%to%"')
    return render(request, "registros/formConsultaContacto.html", {"comentarios": comentarios})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo=request.POST['titulo']
            descripcion=request.POST['descripcion']
            archivo=request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request, "registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")

    else:
        return render(request, "registros/archivos.html",{'archivo': Archivos})