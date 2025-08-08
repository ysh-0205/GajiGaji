from django.shortcuts import render

# Create your views here.
def Toon_main(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 8)  # 한 페이지에 8개씩 보여주기

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Movie/Movie_main.html', {'page_obj': page_obj})