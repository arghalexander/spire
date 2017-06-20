from django import forms
from django.forms import ModelForm
from .models import Member, MemberAddress, MemberEducation
from django.contrib.auth.models import User


class MemberUserForm(ModelForm):
	class Meta:
		model = User
		fields = [
			'first_name',
			'last_name'
		]


class MemberForm(ModelForm):
	class Meta:
		model = Member
		fields = [
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

