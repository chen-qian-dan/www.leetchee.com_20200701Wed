from django.urls import path
from .views import BlogListView, BlogDetailView
from . import views


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_home'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]