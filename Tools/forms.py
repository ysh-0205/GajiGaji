from django import forms
from Tools.models import Post , Comment

class PostForm(forms.ModelForm):
    highlight_image1 = forms.ImageField(label='하이라이트 이미지 1', required=False)
    highlight_image2 = forms.ImageField(label='하이라이트 이미지 2', required=False)
    highlight_image3 = forms.ImageField(label='하이라이트 이미지 3', required=False)
    highlight_image4 = forms.ImageField(label='하이라이트 이미지 4', required=False)
    class Meta:
        model = Post
        fields = ['title','content','Categorytype','Categorygenre','uploaded_image',
                  'highlight_image1','highlight_image2','highlight_image3','highlight_image4' ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']



