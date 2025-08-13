
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Book_main, name='Book_main'),
    path('<int:pk>/', views.Book_detail, name='Book_detail'),
]



