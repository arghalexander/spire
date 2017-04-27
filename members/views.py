from rest_framework import viewsets

from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView

from registration import signals

from .forms import MemberForm, MemberAddressForm, MemberDegreeForm
from .models import Member, MemberAddress, MembershipLevel
from .serializers import MembershipLevelSerializer, MemberAddressSerializer,  MemberSerializer



from django.views.generic.edit import FormView


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MembershipLevelViewSet(viewsets.ModelViewSet):
    queryset = MembershipLevel.objects.all()
    serializer_class = MembershipLevelSerializer


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
