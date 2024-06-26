from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
#Request: para realizar peticiones al servidor
#HTTPRespnose:Para enviar respuestas al protocolo HTTP

def bienvenid (request):
    pagina = """
    <html>
    <head>
    <h1>HOla mundo</h1>
    </head>
    </html>    
    """
    return HttpResponse(pagina)
def index(request):
    plantillas = open (r"C:\Users\moni2\OneDrive\Escritorio\Django\panaderia\panaderia\plantillas\index.html")
    template = Template(plantillas.read())
    plantillas.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)
