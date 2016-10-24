from django import template
from datetime import datetime

from jobs.models import ProfileJob
from users.models import ROLES_PROFILE, MARITAL_STATUS, GENDER

register = template.Library()


@register.simple_tag
def get_verbose_field_name(instance, field_name):
    return instance._meta.get_field(field_name).verbose_name.title()


@register.simple_tag
def get_field_name(obj, field_name):
    return obj._meta.get_field(field_name).verbose_name.title()


@register.simple_tag
def get_state_jobsite(status):
    return {
        'N': 'NUEVO',
        'P': 'EN PROCESO',
        'T': 'TERMINADO',
        'D': 'DETENIDO',
    }[status]


@register.simple_tag
def get_state_profile(status):
    return {
        'CLI': 'CLIENTE',
        'ADM': 'ADMINISTRADOR',
        'GER': 'GERENTE',
        'CAP': 'CAPATAZ',
        'SUP': 'SUPERVISOR',
        'STR': 'SECRETARIA',
    }[status]


@register.simple_tag
def get_gender_profile(gender):
    for status in GENDER:
        if status[0] == gender:
            return status[1]
    return None


@register.simple_tag
def get_marital_profile(marital):
    for status in MARITAL_STATUS:
        if status[0] == marital:
            return status[1]
    return None


@register.simple_tag
def get_role_profile(role):
    print "-%s-" % role
    for rol in ROLES_PROFILE:
        if rol[0] == role:
            return rol[1]
    return None


@register.simple_tag
def get_category(status):
    return {
        'MOV': 'MOVILIDAD',
        'EDT': 'EQUIPO DE TRABAJO',
        'REP': 'REPARADO',
        'NOU': 'NO USABLE',
    }[status]


@register.filter()
def to_int(value):
    return int(value)


@register.filter
def index(List, i):
    count = len(List)
    if (int(i) > count - 1):
        return "No registrado"
    return List[int(i)]


@register.simple_tag
def is_assigned(job_id):
    html_icon = '<span class="label label-danger label-rounded">SIN ASIGNAR</span>'
    if ProfileJob.objects.filter(job_id=int(job_id)).exists():
        html_icon = '<span class="label label-megna label-rounded">ASIGNADO</span>'

    return html_icon
