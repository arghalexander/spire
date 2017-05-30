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
	location = 								models.TextField()
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
		
	
		FieldPanel('location', classname='fn'),
		FieldPanel('description', classname='full'),
		InlinePanel('event_pricings', label="Pricing"),
	]

	search_fields = [
		index.SearchField('title', partial_match=True),
	]


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