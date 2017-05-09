from rest_framework import serializers
from .models import Member, MembershipLevel, MemberAddress, MemberPurchaseHistory, MemberNote, MemberEducation
from spire.serializers import UserSerializer


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





class MemberSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.username', read_only=True, allow_blank=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True, allow_blank=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True, allow_blank=True)
    date_joined = serializers.CharField(source='user.date_joined', read_only=True, allow_blank=True)
    membership_level = serializers.CharField(source='membership_level.level', read_only=True, allow_blank=True)

    address = MemberAddressSerializer(many=False)
    education = MemberEducationSerializer(many=True)

    class Meta:
        model = Member
        fields = ('id','email','full_name','first_name','last_name','company','image','date_joined','membership_level','mobile_phone', 'work_phone', 'address', 'education')



