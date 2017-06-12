from django import forms


class PaymentForm(forms.Form):
	cardholder_name = forms.CharField(label='Name that Appears on the card', max_length=100)
	


