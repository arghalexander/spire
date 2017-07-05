from django import forms
from django.forms import ModelForm
from .models import Member, MemberAddress, MemberEducation,MemberProfesionalInformation
from django.contrib.auth.models import User
from dal import autocomplete
from django.utils.translation import ugettext_lazy as _
from datetime import date
from .fields import ListTextWidget
from .models import MemberIndustry

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
		labels = {
			"region": _('Regional Affiliation'),
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
			'bio': forms.Textarea(attrs={'rows': 20}),
			'image' : forms.FileInput()
		}
		labels = {
			"region": _('Regional Affiliation'),
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
	grad_year = forms.ChoiceField(choices=[(x, x) for x in reversed(range(1935, date.today().year))])

	class Meta:
		model = MemberEducation
		fields = [
			'degree',
			'program',
			'grad_year',
		]


class MemberProfesionalInformationForm(ModelForm):

	industry = forms.ModelChoiceField(queryset=MemberIndustry.objects.exclude(entered_by__isnull=False))

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
