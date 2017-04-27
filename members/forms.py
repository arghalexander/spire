from django import forms
from django.forms import ModelForm
from .models import Member, MemberAddress, MemberDegree

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
			'address_line1',
			'address_line2',
			'city',
			'state',
			'zip_code',
		]

class MemberDegreeForm(ModelForm):
	class Meta:
		model = MemberDegree
		fields = [
			'degree',
			'program',
			'grad_year',
		]