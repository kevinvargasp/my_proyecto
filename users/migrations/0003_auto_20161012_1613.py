# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160928_1909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('show_profile', 'Can Details Profile'), ('index_profile', 'Can List Profile')), 'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfiles'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='imei_code',
            field=models.CharField(max_length=25, unique=True, verbose_name='Imei Celular'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='marital_status',
            field=models.CharField(choices=[('SO', 'SOLTERO(A)'), ('CA', 'CASADO(A)'), ('VI', 'VIUDO(A)'), ('DI', 'DIVORCIADO(A)'), ('CO', 'CONCUBINO(A)'), ('SE', 'SEPARADO(A)')], max_length=2, verbose_name='Estado Civil'),
        ),
    ]