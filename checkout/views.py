# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,render_to_response
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

from cart.cart import Cart
import stripe

import datetime


from products.models import MembershipProduct, MembershipLevel
from events.models import EventPricing, Event, EventAttendance, Product
from members.models import Member, MemberPurchaseHistory, MemberMembershipHistory

from .forms import PaymentForm
from django.utils import formats

from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse



def record_purchase(member, item, price, stripe_id):
	history = MemberPurchaseHistory(member=member,item=item,purchase_price=price, note=stripe_id)
	history.save()


def record_membership_change(member,new_level, previous_level):
	history = MemberMembershipHistory(member=member,new_level=new_level, previous_level=previous_level)
	history.save()




def cart_add(request):
	product_id = request.GET.get('product', '')

	try:
		product = Product.objects.get(sku=product_id)
	except Product.DoesNotExist:
		messages.add_message(request, messages.ERROR, "Product does not exist")
		return redirect('checkout:cart')

	cart = Cart(request)
	cart.clear()

	cart.add(product, product.price, 1)
	return redirect('checkout:cart')


@login_required
def cart(request):
	cart = Cart(request)
	if cart.count() == 0:
		messages.warning(request, 'Cart is Empy')

	return render(request, 'checkout/cart.html', dict(cart=Cart(request)))



@login_required
def checkout(request):

	#get cart total
	cart = Cart(request)


	if cart.count() == 0:
		return redirect('checkout:cart')

	total = cart.summary()

	for item in cart:
		selected_membership = item.product
		description = item.product.name

	if request.method == 'POST':

		try:
			stripe.api_key = settings.STRIPE_SECRET_KEY

			# Get the credit card details submitted by the form
			token = request.POST['stripeToken']

			# Create a charge: this will charge the user's card
			try:

				customer = stripe.Customer.create(
					email= request.user.username,
					source= request.user.username,
				)

				charge = stripe.Charge.create(
					  amount=int(total*100),
					  customer=customer,
					  currency="usd",
					  source=token,
					  description=description
				 )

				cart.clear()

				member = Member.objects.get(user=request.user)

				#record purchase
				record_purchase(member,description,total, charge.id)

			  	return redirect('checkout:success')

			except stripe.error.CardError as e:
				print(e)
				return render(request, 'checkout/checkout.html', {'error': e})
		except stripe.InvalidRequestError as e:
			return render(request, 'checkout/checkout.html', {'error': e})

	return render(request, 'checkout/checkout.html',{'settings': settings, 'cart': Cart(request)})



@login_required
def cart_success(request):
	#empty cart
	cart = Cart(request)
	cart.clear()
	return render(request, 'checkout/checkout_success.html')





def membership_add_to_cart(request):
	"""
	Add a membership level to cart, remove existing membership level if there is one in the cart
	"""

	product_id = request.GET.get('product_id', '')

	try:
		product = MembershipProduct.objects.get(id=int(product_id))
	except MembershipProduct.DoesNotExist:
		messages.add_message(request, messages.ERROR, "Product id does not exist")
		#return redirect('checkout:membership-cart')

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


	for item in cart:
		selected_membership = item.product
		description = item.product.name


	if request.method == 'POST':

		try:
			stripe.api_key = settings.STRIPE_SECRET_KEY

			# Get the credit card details submitted by the form
			token = request.POST['stripeToken']

			# Create a charge: this will charge the user's card
			try:
				charge = stripe.Charge.create(
					  amount=int(total*100),
					  currency="usd",
					  source=token,
					  description=description
				 )

				cart.clear()



				member = Member.objects.get(user=request.user)

				previous_level = member.membership_level

				member.membership_level = selected_membership.membership_level

				#if there is already a membership expiration set, add time to current
				if member.membership_expiration:
					member.membership_expiration = member.membership_expiration + datetime.timedelta(days=selected_membership.membership_length*365)
				else:
					member.membership_expiration = datetime.datetime.now() + datetime.timedelta(days=selected_membership.membership_length*365)
				member.save()

				#record purchase
				record_purchase(member,description,total, charge.id)

				#record membership change
				record_membership_change(member,member.membership_level, previous_level)

			  	return redirect('checkout:membership-success')

			except stripe.error.CardError as e:
				print(e)
				return render(request, 'checkout/membership_checkout.html', {'error': e})
		except stripe.InvalidRequestError as e:
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



