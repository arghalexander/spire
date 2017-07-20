from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export import fields
from django.contrib.auth.models import User
from import_export.widgets import DateWidget, DateTimeWidget

class UserResource(resources.ModelResource):
    date_joined = fields.Field(attribute='date_joined', column_name="date_joined", widget=DateTimeWidget())

    class Meta:
        model = User
        import_id_fields = ('username',)
        fields = ('first_name','last_name','username','email','date_joined')
        #widgets = {
        #    'date_joined': {'format': "%Y-%m-%d"},
        #}