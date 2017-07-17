from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^jobs/new/$', views.job_create, name='job-create'),
    url(r'^jobs/(?P<job_id>[0-9]+)/$', views.job_detail, name='job-detail'),
]
