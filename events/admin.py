from django.contrib import admin
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField

from .models import Event, EventAttendance,EventPricing
from .forms import EventAttendanceAutocompleteForm

from dal import autocomplete

#class EventPricingInline(admin.TabularInline):
#	model = EventPricing
#	extra = 0


class EventAttendanceInline(admin.TabularInline):
	model = EventAttendance
	#form = EventAttendanceAutocompleteForm
	extra = 0
	raw_id_fields = ("member",)
	autocomplete_lookup_fields = {
        'fk': ['member'],
    }


class EventPricingInline(admin.TabularInline):
	model = EventPricing
	extra = 0



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',), }
	formfield_overrides = {
		HTMLField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
	}
	inlines = [
		EventPricingInline,
		EventAttendanceInline
	]


@admin.register(EventAttendance)
class EventAttendaceAdmin(admin.ModelAdmin):
	list_display = ['event','member']
