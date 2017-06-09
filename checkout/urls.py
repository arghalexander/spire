from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'membership/order/$', views.membership_checkout, name='membership-checkout'),  
	url(r'membership/cart/$', views.membership_cart, name='membership-cart'),
    url(r'membership/add/$', views.membership_add_to_cart, name='membership-add'),
]