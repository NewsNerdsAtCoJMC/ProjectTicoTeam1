from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    bio = models.TextField()
    mugshot = models.ImageField(upload_to='Users/lera_alfimova/ProjectTicoTeam1/engage/engage/uploads/', height_field=200, width_field=200, max_length=100)
    def __str__(self):
        return self.name
        return self.bio
        return self.mugshot

class Image(models.Model):
    image = models.ImageField(upload_to='Users/lera_alfimova/ProjectTicoTeam1/engage/engage/uploads/', height_field=600, width_field=800, max_length=100)
    cutline = models.TextField()
    credit = models.ManyToManyField(Author)
    def __str__(self):
        return self.image
        return self.cutline
        return self.credit

    
class Date(models.Model):
    date = models.DateField()
    def __str__(self):
        return self.date


class Post(models.Model):
    headline = models.CharField(max_length=255)
    text = models.TextField()
    images = models.ManyToManyField(Image)
    author = models.ManyToManyField(Author)
    date = models.DateField()
    def __str__(self):
        return self.headline
        return self.text
        return self.images
        return self.author
        return self.date

    
