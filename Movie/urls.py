from django.urls import path
from . import views


urlpatterns = [
    path('',views.Movie,name='index'),

]