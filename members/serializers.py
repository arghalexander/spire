from rest_framework import serializers
from .models import *
from spire.serializers import UserSerializer


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


class MemberNoteSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True, allow_blank=True)
    member = serializers.CharField(read_only=True, allow_blank=True)

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


class MemberProffesionalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberProffesionalInformation
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.username', read_only=True, allow_blank=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True, allow_blank=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True, allow_blank=True)
    date_joined = serializers.CharField(source='user.date_joined', read_only=True, allow_blank=True)
    membership_level = serializers.CharField(source='membership_level.level', read_only=True, allow_blank=True)
    #industry = serializers.CharField(source='industry.industry', read_only=True, allow_blank=True)
    professional_information = MemberProffesionalInformationSerializer(many=False)

    address = MemberAddressSerializer(many=False)
    education = MemberEducationSerializer(many=True)
    #industry = MemberIndustrySerializer(many=False)
    region = MemberRegionSerializer(many=True)

    class Meta:
        model = Member
        fields = ('id','email','full_name','preferred_name','first_name','last_name','region','image','date_joined','membership_level','mobile_phone', 'work_phone','professional_information', 'address', 'education', 'bio')



