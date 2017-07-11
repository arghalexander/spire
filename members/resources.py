from import_export import resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from import_export import fields

from django.contrib.auth.models import User

from .models import Member, MembershipLevel, MemberRegion, MemberAddress

class MemberResource(resources.ModelResource):
	user = fields.Field( column_name='user',attribute='user',widget=ForeignKeyWidget(User, 'username'))
	membership_level = fields.Field( column_name='membership_level',attribute='membership_level',widget=ForeignKeyWidget(MembershipLevel, 'level'))
	#member_regions = fields.Field(column_name='member_regions',attribute='member_regions',widget=ManyToManyWidget(MemberRegion,'region'))

	class Meta:
		model = Member
		import_id_fields = ('user',)
		fields = ('id','user','work_phone','mobile_phone', 'membership_level', 'membership_expiration', 'region')



class MemberAddressResource(resources.ModelResource):
	member = fields.Field( column_name='member',attribute='member',widget=ForeignKeyWidget(Member, 'user'))

	class Meta:
		model = MemberAddress
		import_id_fields = ('member',)
		fields = ('member','address_line_one', 'address_line_two', 'city', 'state', 'zip_code', 'country')
