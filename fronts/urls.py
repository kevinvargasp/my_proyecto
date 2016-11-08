from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api_docs', views.api_view, name='api-docs'),
]
