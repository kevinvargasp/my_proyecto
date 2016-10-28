from django.conf.urls import url, include
from notifications import views

urlpatterns = [
    url(r'^notifications/index/$', views.notifications_index, name='notifications-index'),

]