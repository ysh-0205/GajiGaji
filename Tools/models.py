from django.contrib.auth.models import User
from django.db import models



class Categorytype(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Categorygenre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    uploaded_image = models.ImageField(upload_to='images/', blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    Categorytype = models.ForeignKey(Categorytype, on_delete=models.SET_NULL, null=True)
    Categorygenre = models.ForeignKey(Categorygenre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'게시글제목 : {self.title} - 게시글내용 - {self.content} - 생성시간 - {self.created_date} - 업데이트 - {self.updated_date} - 종류 - {self.Categorytype} - 장르 - {self.Categorygenre}'

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)