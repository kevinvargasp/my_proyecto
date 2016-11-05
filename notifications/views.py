from django.shortcuts import render
from datetime import datetime
from notifications.models import Notification
from users.models import Profile
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import datetime

from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

def notifications_index(request):
    if request.user.is_superuser or Profile.objects.get(user_id=request.user.id).rol == 'SUP':
        notifications = Notification.objects.all()
    else:
        notifications = Notification.objects.filter(profile_id=Profile.objects.get(user_id=request.user.id))
    return render(request, 'notifications/index.html', {
        'notifications': notifications,
    })


def notifications_show(request, id):
    notification = Notification.objects.get(id=int(id))
    notification.read_at = datetime.now()
    notification.save(update_fields=['read_at'])

    return render(request, 'notifications/show.html', {
        'notification_obj': Notification,
        'notification': notification,
    })


def notifications_delete(request, id):
    notification = Notification.objects.get(id=id)
    notification.delete()
    is_exist = Notification.objects.filter(id=id).exists()

    if is_exist:
        message = 'No se pudo eliminar'
        messages.add_message(request, messages.ERROR, message)
    else:
        message = 'Eliminado!'
        messages.add_message(request, messages.SUCCESS, message)

    return HttpResponseRedirect(reverse(notifications_index))
