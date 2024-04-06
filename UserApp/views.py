from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {users: 'users'})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        else:
            form = UserForm()

    return render(request, 'create_user.html', {'form': form})

def update_user(request, user_id):
    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)

    return render(request, 'update_user.html', {'form': form})

def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('user_list')
