from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostCreateForm
from .models import Post
from users.models import Profile
from django.shortcuts import get_object_or_404


# Create your views here.
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostCreateForm(data=request.POST, files=request.FILES)
        
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect("index")
    else:
        form = PostCreateForm(data=request.GET)
    
    return render(request, 'posts/create.html', {'form': form})


@login_required
def feed(request):
    posts = Post.objects.all()
    logged_user = request.user
    return render(request, "posts/feed.html", {'posts': posts, 'logged_user':logged_user})


def like_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    
    return redirect('feed')