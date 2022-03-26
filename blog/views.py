from webbrowser import get
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import RegistroPost

def viewPrincipal(request):
    posts = Post.objects.all()
    return render(request,"principal.html",{"posts":posts})

def viewDetail(request, id):
    posts = Post.objects.all()
    searchedPost  = get_object_or_404(Post, pk=id)
    return render(request, "detalhe.html", {"searchedPost":searchedPost, "id":id})

def viewDelete(request, id):
    posts = Post.objects.all()

    searchedPost  = get_object_or_404(Post, pk=id)
    searchedPost.delete()

    return redirect('principal')

def viewCreate(request):
    formulario = RegistroPost(request.POST, request.FILES,)
    if formulario.is_valid():
            formulario.save()
            return redirect('detalhe', id=formulario.instance.id)

    return render(request, "criar.html", {"formulario":formulario})

def viewAlterar(request, id):
    postagemAlterada = get_object_or_404(Post, pk=id)
    formulario = RegistroPost(request.POST or None, instance=postagemAlterada)
    if formulario.is_valid():
        formulario.save()
        return redirect('detalhe', id=formulario.instance.id)
    
    return render(request, "alterar.html", {"formulario":formulario})
