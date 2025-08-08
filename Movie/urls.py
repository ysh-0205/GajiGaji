from django.urls import path
from . import views


urlpatterns = [
    path('',views.Movie_main,name='main'),
    path('<int:post_id>/', views.Movie_detail, name='Movie_detail'),

]