# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-31 20:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20161028_1726'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profilejob',
            options={'ordering': ['-assign_at'], 'permissions': (('report_profilejob', 'Can Details Report Profile Job'), ('show_profilejob', 'Can Details Profije Job'), ('index_profilejob', 'Can List Profile Job')), 'verbose_name': 'Assignacion', 'verbose_name_plural': 'Asignaciones'},
        ),
    ]