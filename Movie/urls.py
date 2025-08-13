from django.urls import path , include
from . import views


urlpatterns = [
    path('',views.Movie_main,name='Movie_main'),
    path('<int:pk>/', views.Movie_detail, name='Movie_detail'),

    path('<int:pk>/deletecomment/', views.deletecomment, name='deletecomment'),
    path('<int:pk>/updatecomment/', views.updatecomment, name='updatecomment'),
    path('<int:pk>/createcomment/', views.createcomment, name='createcomment'),
    path('create/', views.create, name='Movie_create'),
    path('<int:pk>/update/', views.update, name='Toon_update'),
    path('<int:pk>/delete/', views.delete, name='Toon_delete'),

#    path('accounts/', include('allauth.urls')),
]