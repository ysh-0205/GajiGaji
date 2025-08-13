from django.contrib import admin
from .models import Post, Comment, Categorytype, Categorygenre, HighlightImage

class HighlightImageInline(admin.TabularInline):
    model = HighlightImage
    extra = 3  # 처음부터 3개의 빈 폼을 보여줍니다. 필요에 따라 개수 조절 가능

# ✅ Post 모델을 위한 Admin 클래스
class PostAdmin(admin.ModelAdmin):
    inlines = [HighlightImageInline] # Post 관리자 페이지에 HighlightImageInline 추가
    list_display = ('title', 'author', 'created_date', 'Categorytype', 'Categorygenre')
    list_filter = ('Categorytype', 'Categorygenre')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Categorytype)
admin.site.register(Categorygenre)



