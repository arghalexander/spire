from django.db import models


from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import PageChooserPanel
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel,FieldRowPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


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
    company = models.CharField(max_length=255)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('name'),
        FieldPanel('title'),
        FieldPanel('company'),
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