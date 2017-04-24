from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Author, Post, Image, Tag

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"tag_slug": ("tag",)}

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Tag, TagAdmin)
