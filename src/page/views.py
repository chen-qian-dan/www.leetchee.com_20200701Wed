from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def page_home(request):
    #return HttpResponse('<h1>Page Home</h1>')
    return render(request, 'page/page_home.html')


def page_about(request):
    #return HttpResponse('<h1>Page About</h1>')
    return render(request, 'page/page_about.html')