from django import forms
from .models import Comment

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length = 200)
    phone_number = forms.CharField(max_length = 10)
    message = forms.CharField(widget = forms.Textarea, max_length= 2000)


class CommentForm(forms.ModelForm):
    content = forms.CharField(label = "", widget = forms.Textarea(
    attrs = {
        'class': 'form-control',
        'placeholder': 'comment here',
        'rows': 4,
        'cols': 50
    }
    ))
    class Meta:
        model = Comment
        fields = ['content']
