from __future__ import unicode_literals

from django.db import models

from events.models import Event

# Create your models here.
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page, PageManager, PageQuerySet


"""
class EventsIndexPage(Page):

    def get_context(self, request):
        context = super(EventsIndexPage, self).get_context(request)

        # Add extra variables and return the updated context
        context['events'] = Event.objects.all()
        return context


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
    """