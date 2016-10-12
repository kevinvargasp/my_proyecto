# encoding:utf-8
from django.utils import timezone
from users.models import Profile
from django.shortcuts import render
from users.form import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import datetime

# Import api for users
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response


@permission_required('users.index_profile', login_url='/log_in')
def profiles_index(request):
    profiles_all = Profile.objects.all()
    return render(request, 'profiles/index.html', {
        'profiles': profiles_all,
        'profile_obj': Profile,
    })


@permission_required('users.add_profile', login_url='/log_in')
def profiles_new(request):
    if request.method == 'POST':
        formUser = UserCreationForm(request.POST)
        form = ProfileForm(request.POST)
        if formUser.is_valid() and form.is_valid():
            add_group_permissions()

            user = formUser.save()
            profile = form.save(commit=False)
            profile.user = user
            profile.save()

            type_rol = request.POST['rol']

            if type_rol == 'SUP':
                g = Group.objects.get(name='SUPERVISOR')
                g.user_set.add(user.id)
            elif type_rol == 'TEC':
                g = Group.objects.get(name='TECNICO')
                g.user_set.add(user.id)

            message = 'Registrado correctamente!'
            messages.add_message(request, messages.SUCCESS, message)
            return HttpResponseRedirect(reverse(profiles_index))
        else:
            message = 'Existen errores por favor verifica!.'
            messages.add_message(request, messages.ERROR, message)
    else:
        formUser = UserCreationForm()
        form = ProfileForm()
    return render(request, 'profiles/new.html', {
        'form': form,
        'form_second': formUser,
    })

def check_permision(id):
    add_group_permissions()

    profile = Profile.objects.get(id=id)
    type_rol = profile.rol

    if type_rol == 'SUP':
        g = Group.objects.get(name='SUPERVISOR')
        g.user_set.add(profile.user_id)
    elif type_rol == 'TEC':
        g = Group.objects.get(name='TECNICO')
        g.user_set.add(profile.user_id)


@permission_required('users.change_profile', login_url='/log_in')
def profiles_edit(request, id):
    profile = Profile.objects.get(id=id)
    check_permision(id)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            save_profile = profile_form.save()

            message = "actualizado Correctamente"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse('profiles-show', kwargs={'id': profile.id}))
    else:
        profile_form = ProfileForm(instance=profile)
    return render(request, 'profiles/edit.html', {
        'form': profile_form
    })


#@permission_required('users.show_profile', login_url='/log_in')
def profiles_show(request, id):
    profile = Profile.objects.get(id=id)

    return render(request, 'profiles/show.html', {
        'profile': profile,
        'profile_obj': Profile,
        'user_obj': User,
    })


def profiles_user_show(request, u_id):
    if not Profile.objects.filter(user_id=u_id).exists():
        message = "No existe perfil para este usuario"
        messages.add_message(request, messages.INFO, message)
        return HttpResponseRedirect(reverse(profiles_index))
    profile = Profile.objects.get(user_id=u_id)

    return render(request, 'profiles/show.html', {
        'profile': profile,
        'profile_obj': Profile,
        'user_obj': User,
    })


@permission_required('users.delete_profile', login_url='/log_in')
def profiles_delete(request, id):
    profile = Profile.objects.get(id=id)
    profile.delete()
    is_exist = Profile.objects.filter(id=id).exists()

    if is_exist:
        message = 'No se pudo eliminar'
        messages.add_message(request, messages.ERROR, message)
    else:
        message = 'Eliminado!'
        messages.add_message(request, messages.SUCCESS, message)

    return HttpResponseRedirect(reverse(profiles_index))


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            access = authenticate(username=username, password=password)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    if access.is_superuser:
                        return HttpResponseRedirect('/admin/')
                    else:
                        return HttpResponseRedirect('/')
                else:
                    message = 'El Usuario no esta Activo'
                    messages.add_message(request, messages.ERROR, message)
            else:
                message = 'El nombre de usuario o contraseña no coinciden'
                messages.add_message(request, messages.ERROR, message)
    else:
        form = AuthenticationForm()

    return render(request, 'login/session_new.html', {
        'form': form
    })


@login_required(login_url='/log_in')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


from django.contrib.auth.models import Group, Permission
import logging

logger = logging.getLogger(__name__)


def add_group_permissions():
    # ENCARGADO_RECURSOS_PROPIOS
    group, created = Group.objects.get_or_create(name='SUPERVISOR')

    if created:
        group.permissions.add(
            Permission.objects.get(codename="add_job"),
            Permission.objects.get(codename="change_job"),
            Permission.objects.get(codename="show_job"),
            Permission.objects.get(codename="index_job"),
            Permission.objects.get(codename="delete_job"),

            Permission.objects.get(codename="add_jobtype"),
            Permission.objects.get(codename="change_jobtype"),
            Permission.objects.get(codename="show_jobtype"),
            Permission.objects.get(codename="index_jobtype"),
            Permission.objects.get(codename="delete_jobtype"),

            Permission.objects.get(codename="add_zone"),
            Permission.objects.get(codename="change_zone"),
            Permission.objects.get(codename="show_zone"),
            Permission.objects.get(codename="index_zone"),
            Permission.objects.get(codename="delete_zone"),

            Permission.objects.get(codename="add_profilejob"),
            Permission.objects.get(codename="change_profilejob"),
            Permission.objects.get(codename="show_profilejob"),
            Permission.objects.get(codename="index_profilejob"),
            Permission.objects.get(codename="delete_profilejob"),

            Permission.objects.get(codename="add_jobhistory"),
            Permission.objects.get(codename="change_jobhistory"),
            Permission.objects.get(codename="show_jobhistory"),
            Permission.objects.get(codename="index_jobhistory"),
            Permission.objects.get(codename="delete_jobhistory"),

            Permission.objects.get(codename="add_profile"),
            Permission.objects.get(codename="change_profile"),
            Permission.objects.get(codename="show_profile"),
            Permission.objects.get(codename="index_profile"),
            Permission.objects.get(codename="delete_profile"),
        )

        logger.info('SUPERVISOR Group created')

    # ENCARGADO_SISTEMAS_DAF
    group, created = Group.objects.get_or_create(name='TECNICO')
    if created:
        group.permissions.add(
            Permission.objects.get(codename="change_job"),
            Permission.objects.get(codename="show_job"),
            Permission.objects.get(codename="index_job"),

            Permission.objects.get(codename="change_profile"),
            Permission.objects.get(codename="show_profile"),
        )
        logger.info('SUPERVISOR Group created')
