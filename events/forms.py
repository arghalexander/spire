from dal import autocomplete
from django import forms

from .models import Event, EventAttendance


class EventAttendanceAutocompleteForm(forms.ModelForm):
	 class Meta:
		model = EventAttendance
		fields = ('__all__')
		widgets = {
			'member': autocomplete.ModelSelect2(url='events:attendance-autocomplete')
		}
