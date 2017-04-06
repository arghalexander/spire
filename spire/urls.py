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


from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from registration.backends.hmac.views import RegistrationView
from members.forms import MemberRegistrationForm

from members.views import MemberViewSet

from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^events/', include('events.urls')),

    url(r'^accounts/register/$',  RegistrationView.as_view(form_class=MemberRegistrationForm), name='registration_register'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    #
    
    url(r'^tinymce/', include('tinymce.urls')),

    url('', include('social_django.urls', namespace='social')),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'', include(wagtail_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
