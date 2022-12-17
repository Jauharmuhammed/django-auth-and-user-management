from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',] 

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control',}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-control',}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control',}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class': 'form-control',}))