"""
Definition of models.
"""

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Avatar_m(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    Avatar = models.FileField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)