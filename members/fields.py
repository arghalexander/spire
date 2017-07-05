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





class ListTextWidget(forms.TextInput):
    def __init__(self, data_list, name, *args, **kwargs):
        super(ListTextWidget, self).__init__(*args, **kwargs)
        self._name = name
        self._list = data_list
        self.attrs.update({'list':'list__%s' % self._name})

    def render(self, name, value, attrs=None):
        text_html = super(ListTextWidget, self).render(name, value, attrs=attrs)
        data_list = '<datalist id="list__%s">' % self._name
        for item in self._list:
            data_list += '<option value="%s">' % item
        data_list += '</datalist>'

        return (text_html + data_list)