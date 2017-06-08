# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect,render_to_response
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from cart.cart import Cart
from products.models import MembershipProduct, EventProduct

#from .forms import PaymentForm

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse



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
	cart.clear()

	cart.add(product, product.price, 1)

	return redirect('checkout:membership-cart')
	

@login_required
def membership_cart(request):

	cart = Cart(request)

	if cart.count() == 0:
		messages.warning(request, 'Cart is Empy') 

	return render(request, 'checkout/membership_cart.html', dict(cart=Cart(request)))



@login_required
def membership_checkout(request):
	if request.method == 'POST':
		form = PaymentForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = PaymentForm()

	return render(request, 'name.html', {'form': form})




def remove_from_cart(request, product_id):
	product = Product.objects.get(id=product_id)
	cart = Cart(request)
	cart.remove(product)



