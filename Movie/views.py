from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render , redirect
from .models import Post

# Create your views here.
def Movie(request):
    posts = Post.objects.all()
    return render(request,
                  'Movie/Movie_main.html',
                  context={'posts':posts}
                  )