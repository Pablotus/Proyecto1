from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def saludo(request):

    return HttpResponse("Hola Django - Coder")


def mostrar_html(request):

    return HttpResponse("<button>este es mi boton</button><br><h1>Hola</h1>")

def retornar_parametro(request):
    mensaje = f"La fecha de hoy es {datetime.now()}"
    return HttpResponse(mensaje)


def mi_nombre(request, nombre):
    return HttpResponse(f"Hola, bienvenido <b>{nombre}</b>")

def show_html(request):
    return render(request, "template1.html")

def show_html2(request,cursada):
    contexto = {
        "cursada": cursada,
        "entidad": "Coder",
        "fecha": datetime.now(),
        "lista": [1,2,3,4,5],
        "diccionario": {
            "nombre": "Luis",
            "apellido": "Franco"
        }
    }
    return render(request, "template2.html", context=contexto)


