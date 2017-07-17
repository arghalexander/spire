from wagtail.contrib.modeladmin.options import (
	ModelAdmin, modeladmin_register)
from django.contrib.auth.models import User
from django.db import models
from wagtail.wagtailcore.fields import RichTextField


class Job(models.Model):
	title = 						models.CharField(blank=False, max_length=255)

	JOB_TYPES= (
		('CONTRACT', 'Contract'),
		('FULLTIME', 'Full Time'),
		('PARTTIME', 'Part Time'),
		('INTERNSHIP', 'Internship'),
	)

	job_type = 						models.CharField(blank=False, max_length=255)
	location = 						models.CharField(blank=False, max_length=255)
	organization =					models.CharField(blank=False, max_length=255)
	description =				 	RichTextField(blank=False)
	website =                       models.URLField(max_length=200)
	start_date =					models.DateField(blank=True, null=True)
	expiration_date =               models.DateField(blank=True, null=True)
	posted_date = 					models.DateField(auto_now=True)
	user = 							models.ForeignKey(User)

class JobPageModelAdmin(ModelAdmin):
	model = Job
	menu_label = 'Jobs'  # ditch this to use verbose_name_plural from model
	menu_icon = 'site'  # change as required
	menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
	add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
	exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
	list_display = ('title', 'job_type', 'location', 'organization', 'posted_date')
	search_fields = ('title',)

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(JobPageModelAdmin)
