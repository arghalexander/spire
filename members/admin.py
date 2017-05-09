from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *
from resources import MemberResource

class MemberEducationInline(admin.TabularInline):
	model = MemberEducation
	extra = 0


class AddressInline(admin.TabularInline):
	model = MemberAddress
	extra = 0


class NoteInline(admin.TabularInline):
	model = MemberNote
	extra = 0


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
	resource_class = MemberResource
	inlines = [
		MemberEducationInline,
		AddressInline,
		NoteInline
	]


@admin.register(MembershipLevel)
class MembershipLevelAdmin(admin.ModelAdmin):
	pass


@admin.register(MemberRegion)
class MemberRegionAdmin(admin.ModelAdmin):
	pass



@admin.register(MemberPurchaseHistory)
class MemberEventPurchaseAdmin(admin.ModelAdmin):
	pass
