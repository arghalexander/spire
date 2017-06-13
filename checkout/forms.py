from django import forms


class PaymentForm(forms.Form):
	first_name = forms.CharField(label='First Name', max_length=100)
	last_name = forms.CharField(label='Last Name', max_length=100)
	address_one = forms.CharField(label='Last Name', max_length=100)
	
