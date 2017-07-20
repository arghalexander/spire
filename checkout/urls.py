from django.conf.urls import url

from . import views

urlpatterns = [
    
	url(r'membership/order/$', views.membership_checkout, name='membership-checkout'),
	url(r'membership/cart/$', views.membership_cart, name='membership-cart'),
    url(r'membership/add/$', views.membership_add_to_cart, name='membership-add'),
    url(r'membership/success/$', views.membership_success, name='membership-success'),

    url(r'event/add/$', views.event_add_to_cart, name='event-add'),
    url(r'event/cart/$', views.event_cart, name='event-cart'),
    url(r'event/order/$', views.event_checkout, name='event-checkout'),
    url(r'event/success/$', views.event_success, name='event-success'),


    url(r'membership-combo/add/$', views.combo_add_to_cart, name='combo-add'),
    url(r'membership-combo/order/$', views.combo_checkout, name='combo-checkout'),
    url(r'membership-combo/cart/$', views.combo_cart, name='combo-cart'),
    url(r'membership-combo/success/$', views.combo_success, name='combo-success'),

    url(r'order/$', views.checkout, name='checkout'),  
	url(r'cart/$', views.cart, name='cart'),
    url(r'add/$', views.cart_add, name='add'),
    url(r'success/$', views.cart_success, name='success'),

]
