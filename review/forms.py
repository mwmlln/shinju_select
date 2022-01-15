from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ Create/Update review """
    class Meta:
        model = Review
        fields = ['rating', 'comment']


class DeleteReviewForm(forms.ModelForm):
    """ Delete review """
    class Meta:
        model = Review
        fields = []
