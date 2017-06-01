from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'new-mebership/$', views.newMembership, name='new-membership'),
    url(r'add-membership/$', views.membership_add_to_cart, name='add-membership'),
]