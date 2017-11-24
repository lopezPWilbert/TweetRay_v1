"""
Definition of models.
"""

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Avatar_m(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    Avatar = models.FileField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    fecha_reg=models.DateTimeField(auto_now=True,null=True, blank=True)
class Publicaciones_m(models.Model):
    usuario=models.ForeignKey(User,null=True, blank=True)
    titulo=models.TextField(verbose_name=u"Titulo",max_length=100,null=True, blank=True)
    texto=models.TextField(verbose_name=u"Texto",max_length=500,null=True, blank=True)
    fecha=models.DateTimeField(auto_now=True,null=True, blank=True)
    activo=models.NullBooleanField(verbose_name=u"Activado",null=True, blank=True)
class Comentario_m(models.Model):
    publicacion=models.ForeignKey(Publicaciones_m, null=True, blank=True)
    usuario=models.ForeignKey(User, null=True, blank=True)
    texto=models.TextField(verbose_name=u"Comentario",max_length=500,null=True, blank=True)
    fecha=models.DateTimeField(auto_now=True,null=True, blank=True)
    activo=models.NullBooleanField(verbose_name=u"Activado",null=True, blank=True)
class Respuesta_m(models.Model):
    comentario=models.ForeignKey(Comentario_m, null=True, blank=True)
    usuario=models.ForeignKey(User, null=True, blank=True)
    texto=models.TextField(verbose_name=u"Comentario",max_length=500,null=True, blank=True)
    fecha=models.DateTimeField(auto_now=True,null=True, blank=True)
    activo=models.NullBooleanField(verbose_name=u"Activado",null=True, blank=True)