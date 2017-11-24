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
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from django.views.generic import CreateView
from app.forms import *
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def SingUp2(request):
    if request.method=='POST':
        formulario=UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario=UserCreationForm()
    return render(request,'app/singUp.html',{'formulario':formulario})

class SingUp3(FormView):
    template_name = 'app/singup.html'
    form_class=Usuario_f
    succes_url=reverse_lazy('login')

    def form_valid(self, form):
        user=form.save()
        p=Usuario_m()
        p.usuario=user
        p.Telefono=form.cleaned_data['Telefono']
        p.Correo=form.cleaned_data['Correo']
        p.Direccion=form.cleaned_data['Direccion']
        #p.Avatar=form.cleaned_data['Avatar']
        p.save()

        return super(SingUp, self).form_valid(form)
def SignUp4(request):
    form=Usuario_f(request.POST or None, request.FILES or None)
    if(request.method=='POST' and form.is_valid()):
        form.save()
    return render(request, 'app/signup.html', {'form':form})
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
            if form2.is_valid() and request.FILES['Avatar']:
                id_form=form_resultado.id

                Avatar_m.objects.create(Avatar=request.FILES['Avatar'], usuario_id=id_form)
            return redirect('home')
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
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
