from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    bio = models.TextField()
    mugshot = models.ImageField(upload_to="Users/lera_alfimova/ProjectTicoTeam1/engage/engage/uploads/", blank=True, null=True)
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to="Users/lera_alfimova/ProjectTicoTeam1/engage/engage/uploads/")
    cutline = models.TextField()
    credit = models.ManyToManyField(Author)
    def __str__(self):
        return "%s" % self.image


class Post(models.Model):
    headline = models.CharField(max_length=255)
    text = models.TextField()
    images = models.ManyToManyField(Image)
    author = models.ManyToManyField(Author)
    publication_date = models.DateTimeField()
    def __str__(self):
        return self.headline