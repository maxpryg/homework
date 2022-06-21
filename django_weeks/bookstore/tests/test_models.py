from django.test import TestCase

from bookstore.models import Author, Book


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Mark', last_name='Lutz', age=81)

    def test_last_name_max_length(self):
            author = Author.objects.get(id=1)
            max_length = author._meta.get_field('last_name').max_length
            self.assertEqual(max_length, 20)

    def test_first_name_max_length(self):
            author = Author.objects.get(id=1)
            max_length = author._meta.get_field('first_name').max_length
            self.assertEqual(max_length, 20)

    def test_object_name_is_last_name_comma_first_name(self):
            author = Author.objects.get(id=1)
            expected_object_name = f'{author.last_name}, {author.first_name}'
            self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
            author = Author.objects.get(id=1)
            # This will also fail if the urlconf is not defined.
            self.assertEqual(author.get_absolute_url(), '/catalog/author/1')
