from rest_framework import serializers
from .models import Member, MembershipLevel, MemberAddress
from spire.serializers import UserSerializer



class MemberSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True, allow_blank=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True, allow_blank=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True, allow_blank=True)
    date_joined = serializers.CharField(source='user.date_joined', read_only=True, allow_blank=True)
    membership_level = serializers.CharField(source='membership_level.level', read_only=True, allow_blank=True)

    class Meta:
        model = Member
        fields = ('id','username','first_name','last_name', 'company','date_joined','membership_level','cell_phone', 'work_phone')



class MembershipLevelSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = MembershipLevel
        fields = '__all__'



class MemberAddressSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = MemberAddress
        fields = '__all__'