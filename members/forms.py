from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from registration.forms import RegistrationForm

User = get_user_model()


class MemberRegistrationForm(RegistrationForm):
    username = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email', 'password1')