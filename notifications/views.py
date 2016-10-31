from django.shortcuts import render
from datetime import datetime
from notifications.models import Notification
from users.models import Profile


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
