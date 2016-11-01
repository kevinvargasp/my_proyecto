from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import datetime

# Import api for users
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
from jobs.api import JobSerializer
from jobs.models import JobType, Job, ProfileJob, JobHistory, Zone
from jobs.form import JobTypeForm, JobForm, ProfileJobForm, JobHistoryForm, ZoneForm
from notifications.models import Notification
from users.models import Profile

from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer


@permission_required('jobs.index_jobtype', login_url='/log_in')
def jobtypes_index(request):
    jobtypes_all = JobType.objects.all()
    return render(request, 'jobtypes/index.html', {
        'jobtype_instance': JobType,
        'jobtypes': jobtypes_all,
    })


@permission_required('jobs.add_jobtype', login_url='/log_in')
def jobtypes_new(request):
    if request.method == 'POST':
        form = JobTypeForm(request.POST)
        if form.is_valid():
            jobtype = form.save(commit=False)
            jobtype.save()
            message = 'Registrado correctamente!'
            messages.add_message(request, messages.SUCCESS, message)
            return HttpResponseRedirect(reverse(jobtypes_index))
        else:
            message = 'Existen errores por favor verifica!.'
            messages.add_message(request, messages.ERROR, message)
    else:
        form = JobTypeForm()
    return render(request, 'jobtypes/new.html', {
        'form': form,
    })


@permission_required('jobs.change_jobtype', login_url='/log_in')
def jobtypes_edit(request, id):
    jobtype = JobType.objects.get(id=id)
    if request.method == 'POST':
        jobtype_form = JobTypeForm(request.POST, request.FILES, instance=jobtype)
        if jobtype_form.is_valid():
            save_jobtype = jobtype_form.save()

            message = "actualizado Correctamente"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse(jobtypes_index))
    else:
        jobtype_form = JobTypeForm(instance=jobtype)
    return render(request, 'jobtypes/edit.html', {
        'form': jobtype_form
    })

@permission_required('jobs.delete_jobtype', login_url='/log_in')
def jobtypes_delete(request, id):
    jobtype = JobType.objects.get(id=id)
    if not Job.objects.filter(jobtype_id=int(id)).exists():
        jobtype.delete()
    is_exist = JobType.objects.filter(id=id).exists()

    if is_exist:
        message = 'No se pudo eliminar'
        messages.add_message(request, messages.ERROR, message)
    else:
        message = 'Eliminado!'
        messages.add_message(request, messages.SUCCESS, message)

    return HttpResponseRedirect(reverse(jobtypes_index))


# ZONES
@permission_required('jobs.index_zone', login_url='/log_in')
def zones_index(request):
    zones_all = Zone.objects.all()
    return render(request, 'zones/index.html', {
        'zone_obj': Zone,
        'zones': zones_all,
    })


@permission_required('jobs.add_zone', login_url='/log_in')
def zones_new(request):
    if request.method == 'POST':
        form = ZoneForm(request.POST)
        if form.is_valid():
            zone = form.save(commit=False)
            zone.save()
            message = 'Registrado correctamente!'
            messages.add_message(request, messages.SUCCESS, message)
            return HttpResponseRedirect(reverse(zones_index))
        else:
            message = 'Existen errores por favor verifica!.'
            messages.add_message(request, messages.ERROR, message)
    else:
        form = ZoneForm()
    return render(request, 'zones/new.html', {
        'form': form,
    })


@permission_required('jobs.change_zone', login_url='/log_in')
def zones_edit(request, id):
    zone = Zone.objects.get(id=id)
    if request.method == 'POST':
        zone_form = ZoneForm(request.POST, request.FILES, instance=zone)
        if zone_form.is_valid():
            save_zone = zone_form.save()

            message = "actualizado Correctamente"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse(zones_index))
    else:
        zone_form = ZoneForm(instance=zone)
    return render(request, 'zones/edit.html', {
        'form': zone_form
    })


@permission_required('jobs.delete_zone', login_url='/log_in')
def zones_delete(request, id):
    zone = Zone.objects.get(id=id)
    if not Job.objects.filter(zone_id=int(id)).exists():
        zone.delete()

    is_exist = Zone.objects.filter(id=id).exists()

    if is_exist:
        message = 'No se pudo eliminar'
        messages.add_message(request, messages.ERROR, message)
    else:
        message = 'Eliminado!'
        messages.add_message(request, messages.SUCCESS, message)

    return HttpResponseRedirect(reverse(zones_index))


# JOB HISTORIES
def jobhistories_index(request):
    jobhistories_all = JobHistory.objects.all()
    return render(request, 'jobhistories/index.html', {
        'jobhistory_instance': JobHistory,
        'jobhistories': jobhistories_all,
    })


