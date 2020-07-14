from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30, name='Имя')
    last_name = models.CharField(max_length=30, name='Фамилия')

class Category(models.Model):
    title = models.CharField(max_length=255)

class Topic(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.ManyToManyField(Category, related_name='Записи')

