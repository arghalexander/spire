from django.db import models
from wagtail.contrib.modeladmin.options import (
	ModelAdmin, ModelAdminGroup, modeladmin_register)
from modelcluster.fields import ParentalKey
from django.contrib import admin
from events.models import Event, EventPricing
from modelcluster.models import ClusterableModel

from wagtail.contrib.modeladmin.helpers import AdminURLHelper
from wagtail.contrib.modeladmin.helpers import PageButtonHelper
from wagtail.contrib.modeladmin.helpers import ButtonHelper
from wagtail.wagtailcore.models import Orderable

from django.contrib.admin.utils import quote
from django.utils.encoding import force_text
from django.utils.functional import cached_property
from django.utils.http import urlquote
from django.utils.translation import ugettext as _

from django.utils.html import format_html
from django.contrib.staticfiles.templatetags.staticfiles import static

from wagtail.wagtailcore import hooks


class EventModelAdmin(ModelAdmin):
	model = Event
	menu_label = 'Events'  # ditch this to use verbose_name_plural from model
	menu_icon = 'date'  # change as required
	menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
	add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
	exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
	list_display = ('title','start','end','status')
	list_filter = ('start','status')
	search_fields = ('title',)

modeladmin_register(EventModelAdmin)


@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static('css/wagtail/theme.css'))