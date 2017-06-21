from django import forms



class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=255)
    last_name = forms.CharField(label='Last Name', max_length=255)
    email = forms.EmailField(label='Email', max_length=255)
    phone = forms.CharField(label='Phone', max_length=255)
    message = forms.CharField(widget=forms.Textarea,label='Message')





class JobForm(forms.Form):
    title = forms.CharField(max_length=255)
    job_type = forms.CharField(max_length=255)
    location = forms.CharField(max_length=255)
    organization = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea,label='Description')