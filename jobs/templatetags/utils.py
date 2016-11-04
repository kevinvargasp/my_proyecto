# encoding:utf-8
from django import template
from datetime import datetime
from django.apps import apps
from jobs.models import ProfileJob, Job, JobType, Zone
from notifications.models import Notification
from users.models import ROLES_PROFILE, MARITAL_STATUS, GENDER, Profile

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



@register.simple_tag
def get_total_job_types():
    return JobType.objects.all().count()


@register.simple_tag
def get_total_zones():
    return Zone.objects.all().count()

@register.simple_tag
def get_total_jobs():
    return Job.objects.all().count()


@register.simple_tag
def get_total_profiles():
    return Profile.objects.all().count()


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
def get_label_state(state):
    return {
        'NUEVO': "<span class='label label-default label-rounded'>Nuevo</span>",
        'EN_PROCESO': "<span class='label label-success label-rounded'>En proceso</span>",
        'TERMINADO': "<span class='label label-info label-rounded'>Terminado</span>",
        'DETENIDO': "<span class='label label-warning label-rounded'>Detenido</span>",
    }[state]


@register.simple_tag
def get_label_state_assign(state):
    state_assign = "<i class='fa fa-circle m-r-5' style='color: #00bfc7;' data-tooltip='tooltip' title='Asignado'></i>"
    if not state:
        state_assign = "<i class='fa fa-circle m-r-5' style='color: #fa3e18;' data-tooltip='tooltip' title='No Asignado'></i>"
    return state_assign


@register.assignment_tag
def is_assigned_plain(job_id):
    return ProfileJob.objects.filter(job_id=int(job_id)).exists()


@register.assignment_tag
def get_profiles_assigment(job_id):
    return ProfileJob.objects.filter(job_id=int(job_id))


@register.assignment_tag
def is_use_zone(zone_id):
    return Job.objects.filter(zone_id=int(zone_id)).exists()


@register.assignment_tag
def is_use_job_type(type_job_id):
    return Job.objects.filter(jobtype_id=int(type_job_id)).exists()

@register.assignment_tag
def get_obj_from_notification(notification):
    obj = apps.get_model('jobs', notification.obj)
    return obj.objects.get(pk=notification.obj_id)

@register.assignment_tag
def get_notifications(requestt):

    if requestt.user.is_superuser or Profile.objects.get(user_id=requestt.user.id).rol == 'SUP':
        notifications = Notification.objects.all()[:10]
    else:
        notifications = Notification.objects.filter(profile_id=Profile.objects.get(user_id=requestt.user.id))[:10]

    return notifications
