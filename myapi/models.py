from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    mobile = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name



