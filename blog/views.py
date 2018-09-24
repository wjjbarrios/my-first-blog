from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion

def listado(request):
    posts = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {'posts': posts})
