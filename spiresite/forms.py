from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=255)
    last_name = forms.CharField(label='Last Name', max_length=255)
    email = forms.EmailField(label='Email', max_length=255)
    phone = forms.CharField(label='Phone', max_length=255)
    message = forms.CharField(widget=forms.Textarea,label='Message')