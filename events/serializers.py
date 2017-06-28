from rest_framework import serializers
from .models import Event, EventAttendance, EventPricing
from django_extensions.admin import ForeignKeyAutocompleteAdmin


class AggregateSerilizer(serializers.Serializer):
    value = serializers.IntegerField()
    name = serializers.CharField(max_length=255)


class EventPricingSerializer(serializers.ModelSerializer):
     class Meta:
        model = EventPricing
        fields = '__all__'



class EventSerializer(serializers.ModelSerializer):
    event_pricings = EventPricingSerializer(many=True)

    class Meta:
        model = Event
        fields = '__all__'



class EventMemberListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = EventAttendance
        fields = ('id',) 



class EventAttendanceSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(source='event.title', read_only=True, allow_blank=True)
    event_date = serializers.DateTimeField(source='event.start', read_only=True)
    #event = EventSerializer(many=False)

    email = serializers.EmailField(source='member.user.email',read_only=True)
    first_name = serializers.CharField(source='member.user.first_name',read_only=True, allow_blank=True)
    last_name = serializers.CharField(source='member.user.last_name',read_only=True, allow_blank=True)
    degree_string = serializers.CharField(source='member.degree_string',read_only=True, allow_blank=True)
    company = serializers.CharField(source='member.professional_information.company',read_only=True, allow_blank=True)
    membership_level = serializers.CharField(source='member.membership_level',read_only=True, allow_blank=True)

    class Meta:
        model = EventAttendance
        fields = ('id','event_title','event_date','email','first_name','last_name','degree_string','company', 'attended') 