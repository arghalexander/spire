from django import forms
from django.forms import ModelForm
from .models import Member, MemberAddress, MemberEducation

class MemberForm(ModelForm):
	class Meta:
		model = Member
		fields = [
			'image',
			'bio',
			'region',
			]
		widgets = {
			'region': forms.CheckboxSelectMultiple()
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
		]

class MemberEducationForm(ModelForm):
	class Meta:
		model = MemberEducation
		fields = [
			'degree',
			'program',
			'grad_year',
		]