# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from members.models import MembershipLevel
from events.models import Event

from wagtail.wagtailcore.models import Page

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsnippets.models import register_snippet



@register_snippet
class MembershipProduct(models.Model):
	membership_level = models.ForeignKey(MembershipLevel, related_name="membership_product")
	name = models.CharField(max_length=255)
	price = models.DecimalField(decimal_places=2, max_digits=8)
	subscription = models.BooleanField(default=False)
	membership_length = models.IntegerField(help_text="Length In Years")


	panels = [
        FieldPanel('name'),
        FieldPanel('price'),
    ]


	def __str__(self):
		return self.name


class EventProduct(models.Model):
	event = models.ForeignKey(Event, related_name="event_product")
	name = models.CharField(max_length=255)
	price = models.DecimalField(decimal_places=2, max_digits=8)


	def __str__(self):
		return self.name
