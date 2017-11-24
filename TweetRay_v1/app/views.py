"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from app.models import *
from django.core.urlresolvers import reverse_lazy,reverse
from django.views.generic import FormView
from django.views.generic import CreateView
from app.forms import *
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def MiMuro(request):
    mis_publicaciones=Publicaciones_m.objects.filter(usuario=request.user.id)
    return render(request, 'app/mimuro.html',{'mis_publicaciones':mis_publicaciones})
def Muro(request):
    avatar=Avatar_m.objects.filter(usuario=request.user.id)
    avatar=avatar[0].Avatar.url
    publicados=Publicaciones_m.objects.filter(activo=True).order_by('fecha')
    comentarios=Comentario_m.objects.filter(activo=True).order_by('fecha')
    respuesta=Respuesta_m.objects.filter(activo=True).order_by('fecha')

    publicacion_form=Publicacion_f(request.POST or None)
    comentario_form=Comentario_f(request.POST or None)
    respuesta_form=Respuesta_f(request.POST or None)
    if request.method == 'POST':
        if 'publicar' in request.POST:
            if publicacion_form.is_valid():
                Publicaciones_m.objects.create(texto=request.POST['texto'],titulo=request.POST['titulo'], usuario_id=request.user.id, activo=True)
        if 'comentar' in request.POST:
            if comentario_form.is_valid():
                #Comentario_m.objects.create()
                comentario_form.save()
        if 'responder' in request.POST:
            if respuesta_form.is_valid():
                #Comentario_m.objects.create()
                respuesta_form.save()
        return HttpResponseRedirect(reverse("muro"))
    return render(request, 'app/muro.html', {'publicacion_form':publicacion_form,'comentario_form':comentario_form,'respuesta_form':respuesta_form, 'publicados':publicados,'comentarios':comentarios,'respuesta':respuesta,'avatar':avatar})
def SignUp(request):
    
    if request.method == 'POST':
        form = Usuario_f(request.POST)
        form2=Avatar_f(request.POST or None, request.FILES or None)
        if form.is_valid():
            form_resultado=form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if  request.FILES['Avatar']:
                id_form=form_resultado.id

                Avatar_m.objects.create(Avatar=request.FILES['Avatar'], usuario_id=id_form)
            return redirect('muro')
    else:
        form = Usuario_f()
        form2=Avatar_f()
    return render(request, 'app/signUp.html', {'form': form,'form2':form2})
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'BIenvenido',
            'year':datetime.now().year,
        }
    )
