from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255, blank=True, null=True, default=None)
    author = models.ManyToManyField(Author)