from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length = 200)
    phone_number = forms.CharField(max_length = 10)
    message = forms.CharField(widget = forms.Textarea, max_length= 2000)
