from django.urls import path
from .views import PostListView
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
]