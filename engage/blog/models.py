from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    bio = models.TextField()
    mugshot = models.ImageField(XXXXXXXX)
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(XXXXXXXXX)
    cutline = models.TextField()
    credit = models.ManyToManyField(Author)
    


class Post(models.Model):
    headline = models.CharField(max_length=255)
    text = models.TextField()
    images = models.ManyToManyField(Image)
    author = models.ManyToManyField(Author)
    def __str__(self):
        return self.headline
