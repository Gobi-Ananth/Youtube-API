from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('search_videos/', views.search_videos, name = 'search_videos'),
]
