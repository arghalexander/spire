from rest_framework import viewsets

from django.shortcuts import render
from django.http import HttpResponse,Http404

from .models import Event
from .serializers import EventSerializer


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