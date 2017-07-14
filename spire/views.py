from rest_framework import viewsets
import django_filters.rest_framework
from django.shortcuts import render, redirect
from .serializers import UserSerializer

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



def check_login(request):
	if request.user.is_authenticated():
		return redirect('/')
	else:
		return login(request)

def login_view(request):
	username = request.POST.get('username', '')
	print(username)
	try:
		user = User.objects.get(username=username)
		print(user.password)

	except User.DoesNotExist:
		return login(request)

	return login(request)
