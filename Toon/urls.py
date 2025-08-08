from django.urls import path
from . import views


urlpatterns = [
    #path('category/<slug>/', views.Gaji_Category, name='Toon_category'),
    path('', views.Gaji_index, name='Toon_index'),

]