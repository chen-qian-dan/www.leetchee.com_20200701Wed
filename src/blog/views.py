from django.shortcuts import render
from django.views.generic import ListView 
from .models import Blog

# Create your views here.

posts = [
    {
        'author': 'Qian',
        'title': 'ML',
        'content': 'Machine Learning', 
        'date_posted': 'July 02, 2020',
    }, 
    {
        'author': 'Chen',
        'title': 'CV',
        'content': 'Computer Vision', 
        'date_posted': 'July 02, 2020',
    }
]


def blog_home(request):
    #return HttpResponse('<h1>Page Home</h1>')
    context = {
        #'posts': posts,
        'blogs': Blog.objects.all(),
    }
    return render(request, 'blog/blog_home.html', context)


class PostListView(ListView):
    model = Blog
    template_name = 'blog/blog_home.html'
    context_object_name = 'blogs'
    ordering = ['-date_posted']