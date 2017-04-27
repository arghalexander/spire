from rest_framework import serializers
from django.contrib.auth.models import User, Group

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')

    class Meta:
        model = User
        fields = '__all__'