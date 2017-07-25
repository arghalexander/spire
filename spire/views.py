from rest_framework import viewsets
import django_filters.rest_framework
from django.shortcuts import render, redirect
from .serializers import UserSerializer
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.contrib import auth

from .admin import *

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
	filter_fields = ('id', 'first_name','last_name','groups')



def csrf_failure(request, reason=""):
    ctx = {'message': 'CSRF Token Failure'}
    return render_to_response('403.html', ctx)



def check_login(request):
	if request.user.is_authenticated():
		return redirect('/')
	else:
		return login(request)

def login_view(request):
	print('here')
	#if user is already logged in take them to membership page
	if request.user.is_authenticated():
		return redirect('/members/profile/')
	else:
		return login(request)


	username = request.POST.get('username', '')
	try:
		user = User.objects.get(username=username)
		print(user.password)
		if user.password == '':

			print('no password set')
			password = User.objects.make_random_password()
			user.set_password(password)
			user.save()

			messages.info(request, 'For security reasons we need you to reset your password')
			return redirect('password_reset')
	except User.DoesNotExist:
		return login(request)

	return login(request)
