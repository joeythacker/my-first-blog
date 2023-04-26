from django.utils import timezone
from django.shortcuts import render
from .models import Post

def blog_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog_posts.html', {'posts': posts})
