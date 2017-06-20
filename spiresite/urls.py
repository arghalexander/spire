from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^jobs/(?P<slug>[-\w\d]+)/$', views.job_detail, name='job-detail'),
]