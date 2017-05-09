from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext_lazy as _
import re

CREDIT_CARD_RE = '^[0-9]{4}[\*]{8}[0-9]{4}$'



def validate_redacted(value):
    value = value.replace(' ', '').replace('-', '').replace(',', '')
    
    #pattern = re.compile(CREDIT_CARD_RE)

    if value and not re.match(CREDIT_CARD_RE, value):
        raise ValidationError(
            _('%(value)s is not in the required redacted format (1111-****-****-1111)'),
            params={'value': value},
        )