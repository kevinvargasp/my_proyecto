# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-28 21:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20161028_1527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-register_at'], 'permissions': (('report_job', 'Can Report Job'), ('show_job', 'Can Details Job'), ('index_job', 'Can List Job'), ('index_map_job', 'Can List Maps Job')), 'verbose_name': 'Trabajo', 'verbose_name_plural': 'Trabajos'},
        ),
        migrations.AlterModelOptions(
            name='jobhistory',
            options={'ordering': ['register_at'], 'permissions': (('show_jobhistory', 'Can Details Job History'), ('index_jobhistory', 'Can List Job Histories')), 'verbose_name': 'Historial de Trabajo', 'verbose_name_plural': 'Historiales de trabajos'},
        ),
        migrations.AlterModelOptions(
            name='profilejob',
            options={'permissions': (('report_profilejob', 'Can Details Report Profile Job'), ('show_profilejob', 'Can Details Profije Job'), ('index_profilejob', 'Can List Profile Job')), 'verbose_name': 'Assignacion', 'verbose_name_plural': 'Asignaciones'},
        ),
    ]
