
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import *

def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CustomUserCreationForm()
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Created Successfully')
                return redirect('login')
        
        context = {'form': form}
        return render(request, 'register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            
            user= authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')


products = Products.objects.all()

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html',{
        'products': products
    })

