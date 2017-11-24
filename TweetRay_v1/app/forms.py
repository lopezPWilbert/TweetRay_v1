"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
from .models import *
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm

class Usuario_f(UserCreationForm):
    '''
    Telefono = forms.IntegerField()
    Correo = forms.CharField(max_length = 50)
    Direccion = forms.CharField(max_length =100)
    Avatar=forms.ImageField()
    '''
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta():
        model=User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
class Avatar_f(forms.ModelForm):
    class Meta:
        model=Avatar_m
        fields='__all__'