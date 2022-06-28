from django.db import models
from django.conf import settings
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
        return f'{self.title}'

    @staticmethod
    def create_books_from_dict(books, authors):
        for book in books:
            # loop over dictionary of authors, to get author of current book
            for author in authors:
                if book['author_id'] == author['id']:
                    author_dict = author

            # get author of the current book from DB
            author = Author.objects.get(
                last_name__exact=author_dict['last_name'])

            # save book to DB
            Book.objects.create(author=author,
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

    def get_all_author_books(self):
        """Return all books of certain author"""

        return Book.objects.filter(author__exact=self)


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    review_text = models.TextField(max_length=2000)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}, {self.book}'
