from rest_framework import serializers
from .models import *
from spire.serializers import UserSerializer
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class MemberSignupsByMonthSerilizer(serializers.Serializer):
    value = serializers.IntegerField()
    name = serializers.CharField(max_length=255)


class MemberTypesCountSerilizer(serializers.Serializer):
    value = serializers.IntegerField()
    name = serializers.CharField(max_length=255)

class MembershipLevelSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = MembershipLevel
        fields = '__all__'


class MemberEducationSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = MemberEducation
        fields = '__all__'



class MemberAddressSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = MemberAddress
        fields = '__all__'


class MemberPurchaseHistorySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = MemberPurchaseHistory
        fields = '__all__'


class MemberMembershipHistorySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = MemberMembershipHistory
        fields = '__all__'


class TagSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    slug = serializers.SlugField(read_only=True)


class MemberNoteSerializer(TaggitSerializer,serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True, allow_blank=True)
    member = serializers.CharField(read_only=True, allow_blank=True)
    tags = TagListSerializerField()

    class Meta:
        model = MemberNote
        fields = '__all__'


class MemberRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberRegion
        fields = '__all__'

class MemberIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberIndustry
        fields = '__all__'


class MemberProfesionalInformationSerializer(serializers.ModelSerializer):
    industry = serializers.CharField(source='industry.industry', read_only=True, allow_blank=True)
    industry_associations = serializers.CharField(source='industry_associations.name', read_only=True, allow_blank=True)

    class Meta:
        model = MemberProfesionalInformation
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email', read_only=True, allow_blank=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True, allow_blank=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True, allow_blank=True)
    date_joined = serializers.CharField(source='user.date_joined', read_only=True, allow_blank=True)
    membership_level = serializers.CharField(source='membership_level.level', read_only=True, allow_blank=True)
    professional_information = MemberProfesionalInformationSerializer(many=False)
  
    address = MemberAddressSerializer(many=False)
    education = MemberEducationSerializer(many=True)
    #industry = MemberIndustrySerializer(many=False)
    region = MemberRegionSerializer(many=True)


    class Meta:
        model = Member
        fields = ('id','email','full_name','preferred_name','first_name','last_name','membership_level','membership_expiration','region','image','date_joined','mobile_phone', 'work_phone','degree_string','professional_information', 'address', 'education', 'bio','facebook','linkedin','twitter',)



