from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    content = models.TextField()
    author = models.CharField(max_length=64)
    date = models.DateTimeField()


class Comment(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
