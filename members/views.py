import django_filters

from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import detail_route, list_route
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView

from registration import signals

from .forms import MemberForm, MemberAddressForm, MemberEducationForm
from .models import Member, MemberAddress, MembershipLevel, MemberPurchaseHistory, MemberNote
from .serializers import MembershipLevelSerializer, MemberAddressSerializer,  MemberSerializer, MemberPurchaseHistorySerializer, MemberNoteSerializer
from .pagination import StandardResultsSetPagination


from django.views.generic.edit import FormView


from events.models import EventAttendance
from events.serializers import EventAttendanceSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'company')

    @detail_route(methods=['get'])
    def get_event_attendance(self, request, pk):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        events = EventAttendance.objects.filter(member=member)
        serializer = EventAttendanceSerializer(events, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get', 'post'])
    def member_notes(self, request, pk):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


        if request.method == 'GET':
            notes = MemberNote.objects.filter(member=member)
            serializer = MemberNoteSerializer(notes, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = MemberNoteSerializer(data=request.data)
            if serializer.is_valid():

                #TODO change user back to request user, set to this becuase anonymous users are not allowed
                serializer.save(member=member, user_id=1)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    @detail_route(methods=['get'])
    def get_purchase_history(self, request, pk):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        purchases = MemberPurchaseHistory.objects.filter(member=member)
        serializer = MemberPurchaseHistorySerializer(purchases, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def member_event_attendance(request, pk):
    try:
        member = Memebrs.objects.get(pk=pk)
    except Member.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    events = Events.objects.filter(member=member)
    serializer = EventAttendanceSerializer(events)

    return Response(serializer)


class MembershipLevelViewSet(viewsets.ModelViewSet):
    queryset = MembershipLevel.objects.all()
    serializer_class = MembershipLevelSerializer


class MemberNoteViewSet(viewsets.ModelViewSet):
    queryset = MemberNote.objects.all()
    serializer_class = MemberNoteSerializer


class MemberAddressViewSet(viewsets.ModelViewSet):
    queryset = MemberAddress.objects.all()
    serializer_class = MemberAddressSerializer




def index(request):
    try:
        member = Member.objects.get(user=request.user)
    except Member.DoesNotExist:
        return redirect('members:create-member')

    return render(request, 'members/index.html')



def create_member(request):

    #if member already created go to member edit
    if(Member.objects.filter(user=request.user).count() > 0):
        return redirect('members:edit-member-view')

    if request.method == 'POST':
      
        post_text = request.POST.get('the_post')

        if(address_form.is_valid()):
            return HttpResponseRedirect('/thanks/')
    else:
        address_form =  MemberAddressForm()

    return render(request, 'members/create_member.html', {
        'address_form': address_form,
        })


def create_member_address(request):

    #if member already created go to member edit
    if(Member.objects.filter(user=request.user).count() > 0):
        return redirect('members:edit-member-view')

    if request.method == 'POST':

        post_text = request.POST.get('the_post')

        if(address_form.is_valid()):
            return HttpResponseRedirect('/thanks/')
    else:
        address_form =  MemberAddressForm()

    return render(request, 'members/create_address_form.html', {
        'address_form': address_form,
        })

def create_member_info(request):

    #if member already created go to member edit
    if(Member.objects.filter(user=request.user).count() > 0):
        return redirect('members:edit-member-view')
    
    if request.method == 'POST':
        info_form = MemberForm(request.POST)
        if(address_form.is_valid()):
            return HttpResponseRedirect('/thanks/')
    else:
        info_form = MemberForm()  

    return render(request, 'members/create_info_form.html', {
        'info_form': info_form,
        })


def edit_member(request):

  
    return render(request, 'members/edit-member.html')



class CreateMemberView(CreateView):
    model = Member
    template_name = 'members/member_create_form.html'
    fields = [
        'preferred_name',
        'phone_preferred',
        'image',
        'bio',
        ]
