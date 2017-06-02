from wagtail.contrib.settings.models import BaseSetting, register_setting
from django.db import models


@register_setting(icon='link')
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Your Facebook page URL')
    instagram = models.CharField(
        max_length=255, help_text='Your Instagram username, without the @')
    twitter = models.URLField(
        help_text='Your twitter page URL')
    youtube = models.URLField(
        help_text='Your YouTube channel or user account URL')