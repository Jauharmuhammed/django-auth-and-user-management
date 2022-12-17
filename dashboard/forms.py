
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'first_name'] 

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control mb-4',}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-control mb-4',}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control mb-4',}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class': 'form-control mb-4',}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name','class': 'form-control mb-4',}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name','class': 'form-control mb-4',}), required=False)


# class CustomUserUpdationForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name',] 

#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control mb-4',}))
#     email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-control mb-4',}))
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name','class': 'form-control mb-4',}), required=False)
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name','class': 'form-control mb-4',}), required=False)


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_password(self):
        return self.clean_password
