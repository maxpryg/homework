from django.db import models
from django.core.validators import MaxValueValidator

from datetime import date


class Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    released_year = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(date.today().year,
        message="Release year can't be more than current year")])
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.title}, {self.author}'

    @staticmethod
    def create_books_from_dict(books):
        for book in books:
            Book.objects.create(author=book.author,
                                title=book['title'],
                                released_year=book['released_year'],
                                description=book['description'])


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.SmallIntegerField()

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    @staticmethod
    def create_authors_from_dict(authors):
        for author in authors:
            Author.objects.create(first_name=author['first_name'],
                                  last_name=author['last_name'],
                                  age=author['age'])
