from wagtail.contrib.settings.models import BaseSetting, register_setting
from django.db import models

from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList


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