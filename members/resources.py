from import_export import resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from import_export import fields

from django.contrib.auth.models import User

from .models import Member, MembershipLevel, MemberRegion

class MemberResource(resources.ModelResource):
	user = fields.Field( column_name='user',attribute='user',widget=ForeignKeyWidget(User, 'username'))
	membership_level = fields.Field( column_name='membership_level',attribute='membership_level',widget=ForeignKeyWidget(MembershipLevel, 'level'))
	#member_regions = fields.Field(column_name='member_regions',attribute='member_regions',widget=ManyToManyWidget(MemberRegion,'region'))

	class Meta:
		model = Member    
		fields = ('id','user','work_phone','mobile_phone', 'membership_level', 'membership_expiration', 'member_regions')


	#def dehydrate_region(self, obj):
	#	if obj.id:
	#		return obj.region()

	#def dehydrate_tags(self, book):
	#	return ','.join([tag.name for tag in MemberRegion.objects.all()])