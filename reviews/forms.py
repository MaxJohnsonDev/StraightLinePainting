from .models import Review
from django import forms


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'email', 'body')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'comment', 'image')
