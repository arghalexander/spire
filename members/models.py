from __future__ import unicode_literals
import os
import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from .validators import validate_redacted


from events.models import Event




class MembershipLevel(models.Model):
	level = 							models.CharField(max_length=254, primary_key=True) 
	price = 							models.DecimalField(max_digits=8, decimal_places=2)

	def __str__(self):            
		return self.level


class MemberIndustry(models.Model):
	industry = 							models.CharField(max_length=254) 

	def __str__(self):            
		return self.industry



class MemberRegion(models.Model):
	region =	 						models.CharField(max_length=254) 

	def __str__(self):            
		return self.region


class Member(models.Model):
	user = 								models.OneToOneField(User, on_delete=models.CASCADE)
	
	membership_level =					models.ForeignKey(MembershipLevel, related_name="membership_levels", blank=True, default="guest")
	membership_expiration =				models.DateTimeField(blank=True, null=True)
	
	image =								models.ImageField(upload_to='members', default=os.path.join(settings.MEDIA_URL,'defaults/headshot.png'))	
	
	mobile_phone =						models.CharField(max_length=254, blank=True)
	work_phone = 						models.CharField(max_length=254, blank=True)

	bio = 								models.TextField(blank=True)
	skills_specialties = 				models.TextField(blank=True)

	region = 							models.ManyToManyField(MemberRegion,related_name="member_regions")

	linkedIn = 							models.CharField(max_length=254, blank=True)
	facebook = 							models.CharField(max_length=254, blank=True)
	twitter = 							models.CharField(max_length=254, blank=True)

	company = 							models.CharField(max_length=254, blank=True)
	industry =							models.OneToOneField(MemberIndustry, related_name="member_industry", blank=True, null=True)
	

	def __str__(self):             
		return self.user.email


	def full_name(self):
		return self.user.first_name + ' ' + self.user.last_name

	def is_expiring(self):
		pass

	def upgrade_membership(self):
		pass


class MemberAddress(models.Model):
	member = 							models.OneToOneField(Member, related_name="address")
	ADDRESS_TYPES = (
		('HOME', 'Home'),
		('SEASONAL', 'Seasonal'),
		('ONE_TIME', '1-time'),
		('PREFERRED', 'Preferred'),
	)
	address_type = 						models.CharField(max_length=50,choices=ADDRESS_TYPES)

	address_line_one = 					models.CharField(max_length=255)
	address_line_two = 					models.CharField(max_length=255, blank=True)
	city = 								models.CharField(max_length=255)
	state = 							models.CharField(max_length=255)
	zip_code =							models.CharField(max_length=255)

	def __str__(self):       
		return self.member.user.email




class MemberEducation(models.Model):
	member = 							models.ForeignKey(Member, related_name="education")
	DEGREE_TYPES = (
		('UNDERGRAD', 'Undergraduate'),
		('MA', 'MA'),
		('MS', 'MS'),
		('MBA', 'MBA'),
		('JD', 'JD'),
		('PHD', 'PHD'),
	)
	degree = 						models.CharField(max_length=50,choices=DEGREE_TYPES)
	program = 						models.CharField(max_length=255, blank=True)
	grad_year = 					models.IntegerField()

	def __str__(self):       
		return self.member.user.email




class MemberNote(models.Model):
	member = 							models.ForeignKey(Member)
	user = 								models.ForeignKey(User)
	note = 								models.TextField(blank=False)
	date =  							models.DateTimeField(auto_now=True)

	def __str__(self):       
		return self.member.user.email






class MemberPurchaseHistory(models.Model):
	member = 							models.ForeignKey(Member)
	item = 					  			models.CharField(max_length=255)
	purchase_date = 					models.DateTimeField(auto_now=True)
	purchase_price = 					models.DecimalField(max_digits=8, decimal_places=2)
	note = 								models.TextField(blank=True)
	cc_num_redacted = 					models.CharField(max_length=32,validators=[validate_redacted])

	def __str__(self):       
		return self.member.user.email

	



class MemberStatusHistory(models.Model):
	member = 							models.ForeignKey(Member)
	
	ACTIONS = (
		('UPGRADE', 'Upgrade'),
		('DOWNGRADE', 'Downgrade'),
	)
	action = 							models.CharField(max_length=50,choices=ACTIONS)
	date = 								models.DateTimeField(auto_now=True)

	def __str__(self):       
		return self.member.user.email


