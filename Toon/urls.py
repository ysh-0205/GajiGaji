from django.urls import path
from . import views


urlpatterns = [
    #path('category/<slug>/', views.Category, name='Toon_category'),
    path('', views.index, name='Toon_index'),

]