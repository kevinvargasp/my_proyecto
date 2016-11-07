from django.conf.urls import url, include
from notifications import views

urlpatterns = [
    url(r'^notifications/index/$', views.notifications_index, name='notifications-index'),
    url(r'^notifications/show/(?P<id>\d+)/$', views.notifications_show, name='notifications-show'),
    url(r'^notifications/delete/(?P<id>\d+)/$', views.notifications_delete, name='notifications-delete'),

]
