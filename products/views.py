# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect,render_to_response

from cart.cart import Cart
from .models import MembershipProduct, EventProduct

from django.contrib import messages

def membership_add_to_cart(request):
	"""
	Add a membership level to cart, remove existing membership level if there is one in the cart
	"""

	product_id = request.GET.get('product_id', '')
	try:
		product = MembershipProduct.objects.get(id=product_id)
	except MembershipProduct.DoesNotExist:
		messages.add_message(request, messages.ERROR, "Product id does not exist")
		
	cart = Cart(request)
	cart.add(product, product.price, 1)

	return redirect('products:new-membership')
	


def remove_from_cart(request, product_id):
	product = Product.objects.get(id=product_id)
	cart = Cart(request)
	cart.remove(product)

def get_cart(request):
	return render_to_response('cart.html', dict(cart=Cart(request)))



def newMembership(request):
	return render(request, 'products/membership_cart.html', {})
