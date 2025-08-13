import os
from django.db import models

# 이미지 저장 경로: media/Drama/드라마제목/파일명
def get_upload_path(instance, filename):
    return os.path.join('Drama', instance.title, filename)

class Drama(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    description = models.TextField(blank=True, null=True, verbose_name="설명")
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True, verbose_name="포스터")
    director = models.CharField(max_length=100, blank=True, null=True, verbose_name="감독")
    actors = models.CharField(max_length=200, blank=True, null=True, verbose_name="출연 배우")
    synopsis = models.TextField(blank=True, null=True, verbose_name="줄거리")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "드라마"
        verbose_name_plural = "드라마 목록"

class Comment(models.Model):
    drama = models.ForeignKey(Drama, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(verbose_name="댓글 내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")

    def __str__(self):
        return self.content[:20]
