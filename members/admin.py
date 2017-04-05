from django.contrib import admin
from .models import *


class MemberDegreeInline(admin.TabularInline):
	model = MemberDegree
	extra = 0


class AddressInline(admin.TabularInline):
	model = MemberAddress
	extra = 0


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
	inlines = [
		MemberDegreeInline,
		AddressInline,
	]


@admin.register(MembershipLevel)
class MembershipLevelAdmin(admin.ModelAdmin):
	pass


@admin.register(MemberRegion)
class MemberRegionAdmin(admin.ModelAdmin):
	pass



@admin.register(MemberEventPurchase)
class MemberEventPurchaseAdmin(admin.ModelAdmin):
	pass
