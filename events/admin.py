from django.contrib import admin
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',), }
	formfield_overrides = {
		HTMLField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
	}
