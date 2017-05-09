from django.conf.urls import url

from . import views

app_name = 'members'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create_member, name='create-member'),
    url(r'^address/$', views.create_member_address, name='create-member-address'),
    url(r'^edit/$', views.edit_member, name='edit-member-view'),
    #url(r'(?P<pk>[0-9]+)/event-attendance/$', views.member_event_attendance, name='get-event-attendance'),
]