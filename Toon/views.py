from django.shortcuts import render

from Toon.models import Gaji_Post


# Create your views here.



def Gaji_index(request):
    posts = Gaji_Post.objects.all()
    #categories = Gaji_Category.objects.all()
    return render(request,'Toon/index.html',
                  context={'posts':posts})


