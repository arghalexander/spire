from django.conf.urls import url

from . import views

app_name = 'members'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^profile/(?P<member_id>[0-9]+)/$', views.member_profile, name='member-profile-lookup'),
    
  
 	url(r'^create/$', views.member_create, name='member-create'),   

    url(r'^profile/$', views.my_profile, name='member-profile'),
   	url(r'^profile/edit/$', views.my_profile_edit, name='member-profile-edit'),

    #url(r'(?P<pk>[0-9]+)/event-attendance/$', views.member_event_attendance, name='get-event-attendance'),
    
]