from __future__ import unicode_literals

import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from events.models import Event, EventPricing
from members.models import Member 
from products.models import MembershipProduct

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

from .blocks import *
from orderables import *
from theme_settings import *



class HomePage(Page):

	featured_event = 				models.ForeignKey(
										'events.Event',
										null=True,
										blank=True,
										on_delete=models.SET_NULL,
										related_name='featured_event'
									)

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
		SnippetChooserPanel('featured_event'),
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
		#context['featured_event'] = Event.objects.filter(featured=True)[0:1] #get first in list
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
	gallery_caption = 				models.CharField(blank=True, max_length=255)

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		SnippetChooserPanel('event'),
		FieldPanel('page_content'),
		FieldPanel('gallery_caption'),
		InlinePanel('srec_gallery', label="Gallery"),
		
	]


class SrecMembersPage(Page):
	page_content =				 	RichTextField(blank=True)
	heading = 						models.CharField(blank=True, max_length=255)

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		FieldPanel('page_content'),
		
	]

	def get_context(self, request):
		context = super(SrecMembersPage, self).get_context(request)

		context['srec_members'] = Member.objects.filter(membership_level__slug="srec")
		return context




class SrecConferencePage(Page):
	heading = 						models.CharField(blank=True, max_length=255)

	body =							 StreamField([
										('text_image', ImageTextBlock()),
									])

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		StreamFieldPanel('body')
	]



class MembershipPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)
	description = 					models.TextField(blank=True)
	
	full_membership = 				models.TextField(blank=True)
	
	full_membership_yearly =    	models.ForeignKey(
										'products.MembershipProduct',
										null=True,
										blank=True,
										on_delete=models.SET_NULL,
										related_name='product_full_year'
									)
	full_membership_5_years =    	models.ForeignKey(
										'products.MembershipProduct',
										null=True,
										blank=True,
										on_delete=models.SET_NULL,
										related_name='product_full_5_years'
									)
	
	full_young_membership = 		models.TextField(blank=True)
	full_young_yearly = 			models.ForeignKey(
										'products.MembershipProduct',
										null=True,
										blank=True,
										on_delete=models.SET_NULL,
										related_name='product_full_young'
									)


	full_friends_membership = 		models.TextField(blank=True)
	full_friends_yearly = 			models.ForeignKey(
										'products.MembershipProduct',
										null=True,
										blank=True,
										on_delete=models.SET_NULL,
										related_name='product_full_friends'
									)


	guest_membership = 				models.TextField(blank=True)
	guest_yearly = 					models.ForeignKey(
										'products.MembershipProduct',
										null=True,
										blank=True,
										on_delete=models.SET_NULL,
										related_name='product_guest'
									)
	student_membership = 			models.TextField(blank=True)
	student_yearly = 				models.ForeignKey(
										'products.MembershipProduct',
										null=True,
										blank=True,
										on_delete=models.SET_NULL,
										related_name='product_student'
									)			

	people_image = 					models.ForeignKey(
										'wagtailimages.Image',
										null=True,
										blank=True,
										on_delete=models.SET_NULL,
										related_name='people_image'
									)

	people_review_one = 			RichTextField(blank=True)
	people_review_two = 			RichTextField(blank=True)


	member_closing = 				RichTextField(blank=True)

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		FieldPanel('description'),
		MultiFieldPanel([
			FieldPanel('full_membership'),
			SnippetChooserPanel('full_membership_yearly'),
			SnippetChooserPanel('full_membership_5_years'),
		],
		heading="Full Membership",
		classname="collapsible"
		),
		MultiFieldPanel([

			FieldPanel('full_young_membership'),
			SnippetChooserPanel('full_young_yearly'),
		],
		heading="Full Young Membership",
		classname="collapsible"
		),
		MultiFieldPanel([

			FieldPanel('full_friends_membership'),
			SnippetChooserPanel('full_friends_yearly'),
		],
		heading="Full Friend Membership",
		classname="collapsible"
		),
		MultiFieldPanel([

			FieldPanel('guest_membership'),
			SnippetChooserPanel('guest_yearly'),
		],
		heading="Guest Membership",
		classname="collapsible"
		),
		MultiFieldPanel([

			FieldPanel('student_membership'),
			SnippetChooserPanel('student_yearly'),
		],
		heading="Student Membership",
		classname="collapsible"
		),

		InlinePanel('membership_benefits', label="Membership Benefits"),
		ImageChooserPanel('people_image'),
		FieldPanel('people_review_one'),
		FieldPanel('people_review_two'),
		FieldPanel('member_closing'),
	]
	





class MemberDirectoryPage(Page):
	
	heading = 						models.CharField(blank=True, max_length=255)
	
	

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
	]







class LeadershipOverviewPage(Page):
	
	heading = 						models.CharField(blank=True, max_length=255)
	body = 							RichTextField(blank=True)

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		FieldPanel('body')
	]




class LeadershipStaffPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)

	#body =							 StreamField([
									#	('text_image', ImageTextBlock()),
								#	])

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		InlinePanel('leadership_gallery', label="Staff"),
	]


class LeadershipRegionalLeadersPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)

	body =							 StreamField([
										('region', blocks.CharBlock(required=True)),
										('leader', blocks.ListBlock(LeaderBlock()))
									])

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		StreamFieldPanel('body')
	]





class StandardLeadershipPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)

	body =							 StreamField([
										('text', blocks.RichTextBlock()),
									])

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		StreamFieldPanel('body')
	]



class StandardPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)

	body =							 StreamField([
										('text', blocks.RichTextBlock()),
									])

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		StreamFieldPanel('body')
	]







class EventPricing(Orderable, EventPricing):
	event = ParentalKey(Event,related_name='event_pricings',on_delete=models.CASCADE,blank=False)
	ticket_quantity = models.IntegerField()


