# encoding:utf-8
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from users.models import Profile

STATUS_TASK = (('NUEVO', 'NUEVO'),
               ('EN_PROCESO', 'EN PROCESO'),
               ('TERMINADO', 'TERMINADO'),
               ('DETENIDO', 'DETENIDO'),)


class JobType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Tipo de Trabajo')

    def __unicode__(self):
        return "%s" % (self.name)

    def clean(self):
        self.name = self.name.capitalize()

    class Meta:
        ordering = ['name']
        verbose_name = 'Tipo de Trabajo'
        verbose_name_plural = 'Tipo de Trabajos'
        permissions = (
            ('show_jobtype', 'Can Details JobType'),
            ('index_jobtype', 'Can List JobType'),
        )


class Zone(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre de Zona')

    def __unicode__(self):
        return "%s" % (self.name)

    def clean(self):
        self.name = self.name.capitalize()

    class Meta:
        ordering = ['name']
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'
        permissions = (
            ('show_zone', 'Can Details Zone'),
            ('index_zone', 'Can List Zone'),
        )


class Job(models.Model):
    jobtype = models.ForeignKey(JobType, verbose_name='Tipo de Trabajo')
    name_client = models.CharField(max_length=100, verbose_name='Nombre del Cliente')
    address = models.CharField(max_length=100, verbose_name=u'Dirección')
    zone = models.ForeignKey(Zone, default=1, verbose_name='Zona')
    description = models.TextField(verbose_name=u'Descripción')
    mobile_phone = models.CharField(max_length=20, verbose_name=u'Número de Celular')
    state = models.CharField(max_length=10, choices=STATUS_TASK, verbose_name='Estado', default='NUEVO')
    lat = models.CharField(max_length=50, blank=True, verbose_name='Latitud')
    lng = models.CharField(max_length=50, blank=True, verbose_name='Longitud')
    register_at = models.DateTimeField(default=datetime.now, verbose_name='Fecha de registro')

    def __unicode__(self):
        return "%s %s" % (self.name_client, self.jobtype)

    class Meta:
        ordering = ['-register_at']
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'

        permissions = (
            ('report_job', 'Can Report Job'),
            ('show_job', 'Can Details Job'),
            ('index_job', 'Can List Job'),
            ('index_map_job', 'Can List Maps Job'),
        )


class ProfileJob(models.Model):
    job = models.ForeignKey(Job, verbose_name='Trabajo')
    profile = models.ForeignKey(Profile, verbose_name='Asignado a:')
    state = models.CharField(max_length=10, choices=STATUS_TASK, verbose_name='Estado', default='NUEVO')
    assign_at = models.DateTimeField(default=datetime.now, verbose_name=u'Fecha de Asignación')

    def __unicode__(self):
        return "%s - %s" % (self.job, self.profile)

    class Meta:
        ordering = ['-assign_at']
        verbose_name = 'Assignacion'
        verbose_name_plural = 'Asignaciones'
        permissions = (
            ('report_profilejob', 'Can Details Report Profile Job'),
            ('show_profilejob', 'Can Details Profije Job'),
            ('index_profilejob', 'Can List Profile Job'),
        )


class JobHistory(models.Model):
    profilejob = models.ForeignKey(ProfileJob, verbose_name='Trabajo asignado')
    profile = models.ForeignKey(Profile, verbose_name='Usuario')
    state = models.CharField(max_length=10, choices=STATUS_TASK, verbose_name='Estado', default='EN_PROCESO')
    observation = models.TextField(verbose_name=u'Observación')
    register_at = models.DateTimeField(default=datetime.now, verbose_name='Fecha de Registro')

    lat = models.CharField(max_length=50, blank=True, verbose_name='Latitud')
    lng = models.CharField(max_length=50, blank=True, verbose_name='Longitud')

    def __unicode__(self):
        return "%s" % (self.profilejob)

    class Meta:
        ordering = ['register_at']
        verbose_name = 'Historial de Trabajo'
        verbose_name_plural = 'Historiales de trabajos'

        permissions = (
            ('show_jobhistory', 'Can Details Job History'),
            ('index_jobhistory', 'Can List Job Histories'),
        )
