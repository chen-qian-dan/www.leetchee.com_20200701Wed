from django.shortcuts import render

# Create your views here.

def blog_home(request):
    #return HttpResponse('<h1>Page Home</h1>')
    return render(request, 'blog/blog_home.html')