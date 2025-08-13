from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Categorytype(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(unique=True)

    def __str__(self):
        return self.name

class Categorygenre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    uploaded_image = models.ImageField(upload_to='images/', blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tool_posts')

    Categorytype = models.ForeignKey(Categorytype, on_delete=models.SET_NULL, null=True)
    Categorygenre = models.ForeignKey(Categorygenre, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('Movie_detail', args=[str(self.id)])

    def __str__(self):
        return f'게시글제목 : {self.title} - 게시글내용 - {self.content} - 생성시간 - {self.created_date} - 업데이트 - {self.updated_date} - 종류 - {self.Categorytype} - 장르 - {self.Categorygenre}'

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)



# ✅ 하이라이트 이미지 모델 추가
class HighlightImage(models.Model):
    # post 모델과 연결. related_name을 'highlight_images'로 설정
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='highlight_images')
    image = models.ImageField(upload_to='highlights/')
    caption = models.CharField(max_length=200, blank=True, null=True)  # ✅ null=True 추가
    def __str__(self):
        return f'{self.post.title} Highlight Image'

# 별점 매기기 모델 추가
class Rating(models.Model):
    """
    별점을 저장하기 위한 모델.
    - Post와 연결됩니다.
    - User와 연결되어 누가 별점을 주었는지 알 수 있습니다.
    - rating은 1에서 5까지의 정수로 저장됩니다.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.title} - {self.rating} by {self.author.username}'
