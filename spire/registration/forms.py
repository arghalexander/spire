from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from registration.forms import RegistrationForm

User = get_user_model()


class MemberRegistrationForm(RegistrationForm):
	username = forms.EmailField(label="Email")
	email = forms.EmailField(widget=forms.HiddenInput(),required=False)
	student = forms.BooleanField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = User
		fields = ('username', 'first_name','last_name','password1')
		exclude = ('email',)

	def clean(self):
		super(MemberRegistrationForm, self).clean()
		username = self.cleaned_data.get("username")
		check_student = self.cleaned_data['student']

		if(check_student):
			email = self.cleaned_data.get("username").split("@")
			email_domain = email[1]
			stanford_domain = "standford.edu"

			if( email_domain !=  stanford_domain):
				pass
				#raise forms.ValidationError(
                #    "The email provided is not a stanford email address"
                #)

		return self.cleaned_data