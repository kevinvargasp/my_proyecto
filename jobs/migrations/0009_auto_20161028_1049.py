# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-28 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20161021_1830'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobtype',
            options={'ordering': ['name'], 'permissions': (('show_jobtype', 'Can Details JobType'), ('index_jobtype', 'Can List JobType')), 'verbose_name': 'Tipo de Trabajo', 'verbose_name_plural': 'Tipo de Trabajos'},
        ),
        migrations.AlterModelOptions(
            name='zone',
            options={'ordering': ['name'], 'permissions': (('show_zone', 'Can Details Zone'), ('index_zone', 'Can List Zone')), 'verbose_name': 'Zona', 'verbose_name_plural': 'Zonas'},
        ),
        migrations.AddField(
            model_name='jobhistory',
            name='state',
            field=models.CharField(choices=[(b'NUEVO', b'NUEVO'), (b'EN_PROCESO', b'EN PROCESO'), (b'TERMINADO', b'TERMINADO'), (b'DETENIDO', b'DETENIDO')], default=b'EN_PROCESO', max_length=10, verbose_name=b'Estado'),
        ),
        migrations.AlterField(
            model_name='job',
            name='name_client',
            field=models.CharField(max_length=100, verbose_name=b'Nombre del Cliente'),
        ),
        migrations.AlterField(
            model_name='profilejob',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile', verbose_name=b'Asignado a:'),
        ),
    ]
