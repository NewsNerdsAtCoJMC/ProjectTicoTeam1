from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Author, Post

def index(request):
    post_line = Post.objects.all() 
    context = {'post_line': post_line}
    return render(request, 'blog/index.html', context)

