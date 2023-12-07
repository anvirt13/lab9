from django.forms import ModelForm
from django import forms
from .models import Movie
from .models import Review



class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ["create_at", "updated_at", "posted_by"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment'] 