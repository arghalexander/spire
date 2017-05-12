import django_filters
import rest_framework_filters as filters
from django.contrib.auth.models import User


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'date_joined': ['exact', 'gt','lt','gte','lte','contains'],
            'email': ['exact',],
            }


