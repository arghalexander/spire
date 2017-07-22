from __future__ import unicode_literals

import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from events.models import Event, EventPricing
from members.models import Member
from products.models import MembershipProduct
from wagtail.wagtailcore.models import Page
from django.contrib import messages

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

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from wagtail.wagtailcore.fields import StreamField
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailcore import blocks

from wagtail.wagtailsearch import index

from .blocks import *
from orderables import *
from theme_settings import *
from .model_admin import *

from django.conf import settings
from spire.decorators import member_access



def is_full_member(request):
	if request.user.is_authenticated():
		member = Member.objects.get(user=request.user)
		access_level = member.membership_level.access_level
		if access_level > 0:
			return True
		return False


class HomePage(Page):

	featured_event = 				models.ForeignKey(
										'events.Event',
										null=True,
										blank=False,
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
		context['upcoming_events'] = Event.objects.filter(start__gte=datetime.datetime.now(), status="PUBLISHED")
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

		context['srec_members'] = Member.objects.filter(membership_level__slug="srec").order_by('user__last_name')
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
	member_header_image	=			models.ForeignKey(
										'wagtailimages.Image',
										null=True,
										blank=True,
										on_delete=models.SET_NULL,
										related_name='member_header_image'
									)


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
	#guest_yearly = 					models.ForeignKey(
	#									'products.MembershipProduct',
	#									null=True,
	#									blank=True,
	#									on_delete=models.SET_NULL,
	#									related_name='product_guest'
	#								)
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
		ImageChooserPanel('member_header_image'),
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
			#SnippetChooserPanel('guest_yearly'),
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


	#limit access to full members
	def serve(self,request):

		if not is_full_member(request):
			messages.warning(request, 'You do not have permission to view that page, please upgrade your membership to access.')
			return redirect('/members-directory/membership/')

		return super(MemberDirectoryPage, self).serve(request)



class ResumeBookPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)

	body =							 StreamField([
										('text', blocks.RichTextBlock()),
										('button', ButtonBlock()),
										('people_list', blocks.ListBlock(PersonBlock(), template='spiresite/blocks/people_list.html', icon="group"))
									])

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		StreamFieldPanel('body')
	]


	template = 'standard_page.html'


	#limit access to full members
	def serve(self,request):

		if not is_full_member(request):
			messages.warning(request, 'You do not have permission to view that page, please upgrade your membership to access.')
			return redirect('/members-directory/membership/')

		return super(ResumeBookPage, self).serve(request)





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
										('table', TableBlock()),
										('three_columnn_block', ThreeColumnBlock()),

									])

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		StreamFieldPanel('body')
	]



class StandardPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)

	body =							 StreamField([
										('text', blocks.RichTextBlock()),
										('button', ButtonBlock()),
										('people_list', blocks.ListBlock(PersonBlock(), template='spiresite/blocks/people_list.html', icon="group")),
										('redirect', RedirectBlock()),
										('REAL_page', REALPageBlock()),
									])

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		StreamFieldPanel('body')
	]




class AnnualReportsPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		InlinePanel('annual_reports', label="Reports"),
	]



class HallOfFameStandardPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)

	body =							 StreamField([
										('text', blocks.RichTextBlock()),
										('table', TableBlock()),
										('two_columnn_block', TwoColumnBlock()),
										('three_columnn_block', ThreeColumnBlock())
									])

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		StreamFieldPanel('body')
	]





class HallOfFameOverviewPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)
	event_heading =					models.CharField(blank=True, max_length=255)
	
	event_text =					RichTextField(blank=True)
	button_one_url =				models.URLField(blank=True)
	button_one_text = 				models.CharField(blank=True, max_length=255)
	button_two_url =				models.URLField(blank=True)
	button_two_text = 				models.CharField(blank=True, max_length=255)

	page_content =				 	RichTextField(blank=True)
	gallery_caption = 				models.CharField(blank=True, max_length=255)
	sponsors_caption = 				models.CharField(blank=True, max_length=255)


	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		FieldPanel('event_heading'),

		MultiFieldPanel(
		[
			FieldPanel('event_text'),
			FieldPanel('button_one_url'),
			FieldPanel('button_one_text'),
			FieldPanel('button_two_url'),
			FieldPanel('button_two_text'),
		],
		heading="Event Box",
		classname=""
		),


		FieldPanel('page_content'),
		FieldPanel('gallery_caption'),
		InlinePanel('fame_gallery', label="Gallery"),
		FieldPanel('sponsors_caption'),
		InlinePanel('fame_sponsors', label="Sponsors"),
	]


class HallOfFameInducteesPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)


	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		InlinePanel('current_inductees', label="Current Inductees"),
		InlinePanel('previous_inductees', label="Previous Inductees"),
	]


class HallOfFameBanquetsPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)

	body =							 StreamField([
										('text', blocks.RichTextBlock()),
										('image_block',TwoImageBlock()),
										('gallery_block',GalleryBlock()),
									], null=True)

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		StreamFieldPanel('body')
	]




class ContactPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)
	contact_box =					RichTextField()

	questions = 					RichTextField()

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		FieldPanel('contact_box'),
		FieldPanel('questions')
	]


	def serve(self, request):
		from .forms import ContactForm
		if request.method == 'POST':
			form = ContactForm(request.POST)

			if form.is_valid():

				
				theme_settings = ThemeSettings.for_site(request.site)


				msg = EmailMultiAlternatives(
					subject="Contact Form Submission",
					body= "First Name: " + form.cleaned_data['first_name'] + '\nLast Name: ' + form.cleaned_data['last_name'] + '\nPhone: '+ form.cleaned_data['phone'] + '\nmessage: ' + form.cleaned_data['message'],
					from_email="Contact Form <Contact-us@mg.spirestandford.org>",
					to=[theme_settings.contact_form_email,],
					reply_to=[form.cleaned_data['email']])

				msg.send()

				return render(request, 'spiresite/contact_page.html', {
					'page': self,
				})
			else:
				return render(request, self.template, {
					'page': self,
					'form': form
				})

		form = ContactForm()

		return render(request, self.template, {
			'page': self,
			'form': form
		})




class EventsPage(Page):
	page_content =				 	RichTextField(blank=True)
	heading = 						models.CharField(blank=True, max_length=255)

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		FieldPanel('page_content'),

	]

	def get_context(self, request):
		context = super(EventsPage, self).get_context(request)

		context['upcoming_events'] = Event.objects.filter(start__gte=datetime.datetime.now(),status="PUBLISHED").order_by('start')
		return context



class PastEventsPage(Page):
	page_content =				 	RichTextField(blank=True)
	heading = 						models.CharField(blank=True, max_length=255)

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		FieldPanel('page_content'),

	]

	def get_context(self, request):
		context = super(PastEventsPage, self).get_context(request)

		context['past_events'] = Event.objects.filter(start__lt=datetime.datetime.now()).order_by('-start')[:25]
		return context



class AnnualEventsPage(Page):
	page_content =				 	RichTextField(blank=True)
	heading = 						models.CharField(blank=True, max_length=255)


	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		FieldPanel('page_content'),
		InlinePanel('annual_events', label="Annual Events"),
	]




class JobBoardPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)
	page_content =				 	RichTextField(blank=True)

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		FieldPanel('page_content'),
	]


	def get_context(self, request):
		context = super(JobBoardPage, self).get_context(request)
		#context['jobs'] = self.get_children().live()
		context['jobs'] = Job.objects.all()
		return context


	def serve(self, request):
		if not request.user.is_authenticated:
			return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

		return super(JobBoardPage, self).serve(request)



class JobPage(Page):
	heading = 						models.CharField(blank=True, max_length=255)
	job_type = 						models.CharField(blank=True, max_length=255)
	location = 						models.CharField(blank=True, max_length=255)
	organization =					models.CharField(blank=True, max_length=255)
	page_content =				 	RichTextField(blank=True)
	date = 							models.DateField("Post date")

	content_panels = Page.content_panels + [
		FieldPanel('heading'),

		MultiFieldPanel(
		[
			FieldPanel('date'),
			FieldPanel('job_type'),
			FieldPanel('location'),
			FieldPanel('organization'),
		],
		heading="Job Info",
		classname="collapsible"
		),

		FieldPanel('page_content'),
	]

	def serve(self, request):
		if not request.user.is_authenticated:
			return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
		return super(JobPage, self).serve(request)






class LinkPage(Page):
	page =				 			models.ForeignKey(
									'wagtailcore.Page',
									null=True,
									blank=True,
									on_delete=models.SET_NULL,
									related_name='link_page_link',
								)

	content_panels = Page.content_panels + [
		PageChooserPanel('page'),
	]
