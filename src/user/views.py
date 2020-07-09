from django.shortcuts import render, redirect 
from django.contrib import messages 
from .forms import UserRegisterForm 



# Create your views here.

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'已生成账号：{username}!')
            return redirect('page_home')
    else:
        form = UserRegisterForm()
    return render(request, "user/user_register.html", {'form': form})
    