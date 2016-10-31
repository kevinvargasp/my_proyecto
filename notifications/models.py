from __future__ import unicode_literals

from django.db import models
from datetime import datetime
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

    register_at = models.DateTimeField(default=datetime.now, verbose_name='Fecha de envio')
    read_at = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de lectura')


    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-register_at']
        verbose_name = 'Notificacion'
        verbose_name_plural = 'Notificaciones'

        permissions = (
            ('show_notification', 'Can Details Notificacion'),
            ('index_notification', 'Can List Notificacion'),
        )
