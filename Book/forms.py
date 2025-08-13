from django import forms
from Book.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author','content','head_image','category']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = ['author','content']
        fields = ['content']