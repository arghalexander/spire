import django_filters
import datetime 
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import detail_route, list_route
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView
from django.db.models import Count, Value, F
from django.db.models.functions import TruncMonth

from registration import signals

from .forms import MemberForm, MemberAddressForm, MemberEducationForm, MemberUserForm
from .models import *
from .serializers import *
from .pagination import StandardResultsSetPagination
from filters import MemberFilter

from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt

from events.models import EventAttendance
from events.serializers import EventAttendanceSerializer
from django.forms import formset_factory


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter)
    filter_class = MemberFilter
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'professional_information__company')
    ordering_fields = ('user__email','user__first_name','user__last_name')

    @detail_route(methods=['get'])
    def get_event_attendance(self, request, pk):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        events = EventAttendance.objects.filter(member=member)
        serializer = EventAttendanceSerializer(events, many=True)
        return Response(serializer.data)

    @list_route()
    def get_signups_by_range_month_count(self, request):
        last_year = datetime.datetime.now() - datetime.timedelta(days=1*30)
        members = Member.objects.filter(user__date_joined__gte=last_year) \
            .annotate(name=TruncMonth('user__date_joined')) \
            .values('name')  \
            .annotate(value=Count('id'))  \
            .values('name', 'value') 

        serializer = MemberSignupsByMonthSerilizer(members, many=True)
        return Response(serializer.data)
    
    @list_route()
    def get_signups_by_range_3months_count(self, request):
        last_year = datetime.datetime.now() - datetime.timedelta(days=1*90)
        members = Member.objects.filter(user__date_joined__gte=last_year) \
            .annotate(name=TruncMonth('user__date_joined')) \
            .values('name')  \
            .annotate(value=Count('id'))  \
            .values('name', 'value') 

        serializer = MemberSignupsByMonthSerilizer(members, many=True)
        return Response(serializer.data)


    @list_route()
    def get_signups_by_range_year_count(self, request):
        last_year = datetime.datetime.now() - datetime.timedelta(days=1*365)
        members = Member.objects.filter(user__date_joined__gte=last_year) \
            .annotate(name=TruncMonth('user__date_joined')) \
            .values('name')  \
            .annotate(value=Count('id'))  \
            .values('name', 'value') 

        serializer = MemberSignupsByMonthSerilizer(members, many=True)
        return Response(serializer.data)

    @list_route()
    def get_signups_by_range_5years_count(self, request):
        last_year = datetime.datetime.now() - datetime.timedelta(days=5*365)
        members = Member.objects.filter(user__date_joined__gte=last_year) \
            .annotate(name=TruncMonth('user__date_joined')) \
            .values('name')  \
            .annotate(value=Count('id'))  \
            .values('name', 'value') 

        serializer = MemberSignupsByMonthSerilizer(members, many=True)
        return Response(serializer.data)

    @list_route()
    def get_member_levels_count(self, request):
        members = Member.objects.annotate(name=F('membership_level__level')) \
            .values('name')  \
            .annotate(value=Count('id'))  \
            .values('name', 'value') 


        serializer = MemberTypesCountSerilizer(members, many=True)
        return Response(serializer.data)


    @detail_route(methods=['get'])
    def get_education(self, request, pk):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        events = MemberEducation.objects.filter(member=member)
        serializer = MemberEducationSerializer(events, many=True)
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

class MemberRegionViewSet(viewsets.ModelViewSet):
    queryset = MemberRegion.objects.all()
    serializer_class = MemberRegionSerializer

class MemberIndustryViewSet(viewsets.ModelViewSet):
    queryset = MemberIndustry.objects.all()
    serializer_class = MemberIndustrySerializer


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


@login_required
def member_create(request):


    #if member already created go to member edit
    if(Member.objects.filter(user=request.user).count() > 0):
        return redirect('members:member-profile')

    education_formset = formset_factory(MemberEducationForm)

    if request.method == 'POST':
      
        user_form = MemberUserForm(request.POST, instance=request.user)

        member_form = MemberForm(request.POST)
        address_form = MemberAddressForm(request.POST)

        formset = education_formset(request.POST)


        if(address_form.is_valid() and user_form.is_valid() and member_form.is_valid() and formset.is_valid()):
            #redirect('members:member-profile')

            user_form.save()
            member = member_form.save(commit=False)
            member.user = request.user
            member.save()


            address_form.save(commit=False)
            address_form.member = member
            address_form.save()

            education_formset.save(member=member)

        else:
            return render(request, 'members/member_create.html', {
                'user_form': user_form,
                'member_form': member_form,
                'address_form': address_form,
                'education_formset': education_formset
                })  

    else:

        address_form =  MemberAddressForm()
        user_form = MemberUserForm()
        member_form = MemberForm()
        address_form = MemberAddressForm()


    return render(request, 'members/member_create.html', {
        'user_form': user_form,
        'member_form': member_form,
        'address_form': address_form,
        'education_formset': education_formset
        })


@login_required
def member_profile(request):

    return render(request, 'members/member_profile.html')


def member_profile_edit(request):
    return render(request, 'members/member_profile_edit.html')




@login_required
def my_profile(request):

    try:
        member = Member.objects.get(user=request.user)
    except Member.DoesNotExist:
        return redirect('members:member-create')

    return render(request, 'members/my_profile.html', {
        'member' : member
        })