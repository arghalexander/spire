from django.contrib import admin
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField
from .models import Event, EventPricingLevel, EventAttendance

class EventPricingInline(admin.TabularInline):
	model = EventPricingLevel
	extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',), }
	formfield_overrides = {
		HTMLField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
	}
	inlines = [
		EventPricingInline
	]


@admin.register(EventAttendance)
class EventAdmin(admin.ModelAdmin):
	pass