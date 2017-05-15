from import_export.admin import ImportExportMixin
from django.contrib import admin
from resources import UserResource
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class myUserAdmin(ImportExportModelMixin, UserAdmin):
	resource_class = UserResource


admin.site.unregister(User)
admin.site.register(User, myUserAdmin)