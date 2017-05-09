from rest_framework import serializers
from .models import Event, EventAttendance




class EventSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Event
        fields = '__all__'



class EventAttendanceSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(source='event.title', read_only=True, allow_blank=True)
    event_date = serializers.DateTimeField(source='event.start', read_only=True)
    event = EventSerializer(many=False)

    class Meta:
        model = EventAttendance
        fields = ('id','event_title','event_date','event') 