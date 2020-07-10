from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView
from . import views


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_home'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('new/', BlogCreateView.as_view(), name='blog_create'),
]