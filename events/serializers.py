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
    event = EventSerializer(many=False)

    class Meta:
        model = EventAttendance
        fields = ('id','event_title','event_date','event') 