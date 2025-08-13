from django.urls import path
from . import views

urlpatterns = [
    path('', views.Drama_main, name='Drama_index'),
    path('Drama/<int:drama_id>/', views.Drama_detail, name='Drama_detail'),
]
