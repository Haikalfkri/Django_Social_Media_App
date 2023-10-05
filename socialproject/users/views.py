from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Profile
from post.models import Post

from django.contrib import messages

from .forms import UserEditForm, ProfileEditForm
from users.forms import LoginForm, RegisterForm 

# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return HttpResponse("Invalid login ")
    else:
        form = LoginForm()        
    
    return render(request, "users/login.html", {'form': form})


def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'users/register_done.html')
    else:
        form = RegisterForm()
        
    return render(request, 'users/register.html', {'form': form})
            
    
# homepage
@login_required
def index(request):
    current_user = request.user
    post = Post.objects.filter(user=current_user)
    
    return render(request, "users/index.html", {'posts': post})


# edit user data and user profile
@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "profile update successfull")
            return redirect('index')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        
    return render(request, "users/edit.html", {'user_form': user_form, 'profile_form': profile_form})