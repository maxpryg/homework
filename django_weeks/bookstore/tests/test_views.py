from django.test import TestCase
from django.urls import reverse

from bookstore.data import books, authors
from bookstore.models import Book, Author


class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        """Populate DB with authors and books"""
        Author.create_authors_from_dict(authors)
        Book.create_books_from_dict(books, authors)
        self.books_quantity = Book.objects.count()
        self.books_quantity_with_python = Book.objects.filter(
            title__icontains='python').count()
        self.books_quantity_with_blablabla = Book.objects.filter(
            title__icontains='blablabla').count()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/bookstore/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bookstore:index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bookstore:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookstore/index.html')

    def test_lists_all_books(self):
        response = self.client.get(reverse('bookstore:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['books']), self.books_quantity)

    def test_returns_right_quantity_of_books_with_python(self):
        response = self.client.get('/bookstore/', {'search_text': 'python'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookstore/index.html')
        self.assertEqual(len(response.context['books']),
                         self.books_quantity_with_python)

    def test_returns_zero_quantity_of_books(self):
        response = self.client.get('/bookstore/', {'search_text': 'blablabla'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookstore/index.html')
        self.assertEqual(len(response.context['books']),
                         self.books_quantity_with_blablabla)


class AuthorViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        """Populate DB with authors and books"""
        Author.create_authors_from_dict(authors)
        Book.create_books_from_dict(books, authors)
        self.author = Author.objects.first()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/bookstore/author/{self.author.id}/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bookstore:author_detail',
                                           args=[self.author.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bookstore:author_detail',
                                           args=[self.author.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookstore/author-detail.html')


class BookViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        """Populate DB with authors and books"""
        Author.create_authors_from_dict(authors)
        Book.create_books_from_dict(books, authors)
        self.book = Book.objects.first()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/bookstore/book/{self.book.id}/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bookstore:book_detail',
                                           args=[self.book.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bookstore:book_detail',
                                           args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookstore/book-detail.html')


class AuthorBookListViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        """Populate DB with authors and books"""
        Author.create_authors_from_dict(authors)
        Book.create_books_from_dict(books, authors)
        self.author = Author.objects.first()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/bookstore/author/1/books/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bookstore:author_book_list',
                                           args=[self.author.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bookstore:author_book_list',
                                           args=[self.author.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookstore/author-book-list.html')


class AddAuthorViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/bookstore/add_author/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bookstore:add_author'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bookstore:add_author'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookstore/add-author.html')

    def test_redirects_to_add_book_view_on_success(self):
        response = self.client.post(reverse('bookstore:add_author'),
                                    {'first_name': 'Mark',
                                     'last_name': 'Lutz',
                                     'age': 81})
        self.assertRedirects(response, reverse('bookstore:add_book'))


class AddBookViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/bookstore/add_book/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bookstore:add_book'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bookstore:add_book'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookstore/add-book.html')

    def test_redirects_to_index_view_on_success(self):
        self.author = Author.objects.create(first_name='Mark',
                                            last_name='Lutz',
                                            age=81)
        response = self.client.post(reverse('bookstore:add_book'),
                                    {'author': self.author.id,
                                     'title': 'Learning Python, 5th Edition',
                                     'released_year': 2013,
                                     'description': 'Get a comprehensive...'})
        self.assertRedirects(response, reverse('bookstore:index'))
