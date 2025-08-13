from django.urls import path
from . import views


urlpatterns = [
    #path('category/<slug>/', views.Category, name='Toon_category'),
    path('', views.index, name='Toon_index'),
    path('<int:pk>/', views.detail, name='Toon_detail'),
    path('create/',views.create, name='Create_Toon'),
    path('<int:pk>/createcomment/', views.createcomment, name='Toon_createcomment'),
    path('<int:pk>/updatecomment/', views.updatecomment, name='Toon_updatecomment'),
    path('<int:pk>/deletecomment/', views.deletecomment, name='Toon_deletecomment'),
    path('<int:pk>/update/', views.update, name='Toon_update'),
    path('<int:pk>/delete/', views.delete, name='Toon_delete'),


]