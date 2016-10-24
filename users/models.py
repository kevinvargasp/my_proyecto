# encoding:utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

GENDER = (('F', 'FEMENINO'), ('M', 'MASCULINO'))
MARITAL_STATUS = (('SO', 'SOLTERO(A)'),
                  ('CA', 'CASADO(A)'),
                  ('VI', 'VIUDO(A)'),
                  ('DI', 'DIVORCIADO(A)'),
                  ('CO', 'CONCUBINO(A)'),
                  ('SE', 'SEPARADO(A)'),)

ROLES_PROFILE = (('SUP', 'SUPERVISOR'),
                 ('TEC', 'TECNICO'),)


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True)
    ci = models.CharField(max_length=12, unique=True, verbose_name='CI')
    first_name = models.CharField(max_length=100, verbose_name='Nombres')
    middle_name = models.CharField(max_length=100, verbose_name='Apellido paterno')
    last_name = models.CharField(max_length=100, verbose_name='Apellido materno')
    gender = models.CharField(max_length=2, choices=GENDER, verbose_name=u'Género')
    date_of_birth = models.DateField(verbose_name='Fecha de nacimiento')
    marital_status = models.CharField(max_length=2, choices=MARITAL_STATUS, verbose_name='Estado Civil')
    home_address = models.CharField(max_length=100, verbose_name=u'Dirección')
    mobile_phone = models.CharField(max_length=25, blank=True, verbose_name='Nro. de Celular')
    rol = models.CharField(max_length=3, choices=ROLES_PROFILE, default='TEC', verbose_name='Rol')
    imei_code = models.CharField(max_length=25, unique=True, verbose_name='Imei Celular')
    register_at = models.DateTimeField(default=datetime.now, verbose_name='Fecha de registro')


    def __unicode__(self):
        return "%s %s" % (self.first_name, self.middle_name)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

        permissions = (
            ('show_profile', 'Can Details Profile'),
            ('index_profile', 'Can List Profile'),
        )