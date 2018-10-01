from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publicacion


def listado(request):
    posts = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {'posts': posts})

def detallepost(request, pk):
     posts = get_object_or_404(Publicacion, pk=pk)
     return render(request, 'blog/detalle.html', {'posts': posts})
