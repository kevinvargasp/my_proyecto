# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-01 23:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20161031_1629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-register_at'], 'permissions': (('show_notification', 'Can Details Notificacion'), ('index_notification', 'Can List Notificacion')), 'verbose_name': 'Notificacion', 'verbose_name_plural': 'Notificaciones'},
        ),
    ]
