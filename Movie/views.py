from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render , redirect
from Tools.models import Post

# Create your views here.
def Movie_main(request):
    posts = Tools.Post.objects.all()
    return render(request,
                  'Movie/Movie_main.html',
                  context={'posts':posts}
                  )

def Movie_create(request):
    title = request.POST['title']
    content = request.POST['content']