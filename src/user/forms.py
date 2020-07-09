from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class UserRegisterForm(UserCreationForm): # inherit from UserCreationForm 
    email = forms.EmailField()

    class Meta:
        model = User
        # fields we want to show
        fields = ['username', 'email', 'password1', 'password2']