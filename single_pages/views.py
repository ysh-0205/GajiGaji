from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(
            request,
            'index.html',
            context={
                "name":"사용자님"
            }
                  )


def about_me(request):
    return render(
        request,
        template_name='single_pages/about_me.html'
    )