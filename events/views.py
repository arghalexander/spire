from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Event

# Create your views here.
def detail(request,slug):
    try:
        event = Event.objects.get(slug=slug)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    return render(request, 'events/event_detail.html', {'event': event})
