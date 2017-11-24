# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 04:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario_m',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Telefono', models.IntegerField(blank=True, null=True)),
                ('Direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('Correo', models.CharField(max_length=50)),
                ('Avatar', models.FileField(blank=True, null=True, upload_to=b'avatar/%Y/%m/%d')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
