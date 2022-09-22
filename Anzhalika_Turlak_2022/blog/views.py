from django.shortcuts import render
from .models import Category
from .models import Post
from .models import Comment


def blog_index(request):
    posts = Post.objects.all().reverse('created_on')
    context = {
        'posts': posts
    }
    return render(request, 'posts_index.html', context)


def blog_detail(request, blog_id):
    post = Post.objects.filter(blog_id=blog_id)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)

