from multiprocessing import context
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib.admin.views.decorators import staff_member_required
from .forms import *


# Create your views here.

@login_required(login_url= 'login')
@staff_member_required(login_url='home')
def dashboard(request):
    User = get_user_model()
    users = User.objects.all()
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

        else:
            form= CustomUserCreationForm(request.POST)
    context = {
        'users' : users,
        'form': form
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url= 'login')
@staff_member_required(login_url='home')
def edit_user(request, pk):
    user_edit = User.objects.get(pk=pk)
    edit_form = CustomUserCreationForm(instance=user_edit)
    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, instance=user_edit)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'User data is updated successfully')
            return redirect('edit',pk)

        else:
            # edit_form = CustomUserUpdationForm(instance=user_edit)
            messages.error(request, 'Username is currenly in use or Invalid details')
            return redirect('edit',pk)

    context = {
        'editForm' : edit_form,
        'user' : user_edit
    }
    return render(request, 'edit-user.html', context)



@login_required(login_url= 'login')
@staff_member_required(login_url='home')
def delete_user(request, pk):
    user_del = User.objects.filter(pk = pk)
    user_del.delete()  
    return redirect('dashboard')




