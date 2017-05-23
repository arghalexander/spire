import django_filters
from rest_framework import viewsets
import rest_framework_filters as filters
from .models import Member, MemberIndustry, MemberRegion, MembershipLevel, MemberProfesionalInformation

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


class MemberProfessionalInformationFilter(filters.FilterSet):
    

    class Meta:
        model = MemberProfesionalInformation
        fields ={'industry': ['exact', 'in'] }


class MemberFilter(filters.FilterSet):
    #industry = filters.RelatedFilter(MemberIndustryFilter, name='industry', queryset=MemberIndustry.objects.all())
    #professional_info = filters.RelatedFilter(MemberProfesionalInformation, name='professional_info', queryset=MemberProfesionalInformation.objects.all())
    #region = filters.RelatedFilter(MemberRegionFilter, name='region', queryset=MemberRegion.objects.all().distinct(), distinct=True)
    region__in = django_filters.filters.BaseInFilter(name='region__region',distinct=True)
    membership_level = filters.RelatedFilter(MembershipLevelFilter, name='membership_level', queryset=MembershipLevel.objects.all())

    user = filters.RelatedFilter('spire.filters.UserFilter', name='user', queryset=User.objects.all())
    
    industry = django_filters.CharFilter(name='professional_information__industry__industry', lookup_expr='exact')

    #date_joined = django_filters.IsoDateTimeFilter()
    date_joined__gte = django_filters.DateTimeFilter(name='user__date_joined', lookup_expr='gte')
    date_joined__lte = django_filters.DateTimeFilter(name='user__date_joined', lookup_expr='lte')

    grad_year__gte = django_filters.NumberFilter(name='education__grad_year', lookup_expr='gte')
    grad_year__lte = django_filters.NumberFilter(name='education__grad_year', lookup_expr='lte')

    class Meta:
        model = Member
        fields = {}
