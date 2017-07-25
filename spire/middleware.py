from django.contrib import messages
from members.models import Member
from django.shortcuts import redirect
from django.urls import resolve

def CreateMembershipMiddleware(get_response):

	def middleware(request):

		#if not request.user.is_staff:
		#if user logged in and has not created a profile, direct them to profile create view
		if not resolve(request.path).view_name == 'members:member-create' and not request.path == '/accounts/logout/' : 
			if request.user.is_authenticated:
				try:
					member = Member.objects.get(user=request.user)
				except Member.DoesNotExist:
					messages.warning(request, 'Please complete your member profile')
					return redirect('members:member-create')

				#student memebrs might have empty profile, test on mobile phone to see
				#if member.mobile_phone == '':
				#	messages.warning(request, 'Please complete your member profile')
				#	return redirect('members:member-create')

		
		response = get_response(request)


		return response

	return middleware