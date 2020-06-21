from  django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola")

def Herencias (request):
    return("empezamos con herencias")