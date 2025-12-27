from django import forms
from .models import ReviewModel, Build

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ('body', 'rating')


class BuildForm(forms.ModelForm):
    class Meta:
        model = Build
        fields = ('title', 'content', 'image')
