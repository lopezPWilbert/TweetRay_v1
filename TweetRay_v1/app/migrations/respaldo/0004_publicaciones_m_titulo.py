# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171123_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicaciones_m',
            name='titulo',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Titulo'),
        ),
    ]