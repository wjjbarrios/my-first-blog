from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Publicacion
from .formulario import PostForm
from django.contrib.auth.decorators import login_required


@login_required
def listado(request):
    posts = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {'posts': posts})

def detallepost(request, pk):
     posts = get_object_or_404(Publicacion, pk=pk)
     return render(request, 'blog/detalle.html', {'posts': posts})


def post_publish(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    post.publicar()
    return redirect('detallepost', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    post.delete()
    return redirect('listado')

def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('listado')
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    post = Publicacion.objects.filter(fecha_publicacion__isnull=True).order_by('fecha_creacion')
    return render(request, 'blog/post_draft_list.html', {'post': post})

def post_edit(request, pk):
        post = get_object_or_404(Publicacion, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('listado')
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
