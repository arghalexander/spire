import re
from datetime import date
from calendar import monthrange, IllegalMonthError
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _



class RedactedCreditCardField(forms.CharField):
    """
    Form field that takes credit card numbers and redacts the middle 8 characters.
    """

    default_error_messages = {
        'required': _(u'Please enter a credit card number.'),
    }

    def clean(self, value):    
        cc_type = value[0:4]
        cc_num = value[-4:]
        value = cc_type + '**** **** ' + cc_num

        if self.required and not value:
            raise forms.util.ValidationError(self.error_messages['required'])
        return value