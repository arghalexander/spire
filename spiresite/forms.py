from django import forms
from .models import Job


class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=255)
    last_name = forms.CharField(label='Last Name', max_length=255)
    email = forms.EmailField(label='Email', max_length=255)
    phone = forms.CharField(label='Phone', max_length=255)
    message = forms.CharField(widget=forms.Textarea,label='Message')




class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'job_type','location','organization','description']
