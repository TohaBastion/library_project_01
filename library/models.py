from django.db import models
from .managers import BookManager, AuthorManager


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)
    objects = AuthorManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=20)
    publish_date = models.DateField()
    objects = BookManager()

    def __str__(self):
        return self.title

# Create your models here.
