import os
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    bio = models.TextField()
    mugshot = models.ImageField(upload_to="media/", blank=True, null=True)
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to="media/")
    cutline = models.TextField()
    credit = models.ManyToManyField(Author)
    def __str__(self):
        return "%s" % self.image
    def filename(self):
        return os.path.basename(self.image)

class Tag(models.Model):
    tag = models.CharField(max_length=255)
    tag_slug = models.SlugField()
    def __str__(self):
        return self.tag

class Post(models.Model):
    headline = models.CharField(max_length=255)
    text = models.TextField()
    images = models.ManyToManyField(Image)
    author = models.ManyToManyField(Author)
    publication_date = models.DateTimeField()
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return self.headline
    def get_absolute_url(self):
        return "/blog/post/%i" % self.id
