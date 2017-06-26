from django.contrib import admin
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField
from .models import Event, EventAttendance

#class EventPricingInline(admin.TabularInline):
#	model = EventPricing
#	extra = 0


class EventEventAttendanceInline(admin.TabularInline):
	model = EventAttendance
	extra = 0



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',), }
	formfield_overrides = {
		HTMLField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
	}
	inlines = [
		#EventPricingInline
		EventEventAttendanceInline
	]


@admin.register(EventAttendance)
class EventAttendaceAdmin(admin.ModelAdmin):
	list_display = ['event','member']
