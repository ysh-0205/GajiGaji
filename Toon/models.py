from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    uploaded_image = models.ImageField(upload_to='images/', blank=True)
    uploaded_file = models.FileField(upload_to='images/', blank=True)
    #category = models.ForeignKey('Category', on_delete=models.CASCADE)
    def __str__(self):
        return (f'게시글제목:{self.uploaded_image} - {self.title}-by {self.author} - 게시글 내용 -{self.content} - 생성시간 - '
                f'{self.created_date} - 수정시간 - {self.updated_date} - 수정파일 - {self.uploaded_file}')





# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)
#
#     def get_urls(self):
#         return f'/Toon/category/{self.slug}/'
#     def __str__(self):
#         return f'{self.name} ---- {self.slug}'
#
#
#
#
#
# class coomment(models.Model):
#     post = models.ForeignKey(Gaji_Post, on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_date = models.DateTimeField(auto_now_add=True, null=True)
#     updated_date = models.DateTimeField(auto_now=True, null=True)
#
#     def __str__(self):
#         return f'{self.author.username} - {self.content} in {self.post.title}'