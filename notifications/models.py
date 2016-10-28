from __future__ import unicode_literals

from django.db import models

# Create your models here.
from users.models import Profile

TYPE_NOTIFICATION = (('MES', 'MENSAJE'),
                     ('LOC', 'UBICACION'),)

LEVEL_NOTIFICATION = (('LOW', 'BAJA'),
                      ('MED', 'MEDIO'),
                      ('HIG', 'ALTO'),)


class Notification(models.Model):
    profile = models.ForeignKey(Profile, null=True, blank=True, verbose_name='Emisor')

    level = models.CharField(max_length=3, choices=LEVEL_NOTIFICATION, verbose_name='Nivel de Alerta')
    type = models.CharField(max_length=3, choices=TYPE_NOTIFICATION, verbose_name='Tipo de Alerta')

    title = models.CharField(max_length=100, blank=True, verbose_name='Titulo')
    content = models.CharField(max_length=250, blank=True, verbose_name='Contenido')

    obj = models.CharField(max_length=25)
    obj_id = models.CharField(max_length=5)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Notificacion'
        verbose_name_plural = 'Notificaciones'

        permissions = (
            ('show_notificacion', 'Can Details Notificacion'),
            ('index_notificacion', 'Can List Notificacion'),
        )
