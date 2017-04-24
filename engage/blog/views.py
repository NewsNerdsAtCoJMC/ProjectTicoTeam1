from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Author, Post

def index(request):
    posts = Post.objects.all() 
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def blog(request):
    posts = Post.objects.all() 
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(id=pk) 
    context = {'post': post}
    return render(request, 'blog/blog_detail.html', context)

def housing(request):
    context = {}
    return render(request, 'blog/housing.html', context)

def transportation(request):
    posts = Post.objects.filter(tag__tag_slug="transportation")
    context = {'posts': posts}
    return render(request, 'blog/transportation.html', context)

def food(request):
    posts = Post.objects.filter(tag__tag_slug="food")
    context = {'posts': posts}
    return render(request, 'blog/food.html', context)

def entertainment(request):
    posts = Post.objects.filter(tag__tag_slug="entertainment")
    context = {'posts': posts}
    return render(request, 'blog/entertainment.html', context)