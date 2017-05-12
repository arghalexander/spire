import pytz
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse,Http404
from rest_framework.decorators import detail_route, list_route

from .models import Event, EventAttendance
from .serializers import *
from members.serializers import MemberSerializer  
from members.models import Member  

from django.db.models import Count, Value, F
from django.db.models.functions import TruncMonth

def index(request):
    """
    Events Index Page
    """
    events = Event.objects.all()
    return render(request, 'events/event_detail.html', {'events': events})


def detail(request,slug):
    try:
        event = Event.objects.get(slug=slug)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    return render(request, 'events/event_detail.html', {'event': event})



class EventViewSet(viewsets.ModelViewSet):
    """
        Event Viewset for api
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @detail_route(methods=['get'])
    def get_attendance(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        #members = Members.objects.filter()
        members = Member.objects.filter(member_attendance__event=event)
        
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    
    @list_route()
    def get_attendance_by_month_count(self, request):
        members = EventAttendance.objects.annotate(name=TruncMonth('event__start')) \
            .values('name')  \
            .annotate(value=Count('member__id'))  \
            .values('name', 'value') 
            
        serializer = AggregateSerilizer(members, many=True)
        return Response(serializer.data)


class EventAttendanceViewSet(viewsets.ModelViewSet):
    """
        Event Attendance Viewset for api
    """
    queryset = EventAttendance.objects.all()
    serializer_class = EventAttendanceSerializer