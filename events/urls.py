from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^event/(?P<slug>[-\w\d]+)/$', views.event_detail, name='event-detail'),
]