
from django.urls import path
from . import views
#127.0.01:8000/
urlpatterns = [
    path('',views.landing),
    path('about_me/',views.about_me)

]