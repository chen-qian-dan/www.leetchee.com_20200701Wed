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
            messages.success(request, f'已成功为您注册新账号： {username} ! 您现可用此账号登陆。')
            return redirect('user_login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, "user/user_register.html", context)
    