from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Author, Image, Date, Post

def index(request):
    author_line = Author.objects.all() 
    context = {'author_line': author_line}
    return render(request, 'blog/index.html', context)
    
    image_line = Image.objects.all() 
    context = {'image_line': image_line}
    return render(request, 'blog/index.html', context)

    date_line = Date.objects.all() 
    context = {'date_line': date_line}
    return render(request, 'blog/index.html', context)

    post_line = Post.objects.all() 
    context = {'post_line': post_line}
    return render(request, 'blog/index.html', context)

