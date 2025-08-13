from django.contrib import admin
from django.utils.html import format_html
from .models import Drama, Comment

@admin.register(Drama)
class DramaAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'actors', 'poster_preview')
    search_fields = ('title', 'director', 'actors')
    readonly_fields = ('poster_preview',)

    def poster_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:100px; height:auto;" />', obj.image.url)
        return "(이미지 없음)"
    poster_preview.short_description = "포스터 미리보기"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('drama', 'content', 'created_at')
    search_fields = ('drama__title', 'content')
    list_filter = ('created_at',)
