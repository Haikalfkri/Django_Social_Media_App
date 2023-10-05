from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostCreateForm


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