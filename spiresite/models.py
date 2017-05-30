from __future__ import unicode_literals

import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from events.models import Event, EventPricing

# Create your models here.
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page, PageManager, PageQuerySet
from modelcluster.models import ClusterableModel
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailadmin.edit_handlers import InlinePanel, FieldPanel, StreamFieldPanel, FieldRowPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from modelcluster.fields import ParentalKey


from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks

from wagtail.wagtailsearch import index

from .blocks import MenuItemBlock
from orderables import *



class HomePage(Page):

	sponsor_one =				 	RichTextField(blank=True)
	sponsor_one_link = 				models.URLField(blank=True)
	sponsor_two = 					RichTextField(blank=True)
	sponsor_two_link =				models.URLField(blank=True)
	sponsor_three = 				RichTextField(blank=True)
	sponsor_three_link = 			models.URLField(blank=True)

	join_image = 					models.ForeignKey(
										'wagtailimages.Image',
										null=True,
										blank=True,
										on_delete=models.SET_NULL,
										related_name='join_image'
									)
	join_content =					RichTextField(blank=True)
	join_link = 					models.URLField(blank=True)


	contact_content =				RichTextField(blank=True)
	contact_link = 					models.URLField(blank=True)


	
	content_panels = Page.content_panels + [
		InlinePanel('home_gallery', label="Gallery"),
		MultiFieldPanel([
			FieldRowPanel([
				FieldPanel('sponsor_one'),
				FieldPanel('sponsor_one_link'),
			]),
			FieldRowPanel([
				FieldPanel('sponsor_two'),
				FieldPanel('sponsor_two_link'),
			]),
			FieldRowPanel([
				FieldPanel('sponsor_three'),
				FieldPanel('sponsor_three_link'),
			]),
			
		],
		heading="Sponsors",
		classname="collapsible"
		),
		MultiFieldPanel([
			ImageChooserPanel('join_image'),
			FieldPanel('join_content'),
			FieldPanel('join_link'),
		],
		heading="Join Spire",
		classname="collapsible"
		),
		MultiFieldPanel([
			FieldPanel('contact_content'),
			FieldPanel('contact_link'),
		],
		heading="Contact Spire",
		classname="collapsible"
		)
	]

	def get_context(self, request):
		context = super(HomePage, self).get_context(request)

		# Add extra variables and return the updated context
		context['upcoming_events'] = Event.objects.filter(start__gte=datetime.datetime.now())
		context['featured_event'] = Event.objects.filter(featured=True)[0:1] #get first in list
		return context


class AboutPage(Page):
	
	heading = 						models.CharField(blank=True, max_length=255)
	
	pillar_one =				 	RichTextField(blank=True)
	pillar_two = 					RichTextField(blank=True)
	pillar_three = 					RichTextField(blank=True)
	
	page_content = 					RichTextField(blank=True)
	

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		MultiFieldPanel([
			FieldPanel('pillar_one'),
			FieldPanel('pillar_two'),
			FieldPanel('pillar_three'),
		],
		heading="Pillars",
		classname="collapsible"
		),
		FieldPanel('page_content'),
	]


class ProfessionalsPage(Page):
	pass


class SRECPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)
	event = 						models.ForeignKey(
								        'events.Event',
								        null=True,
								        blank=True,
								        on_delete=models.SET_NULL,
								        related_name='srec_event'
								    )
	page_content =				 	RichTextField(blank=True)
	

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		SnippetChooserPanel('event'),
		FieldPanel('page_content'),
		InlinePanel('srec_gallery', label="Gallery"),
		
	]


class SrecMembersPage(Page):
	page_content =				 	RichTextField(blank=True)
	

	content_panels = Page.content_panels + [
		FieldPanel('page_content'),		
	]

	def get_context(self, request):
		context = super(HomePage, self).get_context(request)

		# Add extra variables and return the updated context
		context['srec_members'] = Member.objects.filter(membership_level="SREC")
		return context



class OnCampusPage(Page):
	pass


class MembershipPage(Page):
	pass



class EventPricing(Orderable, EventPricing):
	event = ParentalKey(Event,related_name='event_pricings',on_delete=models.CASCADE,blank=False)
	ticket_quantity = models.IntegerField()

