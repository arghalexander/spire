from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export import fields
from django.contrib.auth.models import User


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id','email','first_name','last_name','date_joined')