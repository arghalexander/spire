from django.conf.urls import url

from . import views

app_name = 'events'
urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^event/(?P<slug>[-\w]+)/$', views.event_detail, name='event-detail'),
    url(r'^attendance-autocomplete/$',views.EventAttendanceAutocomplete.as_view(),name='attendance-autocomplete',),
]