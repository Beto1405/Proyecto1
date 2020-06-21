from  django.http import HttpResponse
from django.template import loader

def saludo(request):
    return HttpResponse("Hola")

def Herencias (request):
    return("empezamos con herencias")