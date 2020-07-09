from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 


# Create your views here.

def user_register(request):
    form = UserCreationForm()
    return render(request, "user/user_register.html", {'form': form})
    