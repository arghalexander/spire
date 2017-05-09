from __future__ import unicode_literals
from wagtail.wagtailcore.fields import RichTextField
from tinymce.models import HTMLField
from django.db import models


class Event(models.Model):
	title =							 		models.CharField(max_length=254)
	slug = 									models.SlugField()
	all_day = 								models.BooleanField()
	start = 								models.DateTimeField()
	end =									models.DateTimeField()
	Location = 								models.TextField()
	Description = 							RichTextField()


	def __str__(self):
		return self.title


class EventAttendance(models.Model):
	event = 								models.ForeignKey(Event, related_name="events")
	member = 								models.ForeignKey('members.Member', related_name="member")


class EventPricingLevel(models.Model):
	event = 								models.ForeignKey(Event, related_name="event_pricing")
	membership_level = 						models.ForeignKey('members.MembershipLevel', related_name="membership_level") #avoid circular dependency
	price = 								models.DecimalField(max_digits=8, decimal_places=2)

	def __str__(self):
		return self.event.title