from django.db import models

from events.models import Event
from modelcluster.fields import ParentalKey
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailadmin.edit_handlers import PageChooserPanel
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel,FieldRowPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel




class HomePageGallery(Orderable):
	page = ParentalKey('spiresite.HomePage', related_name='home_gallery')
	title = models.CharField(max_length=255)
	description = models.TextField()
	learn_more_link = models.ForeignKey(
		'wagtailcore.Page',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='home_gallery_learn_more',
	)
	background = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='home_gallery_background'
	)

	panels = [
		FieldPanel('title'),
		FieldPanel('description'),
		PageChooserPanel('learn_more_link'),
		ImageChooserPanel('background'),
		
	]


class SCRECPageGallery(Orderable):
	page = ParentalKey('spiresite.SRECPage', related_name='srec_gallery')
	image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='srec_gallery_image'
	)

	panels = [
		ImageChooserPanel('image'),
	]





class LeadershipStaffGallery(Orderable):
	page = ParentalKey('spiresite.LeadershipStaffPage', related_name='leadership_gallery')
	image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='staff_gallery_image'
	)
	name = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	description = RichTextField(blank=True)

	panels = [
		ImageChooserPanel('image'),
		FieldPanel('name'),
		FieldPanel('title'),
		FieldPanel('description')
	]



class MembershipBenefits(Orderable):
	page = ParentalKey('spiresite.MembershipPage', related_name='membership_benefits')
	icon_class = models.CharField(max_length=255, help_text="Icon CSS class")
	text = models.CharField(max_length=255)

	panels = [
		FieldRowPanel([
			FieldPanel('icon_class'),
			FieldPanel('text'),
		])
	]



class AnnualReports(Orderable):
	page = ParentalKey('spiresite.AnnualReportsPage', related_name='annual_reports')
	image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='report_image'
	)
	document = models.ForeignKey(
			'wagtaildocs.Document',
			null=True,
			blank=True,
			on_delete=models.SET_NULL,
			related_name='annual_report'
		)

	panels = [
		ImageChooserPanel('image'),
		DocumentChooserPanel('document'),
	]



class FameGallery(Orderable):
	page = ParentalKey('spiresite.HallOfFameOverviewPage', related_name='fame_gallery')
	image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='fame_gallery_image'
	)

	panels = [
		ImageChooserPanel('image'),
	]


class FameSponsors(Orderable):
	page = ParentalKey('spiresite.HallOfFameOverviewPage', related_name='fame_sponsors')
	image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='fame_sponsor_image'
	)

	panels = [
		ImageChooserPanel('image'),
	]


class FameCurrentInductees(Orderable):
	page = ParentalKey('spiresite.HallOfFameInducteesPage', related_name='current_inductees')
	image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='fame_current_inductee_image'
	)
	text = RichTextField()

	panels = [
		ImageChooserPanel('image'),
		FieldPanel('text'),
	]


class FamePreviousInductees(Orderable):
	page = ParentalKey('spiresite.HallOfFameInducteesPage', related_name='previous_inductees')
	image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='fame_previous_inductee_image'
	)
	name = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	company = models.CharField(max_length=255)
	bio = RichTextField()

	panels = [
		ImageChooserPanel('image'),
		FieldPanel('name'),
		FieldPanel('title'),
		FieldPanel('company'),
		FieldPanel('bio'),
	]



class FameBanquetGallery(Orderable):
	page = ParentalKey('spiresite.HallOfFameBanquetsPage', related_name='banquet_gallery')
	
	featured_one = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='banquet_featured_one'
	)

	featured_two = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='banquet_featured_two'
	)
	
	panels = [
		ImageChooserPanel('featured_one'),
		ImageChooserPanel('featured_two'),
		InlinePanel('banquet_gallery_images', label="Gallery"),
	]


class FameBanquetGalleryImage(Orderable):
	page = models.ForeignKey(FameBanquetGallery, related_name='banquet_gallery_images')
	
	image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='banquet_gallery_image'
	)
	
	panels = [
		ImageChooserPanel('image'),
	]




class AnnualEvent(Orderable):
	page = ParentalKey('spiresite.AnnualEventsPage', related_name='annual_events') 
	event = 	models.ForeignKey(
					'events.Event',
					null=True,
					blank=True,
					on_delete=models.SET_NULL,
					related_name='annual_event_image'
				)

	panels = [
		SnippetChooserPanel('event'),
	]




