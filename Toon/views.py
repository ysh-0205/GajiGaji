from django.shortcuts import render

from Toon.models import Post


# Create your views here.



def index(request):
    posts = Post.objects.all()
    #categories = Gaji_Category.objects.all()
    return render(request,'Toon/Toon_index.html',
                  context={'posts':posts})


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request,'Toon/Toon_detail.html',
                  context={'post':post})