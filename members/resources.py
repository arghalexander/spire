from import_export import resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from import_export import fields

from django.contrib.auth.models import User

from .models import Member, MembershipLevel, MemberRegion, MemberAddress, MemberProfesionalInformation, MemberEducation, MemberIndustry

class MemberResource(resources.ModelResource):
	user = fields.Field( column_name='user',attribute='user',widget=ForeignKeyWidget(User, 'username'))
	membership_level = fields.Field( column_name='membership_level',attribute='membership_level',widget=ForeignKeyWidget(MembershipLevel, 'level'))
	#member_regions = fields.Field(column_name='member_regions',attribute='member_regions',widget=ManyToManyWidget(MemberRegion,'region'))

	class Meta:
		model = Member
		#import_id_fields = ('user',)
		fields = ('id','user','work_phone','mobile_phone', 'membership_level', 'membership_expiration', 'region')


class UserForeignKeyWidget(ForeignKeyWidget):
    def get_queryset(self, value, row):
        return self.model.objects.filter(
            user__username__iexact=row["member"],
        )


class MemberAddressResource(resources.ModelResource):
	member = fields.Field( column_name='member',attribute='member',widget=ForeignKeyWidget(Member, 'id'))

	class Meta:
		model = MemberAddress
		import_id_fields = ('member',)
		fields = ('member','address_line_one', 'address_line_two', 'city', 'state', 'zip_code', 'country')


class MemberEducationResource(resources.ModelResource):
	member = fields.Field( column_name='member',attribute='member',widget=ForeignKeyWidget(Member, 'id'))

	class Meta:
		model = MemberEducation
		fields = ('id','member','degree', 'program', 'grad_year')




class MemberProfesionalInformationResource(resources.ModelResource):
	member = fields.Field( column_name='member',attribute='member',widget=ForeignKeyWidget(Member, 'id'))
	industry = fields.Field( column_name='industry',attribute='industry',widget=ForeignKeyWidget(MemberIndustry, 'industry'))

	class Meta:
		model = MemberProfesionalInformation
		import_id_fields = ('member',)
		fields = ('member','title', 'company', 'industry')
