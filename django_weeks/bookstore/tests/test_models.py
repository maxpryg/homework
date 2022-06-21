from django.test import TestCase

from bookstore.models import Author, Book
from bookstore.data import books, authors


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Populate DB with authors and books"""
        Author.create_authors_from_dict(authors)
        Book.create_books_from_dict(books, authors)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 20)

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 20)

    def test_author_string_representation(self):
        author = Author.objects.get(id=1)
        expected_author_name = f'{author.last_name} {author.first_name}'
        self.assertEqual(str(author), expected_author_name)

    def test_get_all_author_books(self):
        author = Author.objects.get(id=1)
        expected_author_books_count = Book.objects.filter(
            author_id__exact=author.id).count()
        author_books_count = Author.get_all_author_books(author).count()
        self.assertEqual(author_books_count, expected_author_books_count)


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Populate DB with authors and books"""
        Author.create_authors_from_dict(authors)
        Book.create_books_from_dict(books, authors)

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_description_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('description').max_length
        self.assertEqual(max_length, 1000)

    def test_book_string_representation(self):
        book = Book.objects.get(id=1)
        expected_book_name = f'{book.title}, {book.author}'
        self.assertEqual(str(book), expected_book_name)
