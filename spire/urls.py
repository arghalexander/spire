"""spire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from django.views.defaults import server_error, page_not_found, permission_denied

#from registration.backends.hmac.views import RegistrationView
from spire.registration.forms import MemberRegistrationForm
from spire.registration.views import RegistrationView

from members.views import MemberViewSet, MembershipLevelViewSet, MemberAddressViewSet, MemberNoteViewSet, MemberRegionViewSet, MemberIndustryViewSet, member_profile
from events.views import EventViewSet, EventAttendanceViewSet

from .views import UserViewSet, check_login


from rest_framework import routers

router = routers.DefaultRouter()

#Member endpoints
router.register(r'members', MemberViewSet)
router.register(r'member-address', MemberAddressViewSet)
router.register(r'membership-levels', MembershipLevelViewSet)
router.register(r'member-notes', MemberNoteViewSet)
router.register(r'member-regions', MemberRegionViewSet)
router.register(r'member-industry', MemberIndustryViewSet)
#Event endpoints
router.register(r'events', EventViewSet)
router.register(r'event-attendance', EventAttendanceViewSet)

#Event endpoints
router.register(r'users', UserViewSet)


urlpatterns = [

    url(r'^404/$', page_not_found, kwargs={'exception': Exception("Page not Found")}),
    url(r'^500/$', server_error),



    url(r'^checkout/', include('checkout.urls', namespace='checkout')),
    url(r'^members/', include('members.urls', namespace='members')),
    url(r'^events/', include('events.urls', namespace='events')),


    url(r'^accounts/register/$',  RegistrationView.as_view(form_class=MemberRegistrationForm), name='registration_register'),
    url(r'^accounts/login/$', check_login),

    #url(r'^password_reset/$', auth_views.password_reset.as_view(),  html_email_template_name='registration/password_reset_email.html', email_template_name='registration/password_reset_email.txt',name='password_reset'),
    url(r'^accounts/reset_password/$',auth_views.password_reset, {'html_email_template_name': 'registration/password_reset_email.html','email_template_name': 'registration/password_reset_email.txt'}),

    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^tinymce/', include('tinymce.urls')),
    url('', include('social_django.urls', namespace='social')),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^spire/', include('spiresite.urls', namespace='spiresite')),

    url(r'^cms/', include(wagtailadmin_urls)),

    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', admin.site.urls),

    url(r'', include(wagtail_urls)),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
