from django import forms
from .models import Record, Review

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('title', 'author', 'featured_image', 'artist', 'genre', 'year', 'recordLabel', 'content', 'status', 'excerpt')  # include image

    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body', 'rating')