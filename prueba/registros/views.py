from django.shortcuts import render
from .models import Alumnos, ComentarioContacto
from .forms import ComentarioContactoForm
# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()
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