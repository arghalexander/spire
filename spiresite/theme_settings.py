from wagtail.contrib.settings.models import BaseSetting, register_setting
from django.db import models
from wagtail.wagtailadmin.edit_handlers import InlinePanel, FieldPanel, StreamFieldPanel, FieldRowPanel
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList
from wagtail.wagtailcore.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailcore.fields import RichTextField

@register_setting(icon='link')
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Your Facebook page URL')
    instagram = models.CharField(
        max_length=255, help_text='Your Instagram url')
    twitter = models.URLField(
        help_text='Your twitter page URL')
    linkedin = models.URLField(
        help_text='Your Linkedin Profile URL')



@register_setting(icon='cog')
class ThemeSettings(BaseSetting):
    contact_form_email = models.EmailField(max_length=255, help_text='Address that contact form submissions will be sent to')
    contact_form_message = models.CharField(max_length=255)

    footer = RichTextField(blank=True)



class CoreSponsors(Orderable):
    setting = models.ForeignKey(ThemeSettings, related_name='core_sponsors')
    title =  models.CharField(max_length=255)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='sponsor_logo'
    )

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('image'),
    ]

