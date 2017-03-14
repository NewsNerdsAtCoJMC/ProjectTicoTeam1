from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Author, Post

def index(request):
    author_line = Author.objects.all() 
    context = {'author_line': author_line}
    return render(request, 'blog/index.html', context)
    
    post_line = Post.objects.all() 
    context = {'post_line': post_line}
    return render(request, 'blog/index.html', context)

