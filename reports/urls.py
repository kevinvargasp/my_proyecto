from django.conf.urls import url, include
from reports import views

# import api lib for routes
from reports.views import JobsStatePdf, EmployeesPdf, AssignPdf, AssignsPdf

urlpatterns = [
    url(r'^reports/index/$', views.index, name='report-index'),
    url(r'^reports/jobs/$', views.report_jobs, name='report-jobs'),
    url(r'^reports/jobs.pdf$', JobsStatePdf.as_view(), name='jobs-pdf'),
    url(r'^reports/employees/$', views.report_employees, name='report-employees'),
    url(r'^reports/employees.pdf$', EmployeesPdf.as_view(), name='employees-pdf'),
    url(r'^reports/assign.pdf$', AssignPdf.as_view(), name='assign-pdf'),
    url(r'^reports/assigns/$', views.report_assigns, name='report-assigns'),
    url(r'^reports/assigns.pdf$', AssignsPdf.as_view(), name='assigns-pdf'),
]

'''

        url(r'^(?P<c>\d+)/(?P<s>\d+)/(?P<m>\d+)/(?P<p>\d+)/student_state.pdf$', StudentStatePdf.as_view(),
            name='students-state-pdf'),
        url(r'^(?P<c>\d+)/(?P<s>\d+)/(?P<p>\d+)/total_student_state.pdf$', TotalStudentStatePdf.as_view(),
            name='total-students-state-pdf'),

'''
