from django import forms
from .models import Record, Review

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('title', 'content', 'status', 'featured_image')  # include image

    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body', 'rating')