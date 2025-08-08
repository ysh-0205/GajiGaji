from django import forms
from Tools.models import Post , Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','category','uploaded_image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']