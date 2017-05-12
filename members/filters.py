import django_filters
from rest_framework import viewsets
import rest_framework_filters as filters
from .models import Member, MemberIndustry, MemberRegion, MembershipLevel

from django.contrib.auth.models import User

class MemberIndustryFilter(filters.FilterSet):
    class Meta:
        model = MemberIndustry
        fields = {'industry': ['exact', 'in',]}


class MemberRegionFilter(filters.FilterSet):
    class Meta:
        model = MemberRegion
        fields = {'region': ['exact', 'in',]}


class MembershipLevelFilter(filters.FilterSet):
    class Meta:
        model = MembershipLevel
        fields = {'level': ['exact', 'in', 'startswith']}


class MemberFilter(filters.FilterSet):
    industry = filters.RelatedFilter(MemberIndustryFilter, name='industry', queryset=MemberIndustry.objects.all())
    #region = filters.RelatedFilter(MemberRegionFilter, name='region', queryset=MemberRegion.objects.all().distinct(), distinct=True)
    region__in = django_filters.filters.BaseInFilter(name='region__region',distinct=True)
    membership_level = filters.RelatedFilter(MembershipLevelFilter, name='membership_level', queryset=MembershipLevel.objects.all())

    user = filters.RelatedFilter('spire.filters.UserFilter', name='user', queryset=User.objects.all())
    
    #date_joined = django_filters.IsoDateTimeFilter()
    date_joined__gte = django_filters.DateTimeFilter(name='user__date_joined', lookup_type='gte')
    date_joined__lte = django_filters.DateTimeFilter(name='user__date_joined', lookup_type='lte')

    class Meta:
        model = Member
        fields = {}
