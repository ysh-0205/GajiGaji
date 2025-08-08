from django import forms
from GajiGaji.Movie.models import Post , Comment , Category

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

