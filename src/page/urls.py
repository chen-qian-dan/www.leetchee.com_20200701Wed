from django.urls import path
from . import views


urlpatterns = [
    path('', views.page_home, name='page_home'),
    path('about/', views.page_about, name='page_about'),
]