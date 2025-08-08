from django.contrib import admin
from .models import Post , Comment , Categorytype , Categorygenre

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Categorytype)
admin.site.register(Categorygenre)