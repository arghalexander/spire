# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

@admin.register(MembershipProduct)
class MembershipProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'price', 'membership_length', 'subscription')
