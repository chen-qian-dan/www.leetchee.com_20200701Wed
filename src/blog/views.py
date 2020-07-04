from django.shortcuts import render

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
        'posts': posts,
    }
    return render(request, 'blog/blog_home.html', context)