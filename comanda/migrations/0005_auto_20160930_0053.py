# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 05:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0002_auto_20160921_1745'),
        ('comanda', '0004_reservacion_guarnicion'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservacion',
            name='plato_fuerte_opcional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_plato_fuerte_opcional', to='configuracion.Alimento'),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='correo',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
