from django.urls import path
from . import views


urlpatterns = [
    path('',views.Movie_main,name='index'),

]