def jobhistories_new(request, pj_id):
    if request.method == 'POST':
        form = JobHistoryForm(request.POST)
        if form.is_valid():
            jobhistory = form.save(commit=False)
            jobhistory.save()
            message = 'Registrado correctamente!'
            messages.add_message(request, messages.SUCCESS, message)
            return HttpResponseRedirect(reverse(jobhistories_index))
        else:
            message = 'Existen errores por favor verifica!.'
            messages.add_message(request, messages.ERROR, message)
    else:
        pj = ProfileJob.objects.get(pk=int(pj_id))
        form = JobHistoryForm(initial={'profilejob': pj})
    return render(request, 'jobhistories/new.html', {
        'form': form,
    })


def jobhistories_edit(request, id):
    jobhistory = JobHistory.objects.get(id=id)
    if request.method == 'POST':
        jobhistory_form = JobHistoryForm(request.POST, request.FILES, instance=jobhistory)
        if jobhistory_form.is_valid():
            save_jobhistory = jobhistory_form.save()

            message = "actualizado Correctamente"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse(jobhistories_index))
    else:
        jobhistory_form = JobHistoryForm(instance=jobhistory)
    return render(request, 'jobhistories/edit.html', {
        'form': jobhistory_form
    })


def jobhistories_show(request, id):
    jobhistory = JobHistory.objects.get(id=id)

    return render(request, 'jobhistories/show.html', {
        'jobhistory': jobhistory,
        'jobhistory_instance': JobHistory,
        'user_instance': User,
    })


def jobhistories_delete(request, id):
    jobhistory = JobHistory.objects.get(id=id)
    jobhistory.delete()
    is_exist = JobHistory.objects.filter(id=id).exists()

    if is_exist:
        message = 'No se pudo eliminar'
        messages.add_message(request, messages.ERROR, message)
    else:
        message = 'Eliminado!'
        messages.add_message(request, messages.SUCCESS, message)

    return HttpResponseRedirect(reverse(jobhistories_index))