def event_add_to_cart(request):
	"""
	Add a event pricing object to cart
	"""
	event_id = request.GET.get('event', '')

	try:
		event = Event.objects.get(id=event_id)
	except Event.DoesNotExist:
		messages.add_message(request, messages.ERROR, "Event does not exist")
		return redirect('checkout:event-cart')

	try:
		member = Member.objects.get(user=request.user)
	except Member.DoesNotExist:
		redirect('login')

	if EventAttendance.objects.filter(member=member, event=event).count() > 0:
		messages.warning(request,'You Are already registered for this event')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


	event_price = EventPricing.objects.get(event=event, level=member.membership_level)

	cart = Cart(request)

	cart.add(event, event_price.event_price, 1)

	return redirect('checkout:event-cart')



def event_cart(request):


	cart = Cart(request)

	if cart.count() == 0:
		messages.warning(request, 'Cart is Empy')

	return render(request, 'checkout/event_cart.html', dict(cart=Cart(request)))


@login_required
def event_checkout(request):

	#get cart total
	cart = Cart(request)


	if cart.count() == 0:
		return redirect('checkout:event-cart')

	total = cart.summary()


	for item in cart:
		description = item.product.title + ' ' + formats.date_format(item.product.start, "SHORT_DATETIME_FORMAT")
		event = item.product.id

	event = get_object_or_404(Event,id=event)

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
				  description=description
			)
		 	cart.clear()


			member = Member.objects.get(user=request.user)

			attendance = EventAttendance.objects.create(member=member, event=event)

			#record purchase
			record_purchase(member,description,total, charge.id)

			return redirect('checkout:event-success')

		except stripe.error.CardError as e:
			return render(request, 'checkout/event_checkout.html', {'error': e})
		except Member.DoesNotExist:
			messages.error(request, 'Membership Not Found, Please login or register')
			return redirect('/accounts/login/')


	return render(request, 'checkout/event_checkout.html',{'settings': settings, 'cart': Cart(request)})





@login_required
def event_success(request):
	#empty cart
	cart = Cart(request)
	cart.clear()
	return render(request, 'checkout/event_checkout_success.html')



@login_required
def combo_add_to_cart(request):
	"""
	Add a event pricing object to cart
	"""
	event_id = request.GET.get('event', '')
	#membership = request.GET.get('membership', '')

	try:
		event = Event.objects.get(id=event_id)
	except Event.DoesNotExist:
		messages.add_message(request, messages.ERROR, "Event does not exist")

	try:
		member = Member.objects.get(user=request.user)
	except Member.DoesNotExist:
		redirect('login')

	if EventAttendance.objects.filter(member=member, event=event).count() > 0:
		messages.warning(request,'You Are already registered for this event')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


	membership = MembershipProduct.objects.get(id=3)

	cart = Cart(request)
	cart.clear()
	cart.add(event, membership.price , 1)

	return redirect('checkout:combo-cart')




@login_required
def combo_cart(request):
	"""
	Add a event membership combo pricing object to cart
	"""
	cart = Cart(request)

	if cart.count() == 0:
		messages.warning(request, 'Cart is Empy')

	return render(request, 'checkout/combo_cart.html', dict(cart=Cart(request)))




@login_required
def combo_checkout(request):

	#get cart total
	cart = Cart(request)


	if cart.count() == 0:
		return redirect('checkout:combo-cart')

	total = cart.summary()


	for item in cart:
		#description = item.product.title + ' ' + formats.date_format(item.product.start, "SHORT_DATETIME_FORMAT")
		event = get_object_or_404(Event,id=item.product.id)


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
			  description="Membership + Event Combo"
		  )
		  cart.clear()


		  member = Member.objects.get(user=request.user)


		  attendance = EventAttendance.objects.create(member=member, event=event)

		  membership_level = get_object_or_404(MembershipLevel,slug="full")
		  member.membership_level = membership_level
		  member.save()

		  #record purchase
		  record_purchase(member,"Membership + Event Combo",total)

		  return redirect('checkout:combo-success')
		except stripe.error.CardError as e:
			return render(request, 'checkout/combo_checkout.html', {'error': e})
		except Member.DoesNotExist:
			messages.error(request, 'Membership Not Found, Please login or register')
			return redirect('login')


	return render(request, 'checkout/combo_checkout.html',{'settings': settings, 'cart': Cart(request)})

@login_required
def combo_success(request):
	#empty cart
	cart = Cart(request)
	cart.clear()
	return render(request, 'checkout/combo_checkout_success.html')
