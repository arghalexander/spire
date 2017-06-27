from django import forms
from django.forms import ModelForm
from .models import Member, MemberAddress, MemberEducation,MemberProfesionalInformation
from django.contrib.auth.models import User
from dal import autocomplete



class MemberUserForm(ModelForm):
	first_name = forms.CharField(max_length=200,required=True)
	last_name = forms.CharField(max_length=200,required=True)
	
	class Meta:
		model = User
		fields = [
			'first_name',
			'last_name'
		]


class MemberCreateForm(ModelForm):
	class Meta:
		model = Member
		fields = [
			'region',
			]
		widgets = {
			'region': forms.CheckboxSelectMultiple(),
		}


class MemberForm(ModelForm):
	class Meta:
		model = Member
		fields = [
			'region',
			'image',
			'bio',
			]
		widgets = {
			'region': forms.CheckboxSelectMultiple(),
			'bio': forms.Textarea(attrs={'rows': 20})
		}
		labels = {
        	"region": _("Regional Affiliation")
    	}


class MemberAddressForm(ModelForm):
	class Meta:
		model = MemberAddress
		fields = [
			
			'address_line_one',
			'address_line_two',
			'city',
			'state',
			'zip_code',
			'country',
		]

class MemberEducationForm(ModelForm):
	class Meta:
		model = MemberEducation
		fields = [
			'degree',
			'program',
			'grad_year',
		]


class MemberProfesionalInformationForm(ModelForm):
	class Meta:
		model = MemberProfesionalInformation
		fields = [
			'title',
			'company',
			'industry',
			'address_line_one',
			'address_line_two',
			'city',
			'state',
			'zip_code',
			'country',
			'assistant_name',
			'assistant_email',
			'assistant_phone',
		]
