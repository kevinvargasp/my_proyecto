from django.conf.urls import url, include
from jobs import views

# import api lib for routes

urlpatterns = [

    url(r'^jobhistories/index$', views.jobhistories_index, name='jobhistories-index'),
    url(r'^jobhistories/new/(?P<pj_id>\d+)/$', views.jobhistories_new, name='jobhistories-new'),
    url(r'^jobhistories/edit/(\d+)/$', views.jobhistories_edit, name='jobhistories-edit'),
    url(r'^jobhistories/show/(\d+)/$', views.jobhistories_show, name='jobhistories-show'),
    url(r'^jobhistories/delete/(\d+)/$', views.jobhistories_delete, name='jobhistories-delete'),

    url(r'^api/v1/jobhistories/$', views.HistoryViewSet.as_view(), name='gmap_list'),
    url(r'^api/v1/jobs/(?P<imei>\d+)/$', views.JobViewSet.as_view(), name='job_list'),
    url(r'^jobs/index$', views.jobs_index, name='jobs-index'),
    url(r'^jobs/new/$', views.jobs_new, name='jobs-new'),
    url(r'^jobs/edit/(\d+)/$', views.jobs_edit, name='jobs-edit'),
    url(r'^jobs/show/(\d+)/$', views.jobs_show, name='jobs-show'),
    url(r'^jobs/delete/(\d+)/$', views.jobs_delete, name='jobs-delete'),

    url(r'^jobtypes/index$', views.jobtypes_index, name='jobtypes-index'),
    url(r'^jobtypes/new/$', views.jobtypes_new, name='jobtypes-new'),
    url(r'^jobtypes/edit/(\d+)/$', views.jobtypes_edit, name='jobtypes-edit'),
    url(r'^jobtypes/show/(\d+)/$', views.jobtypes_show, name='jobtypes-show'),
    url(r'^jobtypes/delete/(\d+)/$', views.jobtypes_delete, name='jobtypes-delete'),

    url(r'^profilejobs/index$', views.profilejobs_index, name='profilejobs-index'),
    url(r'^profilejobs/new/(?P<j_id>\d+)/$', views.profilejobs_new, name='profilejobs-new'),
    url(r'^profilejobs/edit/(\d+)/$', views.profilejobs_edit, name='profilejobs-edit'),
    url(r'^profilejobs/show/(\d+)/$', views.profilejobs_show, name='profilejobs-show'),
    url(r'^profilejobs/delete/(\d+)/$', views.profilejobs_delete, name='profilejobs-delete'),

]
