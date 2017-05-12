from __future__ import unicode_literals
from wagtail.wagtailcore.fields import RichTextField
from tinymce.models import HTMLField
from django.db import models

from modelcluster.models import ClusterableModel
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel

class Event(ClusterableModel):
	title =							 		models.CharField(max_length=254)
	slug = 									models.SlugField()
	all_day = 								models.BooleanField()
	start = 								models.DateTimeField()
	end =									models.DateTimeField()
	location = 								models.TextField()
	description = 							RichTextField()


	def __str__(self):
		return self.title

	panels = [
		FieldPanel('title', classname='fn'),
		FieldPanel('slug', classname='fn'),
		FieldPanel('all_day', classname='fn'),
		FieldPanel('start', classname='fn'),
		FieldPanel('end', classname='fn'),
		FieldPanel('location', classname='fn'),
		FieldPanel('description', classname='fn'),
    	InlinePanel('event_pricings', label="Pricing"),
  	]



class EventAttendance(models.Model):
	event = 								models.ForeignKey(Event, related_name="event_instance")
	member = 								models.ForeignKey('members.Member', related_name="member_attendance")

"""
class EventPricingLevel(models.Model):
	event = 								models.ForeignKey(Event, related_name="event_pricing")
	level = 								models.ForeignKey('members.MembershipLevel', related_name="membership_level") #avoid circular dependency
	price = 								models.DecimalField(max_digits=8, decimal_places=2)

	def __str__(self):
		return self.event.title
	
	class Meta:
		abstract = True
"""

class EventPricing(models.Model):
	event = 								models.ForeignKey(Event, related_name="event_pricing")
	level = 								models.ForeignKey('members.MembershipLevel', related_name="membership_level") #avoid circular dependency
	price = 								models.DecimalField(max_digits=8, decimal_places=2)

	def __str__(self):
		return self.event.title
	
	class Meta:
		abstract = True