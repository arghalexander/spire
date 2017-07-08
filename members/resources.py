from import_export import resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from import_export import fields

from django.contrib.auth.models import User

from .models import Member, MembershipLevel, MemberRegion

class MemberResource(resources.ModelResource):
    user = fields.Field( column_name='user',attribute='user',widget=ForeignKeyWidget(User, 'username'))
    membership_level = fields.Field( column_name='membership_level',attribute='membership_level',widget=ForeignKeyWidget(MembershipLevel, 'level'))
    region = fields.Field(column_name='region',widget=ManyToManyWidget(MemberRegion,field="region"))

    class Meta:
        model = Member    
        fields = ('id','user','work_phone','mobile_phone', 'membership_level', 'membership_expiration')