from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):
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


class AuthorViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/bookstore/author/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bookstore:author_detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bookstore:author_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookstore/author-detail.html')


class BookViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/bookstore/book/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bookstore:book_detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bookstore:book_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookstore/book-detail.html')


class AuthorBookListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/bookstore/author/1/books/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bookstore:author_book_list', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bookstore:author_book_list', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookstore/author-book-list.html')
