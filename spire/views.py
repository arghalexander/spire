from rest_framework import viewsets
import django_filters.rest_framework

from .serializers import UserSerializer

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
	filter_fields = ('id', 'first_name','last_name','groups')