class JobViewSet(APIView):
    def get(self, request, imei, format=None):

        if imei is not None and Profile.objects.filter(imei_code=imei).exists():

            profile = Profile.objects.get(imei_code=imei)

            jobs = Job.objects.filter(profilejob__profile=profile, state__in=['NUEVO', 'EN_PROCESO'])

            serializer_class = JobSerializer(jobs, many=True)

            return Response({'jobs': serializer_class.data})
        else:
            message = {'message': 'Imei no registrado'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


# FORMAT API
'''
{
	"job_id": 1,
	"imei_code": "123456789",
	"state": "P",
	"observation": "Esto es una observacion",
	"lat": "-12.312123",
	"lng": "12.123123123"
}
'''


class HistoryViewSet(APIView):
    renderer_classes = (JSONRenderer,)

    def post(self, request, format=None):
        # print request.data
        updates = []
        if request.data.has_key('updates') is None:
            message = {'message': 'No Existen Actualizaciones'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            updates = request.data['updates']
            response_json = []

            for history in updates:
                print history['imei_code']
                job_id = history['job_id']
                imei = history['imei_code']
                # imei = '123456789'

                state = history['h_state'] if history.has_key('h_state') else None
                observation = history['h_observation'] if history.has_key('h_observation') else None
                lat = history['h_lat'] if history.has_key('h_lat') else None
                lng = history['h_lng'] if history.has_key('h_lng') else None

                if Profile.objects.filter(imei_code=imei).exists() and Job.objects.filter(pk=job_id).exists():
                    profile = Profile.objects.get(imei_code=imei)

                    job = Job.objects.get(pk=job_id)
                    job.state = state
                    job.save(update_fields=['state'])

                    pj = ProfileJob.objects.get(profile=profile, job_id=job_id)
                    pj.state = state
                    pj.save(update_fields=['state'])

                    jh = JobHistory(observation=observation,
                                    lat=lat,
                                    lng=lng,
                                    state=state,
                                    profile_id=profile.id,
                                    profilejob_id=pj.id)
                    jh.save()
                    build_notification(imei, job_id, state)

                    build_json = {'imei_code': imei,
                                  'state': state,
                                  'lat': lat,
                                  'lng': lng,
                                  'observation': observation,
                                  'job_id': job.id,
                                  'profile_id': profile.id}

                    response_json.append(build_json)

            return Response({"updates": response_json}, status=status.HTTP_201_CREATED)

            # message = {'message': 'No Existe perfil o Tarea'}
            # return Response(message, status=status.HTTP_400_BAD_REQUEST)


def build_notification(imei, job_id, state):
    profile = Profile.objects.get(imei_code=imei)

    job = Job.objects.get(pk=job_id)
    pj = ProfileJob.objects.get(profile=profile, job=job)

    notification = Notification(profile_id=profile.id,
                                level='LOW',
                                type='MES',
                                title='Historial enviado por: %s' % (profile),
                                content='Se envio el historial con estado %s' % (state),
                                obj='ProfileJob',
                                obj_id=pj.id,
                                )
    notification.save()


# JOBS MAPS

def jobs_maps_index(request):
    filter = request.GET.get('filter')

    if filter == 'assig':
        pj = ProfileJob.objects.all().values_list('id', flat=True)
        jobs_all = Job.objects.filter(pk__in=pj)
    elif filter == 'wassig':
        jobs_all = Job.objects.filter(profilejob__profile=None)
    elif filter == 'comp':
        jobs_all = Job.objects.filter(state='TERMINADO')
    else:
        jobs_all = Job.objects.all()
    return render(request, 'jobs/maps/index.html', {
        'job_obj': Job,
        'jobs': jobs_all,
    })


# JOBS
def jobs_index(request):
    if request.user.is_superuser or Profile.objects.get(user_id=request.user.id).rol == 'SUP':
        jobs_all = Job.objects.all()
    else:
        profile = Profile.objects.get(user_id=request.user.id)
        jobs_all = Job.objects.filter(profilejob__profile=profile)

    # jobs_all = Job.objects.all()
    return render(request, 'jobs/index.html', {
        'job_obj': Job,
        'jobs': jobs_all,
    })


def jobs_new(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.save()
            message = 'Registrado correctamente!'
            messages.add_message(request, messages.SUCCESS, message)
            return HttpResponseRedirect(reverse(jobs_index))
        else:
            message = 'Existen errores por favor verifica!.'
            messages.add_message(request, messages.ERROR, message)
    else:
        form = JobForm()
    return render(request, 'jobs/new.html', {
        'form': form,
    })


def jobs_edit(request, id):
    job = Job.objects.get(id=id)
    if request.method == 'POST':
        job_form = JobForm(request.POST, request.FILES, instance=job)
        if job_form.is_valid():
            save_job = job_form.save()

            message = "actualizado Correctamente"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse(jobs_index))
    else:
        job_form = JobForm(instance=job)
    return render(request, 'jobs/edit.html', {
        'form': job_form,
        'job': job
    })


def jobs_show(request, id):
    job = Job.objects.get(id=id)

    return render(request, 'jobs/show.html', {
        'job': job,
        'job_obj': Job,
    })


def jobs_delete(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    is_exist = Job.objects.filter(id=id).exists()

    if is_exist:
        message = 'No se pudo eliminar'
        messages.add_message(request, messages.ERROR, message)
    else:
        message = 'Eliminado!'
        messages.add_message(request, messages.SUCCESS, message)

    return HttpResponseRedirect(reverse(jobs_index))


# PROFILE JOBS
def profilejobs_index(request):
    profilejobs_all = ProfileJob.objects.all()
    return render(request, 'profilejobs/index.html', {
        'profilejob_obj': ProfileJob,
        'profile_obj': Profile,
        'job_obj': Job,
        'profilejobs': profilejobs_all,
    })


def profilejobs_new(request, j_id):
    if request.method == 'POST':
        form = ProfileJobForm(request.POST)
        if form.is_valid():
            profilejob = form.save(commit=False)
            pj = profilejob.save()

            profilejob = ProfileJob.objects.get(pk=profilejob.id)

            job = Job.objects.get(pk=profilejob.job_id)
            job.state = request.POST.get('state')
            job.save(update_fields=['state'])

            message = 'Registrado correctamente!'
            messages.add_message(request, messages.SUCCESS, message)
            return HttpResponseRedirect(reverse(profilejobs_index))
        else:
            message = 'Existen errores por favor verifica!.'
            messages.add_message(request, messages.ERROR, message)
    else:
        job = Job.objects.get(pk=int(j_id))
        form = ProfileJobForm(initial={'job': job})
    return render(request, 'profilejobs/new.html', {
        'form': form,
    })


def profilejobs_edit(request, id):
    profilejob = ProfileJob.objects.get(id=id)
    if request.method == 'POST':
        profilejob_form = ProfileJobForm(request.POST, request.FILES, instance=profilejob)
        if profilejob_form.is_valid():
            save_profilejob = profilejob_form.save()

            job = Job.objects.get(pk=profilejob.job_id)
            job.state = request.POST.get('state')
            job.save(update_fields=['state'])

            message = "actualizado Correctamente"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse(profilejobs_index))
    else:
        profilejob_form = ProfileJobForm(instance=profilejob)
    return render(request, 'profilejobs/edit.html', {
        'form': profilejob_form
    })


def profilejobs_show(request, id):
    profilejob = ProfileJob.objects.get(id=id)
    jobhistories = JobHistory.objects.filter(profilejob=profilejob)

    return render(request, 'profilejobs/show.html', {
        'profilejob': profilejob,
        'profilejob_obj': ProfileJob,
        'job_obj': Job,
        'profile_obj': Profile,
        'jobhistories': jobhistories,
        'jobhistory_obj': JobHistory,
    })


def profilejobs_delete(request, id):
    profilejob = ProfileJob.objects.get(id=id)
    profilejob.delete()
    is_exist = ProfileJob.objects.filter(id=id).exists()

    if is_exist:
        message = 'No se pudo eliminar'
        messages.add_message(request, messages.ERROR, message)
    else:
        message = 'Eliminado!'
        messages.add_message(request, messages.SUCCESS, message)

    return HttpResponseRedirect(reverse(profilejobs_index))
