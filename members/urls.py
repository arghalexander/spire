from django.conf.urls import url

from . import views

app_name = 'members'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    #url(r'^address/$', views.create_member_address, name='create-member-address'),
   
 	url(r'^create/$', views.member_create, name='member-create'),
   
    url(r'^profile/$', views.member_profile, name='member-profile'),
   	url(r'^profile/edit/$', views.member_profile_edit, name='member-profile-edit'),


    #url(r'(?P<pk>[0-9]+)/event-attendance/$', views.member_event_attendance, name='get-event-attendance'),
]