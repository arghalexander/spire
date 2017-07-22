from __future__ import unicode_literals
from wagtail.wagtailcore.fields import RichTextField
from tinymce.models import HTMLField
from django.db import models

import datetime
from django.utils import timezone

from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsearch import index

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel, InlinePanel

from django.utils.translation import ugettext as _
from wagtailgeowidget.edit_handlers import GeoPanel
from django.utils.functional import cached_property
from wagtailgeowidget.helpers import geosgeometry_str_to_struct

from django.db.models.signals import post_save
from django.dispatch import receiver

#from spiresite.orderables import EventPricing



@register_snippet
class Event(index.Indexed,ClusterableModel):
	title =							 		models.CharField(max_length=254)
	slug = 									models.SlugField(verbose_name="Event URL",unique=True)
	featured = 								models.BooleanField(default=False)
	image = 								models.ForeignKey(
												'wagtailimages.Image',
												null=True,
												blank=True,
												on_delete=models.SET_NULL,
												related_name='event_image'
											)
	status =								models.CharField(max_length=254, choices=[('PUBLISHED','Published'),('DRAFT','Draft')], default="DRAFT")
	all_day = 								models.BooleanField()
	start = 								models.DateTimeField()
	end =									models.DateTimeField()
	capacity = 								models.IntegerField(blank=True,null=True)
	address = 								models.CharField(max_length=250)
	location = 								models.CharField(max_length=255)
	description = 							RichTextField()

	@property
	def registration_open(self):
		if self.start >= timezone.now():
			return True
		return False


	def __str__(self):
		return self.title

	def __unicode__(self):
		return u'%s' % self.title

	panels = [

		FieldPanel('status', classname='fn'),
		FieldPanel('capacity', classname='fn'),

		MultiFieldPanel([
			FieldPanel('title', classname='fn'),
			FieldPanel('slug', classname='fn'),
		],
		classname="",
		heading="Event",),

		ImageChooserPanel('image'),



		MultiFieldPanel([
			FieldPanel('all_day', classname='fn'),
			FieldRowPanel([
				FieldPanel('start', classname='fn'),
				FieldPanel('end', classname='col-3'),
			],
			)
		],
		classname="",
		heading="Date",
		),

		MultiFieldPanel([
			FieldPanel('address'),
			GeoPanel('location', address_field='address'),
		], _('Location details')),

		FieldPanel('description', classname='full'),
		InlinePanel('event_pricings', label="Pricing"),
		InlinePanel('events_products', label="Additional Products"),
	]

	search_fields = [
		index.SearchField('title', partial_match=True),
	]

	@cached_property
	def point(self):
		return geosgeometry_str_to_struct(self.location)

	@property
	def lat(self):
		return self.point['y']

	@property
	def lng(self):
		return self.point['x']


	def save(self, *args, **kwargs):
		super(Event, self).save()

"""
# method for updating
@receiver(post_save, sender=Event)
def update_stock(sender, instance, created, **kwargs):
	from spiresite.models import EventPricing
	from members.models import MembershipLevel

	if created:
		for level in MembershipLevel.objects.all():
			pricing_level = EventPricing(event=instance,event_price=0.00,level=level)
			pricing_level.save()
"""


class EventAttendance(models.Model):
	event = 								models.ForeignKey(Event, related_name="event_instance")
	member = 								models.ForeignKey('members.Member', related_name="member_attendance")
	attended = 								models.BooleanField(default=False)


class EventPricing(models.Model):
	event = 						ParentalKey(Event, related_name="event_pricings")
	level = 						models.ForeignKey('members.MembershipLevel', related_name="membership_level") #avoid circular dependency
	can_attend = 					models.BooleanField(default=False)
	event_price = 					models.DecimalField(max_digits=8, decimal_places=2)


class Product(Orderable):
	sku = models.SlugField(unique=True)
	event = ParentalKey(Event, related_name="events_products")
	name = models.CharField(max_length=255)


	CATEGORY = (
		('SPONSORSHIP','Sponsorship'),
		('GIFTS','Gifts/Students'),
		('TRIBUTE','Tribute Ads'),
	)
	category = models.CharField(max_length=50,choices=CATEGORY, default="TRIBUTE")
	price = models.DecimalField(decimal_places=2, max_digits=8)

	def __str__(self):
		return self.name
