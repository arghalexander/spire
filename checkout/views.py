# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect,render_to_response
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from cart.cart import Cart
import stripe
from products.models import MembershipProduct, EventProduct

from .forms import PaymentForm

from django.conf import settings
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
	
	#get cart total
	cart = Cart(request)
	

	if cart.count() == 0:
		return redirect('checkout:membership-cart')

	total = cart.summary()
	description = cart[0].product_name

	if request.method == 'POST':
		
		stripe.api_key = settings.STRIPE_SECRET_KEY

		# Get the credit card details submitted by the form
		token = request.POST['stripeToken']

		

		# Create a charge: this will charge the user's card
		try:
		  charge = stripe.Charge.create(
			  amount=int(total*100),
			  currency="usd",
			  source=token,
			  description=""
		  )
		  return redirect('checkout:membership-success')
		except stripe.error.CardError as e:
			print(e)
			return render(request, 'checkout/membership_checkout.html', {'error': e})


	return render(request, 'checkout/membership_checkout.html',{'settings': settings, 'cart': Cart(request)})



@login_required
def membership_success(request):
	#empty cart
	cart = Cart(request)
	cart.clear()
	return render(request, 'checkout/membership_checkout_success.html')



def remove_from_cart(request, product_id):
	product = Product.objects.get(id=product_id)
	cart = Cart(request)
	cart.remove(product)





def event_cart(request):
	pass


def event_checkout(request):
	pass



