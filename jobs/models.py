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
    name = models.CharField(max_length=100, verbose_name='Tipo de Trabajo')

    def __unicode__(self):
        return "%s" % (self.name)

    class Meta:
        ordering = ['id']
        verbose_name = 'Tipo de Trabajo'
        verbose_name_plural = 'Tipo de Trabajos'
        permissions = (
            ('show_jobtype', 'Can Details JobType'),
            ('index_jobtype', 'Can List JobType'),
        )


class Job(models.Model):
    jobtype = models.ForeignKey(JobType, verbose_name='Tipo de Trabajo')
    name_client = models.CharField(max_length=100, verbose_name='Nombres del Cliente')
    address = models.CharField(max_length=100, verbose_name=u'Dirección')
    description = models.TextField(verbose_name=u'Descripción')
    mobile_phone = models.CharField(max_length=20, verbose_name=u'Número de Celular')
    state = models.CharField(max_length=10, choices=STATUS_TASK, verbose_name='Estado', default='NUEVO')
    lat = models.CharField(max_length=50, blank=True, verbose_name='Latitud')
    lng = models.CharField(max_length=50, blank=True, verbose_name='Longitud')
    register_at = models.DateTimeField(default=datetime.now, verbose_name='Fecha de registro')

    def __unicode__(self):
        return "%s %s" % (self.name_client, self.jobtype)

    class Meta:
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'

        permissions = (
            ('report_job', 'Can Report Job'),
            ('show_job', 'Can Details Job'),
            ('index_job', 'Can List Job'),
        )


class ProfileJob(models.Model):
    job = models.ForeignKey(Job, verbose_name='Trabajo')
    profile = models.ForeignKey(Profile, verbose_name='Perfil')
    state = models.CharField(max_length=10, choices=STATUS_TASK, verbose_name='Estado', default='NUEVO')
    assign_at = models.DateTimeField(default=datetime.now, verbose_name=u'Fecha de Asignación')

    def __unicode__(self):
        return "%s - %s" % (self.job, self.profile)

    class Meta:
        verbose_name = 'Assignacion'
        verbose_name_plural = 'Asignaciones'
        permissions = (
            ('show_pj', 'Can Details PJ'),
            ('index_pj', 'Can List PJ'),
        )


class JobHistory(models.Model):
    profilejob = models.ForeignKey(ProfileJob, verbose_name='Trabajo asignado')
    profile = models.ForeignKey(Profile, verbose_name='Usuario')

    # STATE ADD PARAMS
    observation = models.TextField(verbose_name=u'Observación')
    register_at = models.DateTimeField(default=datetime.now, verbose_name='Fecha de Registro')

    lat = models.CharField(max_length=50, blank=True, verbose_name='Latitud')
    lng = models.CharField(max_length=50, blank=True, verbose_name='Longitud')

    def __unicode__(self):
        return "%s" % (self.profilejob)

    class Meta:
        verbose_name = 'Historial de Trabajo'
        verbose_name_plural = 'Historiales de trabajos'

        permissions = (
            ('show_jobhistory', 'Can Details Job History'),
            ('index_jobhistory', 'Can List Job Histories'),
        )
