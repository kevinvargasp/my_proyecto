from django.shortcuts import render

# Create your views here.
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
