from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts.html', {'posts' : posts})

def page_view(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post.html', {'post':post})

@login_required(login_url='/users/login/')
def create_post(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            # print("save")
            return redirect("posts:list")
    else:
        form = forms.CreatePost()
    return render(request, 'posts/new_post.html', {'form' : form})