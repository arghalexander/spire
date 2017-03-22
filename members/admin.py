from django.contrib import admin
from .models import Member, MembershipLevel




@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
	pass


@admin.register(MembershipLevel)
class MembershipLevelAdmin(admin.ModelAdmin):
	pass