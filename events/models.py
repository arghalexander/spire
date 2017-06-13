from __future__ import unicode_literals
from wagtail.wagtailcore.fields import RichTextField
from tinymce.models import HTMLField
from django.db import models

from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsearch import index

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from modelcluster.models import ClusterableModel
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel, InlinePanel

from django.utils.translation import ugettext as _
from wagtailgeowidget.edit_handlers import GeoPanel
from django.utils.functional import cached_property
from wagtailgeowidget.helpers import geosgeometry_str_to_struct

from django.db.models.signals import post_save
from django.dispatch import receiver







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
	address = 								models.CharField(max_length=250, blank=True, null=True)
	location = 								models.CharField(max_length=255, blank=True, null=True)
	description = 							RichTextField()


	def __str__(self):
		return self.title

	panels = [
		
		FieldPanel('status', classname='fn'),

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

# method for updating
@receiver(post_save, sender=Event)
def update_stock(sender, instance, created, **kwargs):
	from spiresite.models import EventPricing
	from members.models import MembershipLevel

	if created:
		for level in MembershipLevel.objects.all():
			pricing_level = EventPricing(event=instance,price=0.00,level=level)
			pricing_level.save()



class EventAttendance(models.Model):
	event = 								models.ForeignKey(Event, related_name="event_instance")
	member = 								models.ForeignKey('members.Member', related_name="member_attendance")


class EventPricing(models.Model):
	event = 								models.ForeignKey(Event, related_name="event_pricing")
	level = 								models.ForeignKey('members.MembershipLevel', related_name="membership_level") #avoid circular dependency
	price = 								models.DecimalField(max_digits=8, decimal_places=2)

	def __str__(self):
		return self.event.title
	
	class Meta:
		abstract = True