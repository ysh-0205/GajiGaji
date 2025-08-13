from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render , redirect
from Tools.models import Post, Comment, Categorytype, Categorygenre , HighlightImage , Rating
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from Tools.forms import PostForm , CommentForm
from django.db.models import Count, Avg, Q
from django.contrib.auth.decorators import login_required

def Book_main(request):
    query = request.GET.get('q')
    post_list = Post.objects.filter(Categorytype__name='책').annotate(avg_rating=Avg('ratings__rating')).order_by(
        '-created_date')

    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) | Q(Categorygenre__name__icontains=query)
        )

    paginator = Paginator(post_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    try:
        Book_category = Categorytype.objects.get(name='책')
        categories = [Book_category]
    except Categorytype.DoesNotExist:
        categories = []

    return render(request, 'Book/Book_main.html', {'page_obj': page_obj, 'categories': categories})

def Book_detail(request, pk):
    post = Post.objects.get(pk=pk)
    highlight_images = post.highlight_images.all()
    categories = Categorytype.objects.all()
    comments = Comment.objects.filter(post=post)
    commentform = CommentForm()

    return render(
        request,
        'Book/Book_detail.html',
        {
            'post': post,
            'categories': categories,
            'commentform': commentform,
            'comments': comments,
            'highlight_images': highlight_images,
        }
    )

@login_required(login_url='/accounts/google/login/')
def createcomment(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(post.get_absolute_url())
    return redirect(post.get_absolute_url())
@login_required(login_url='/accounts/google/login/')
def updatecomment(request,pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    if request.method == "POST":
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment1 = commentform.save(commit=False)
            comment1.post = post
            comment1.save()
            return redirect(post.get_absolute_url())
    else:
        commentform = CommentForm(instance=comment)
    return render(request,
                  template_name='blog/commentform.html',
                  context={'commentform':commentform,})
@login_required(login_url='/accounts/google/login/')
def deletecomment(request,pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    comment.delete()
    return redirect(post.get_absolute_url())
@login_required(login_url='/accounts/google/login/')
def create(request):
    categories = Categorytype.objects.all()
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            post = postform.save(commit=False)
            post.author = request.user
            post.save()

            images = [
                request.FILES.get('highlight_image1'),
                request.FILES.get('highlight_image2'),
                request.FILES.get('highlight_image3')
            ]
            for image_file in images:
                if image_file:  # 파일이 있을 경우에만 저장
                    HighlightImage.objects.create(post=post, image=image_file)

            return redirect('/Book/')
        else:
            return render(request, 'Book/Book_create.html', {'postform': postform, 'categories': categories})
    else:
        postform = PostForm()
        return render(request, 'Book/Book_Create.html', {'postform': postform, 'categories': categories})
@login_required(login_url='/accounts/google/login/')
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/Book/')

@login_required(login_url='/accounts/google/login/')
def update(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        # request.FILES를 반드시 포함하여 폼을 초기화합니다.
        postform = PostForm(request.POST, request.FILES, instance=post)

        if postform.is_valid():
            # 먼저 Post 모델의 내용을 저장합니다.
            post = postform.save()

            # ✅ 이미지 처리 로직 추가:
            # 1. 기존 HighlightImage들을 모두 삭제합니다.
            post.highlight_images.all().delete()

            # 2. 새로운 이미지 파일들을 가져와 HighlightImage 객체를 생성합니다.
            #    create 함수에서 사용한 필드명 ('highlight_image1', 'highlight_image2' 등)을 그대로 사용합니다.
            for i in range(1, 4):  # 1부터 4까지 반복
                image_file = request.FILES.get(f'highlight_image{i}')
                if image_file:
                    HighlightImage.objects.create(post=post, image=image_file)

            return redirect('Book_detail', pk=post.pk)  # 수정 후 상세 페이지로 리다이렉트
        else:
            # 폼이 유효하지 않을 경우, 에러 메시지와 함께 다시 렌더링하거나 다른 처리를 할 수 있습니다.
            return render(request, 'Book/Book_create.html', {'postform': postform})
    else:
        # GET 요청일 경우, 기존 데이터를 폼에 채워서 보여줍니다.
        postform = PostForm(instance=post)

    return render(request, template_name='Book/Book_create.html', context={'postform': postform})
