from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class MembershipLevel(models.Model):
	level = models.CharField(max_length=254) 

	def __str__(self):              # __unicode__ on Python 2
		return self.level

class Member(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	membership_level = models.ManyToManyField(MembershipLevel, related_name="membership_levels")

	def __str__(self):              # __unicode__ on Python 2
		return self.user.email


