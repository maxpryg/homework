from django.test import TestCase
from django.urls import reverse

from datetime import date

class HellodjangoViewTest(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('hellodjango'))
        self.assertEqual(response.status_code, 200)

    def test_returns_correct_greeting(self):
        response = self.client.get('/')
        self.assertContains(response, 'Hello Django!')


class GreetingViewTest(TestCase):
#     def test_view_url_exists_at_correct_location(self):
#         response = self.client.get('', {'name': 'bob'})
#         self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('greeting', kwargs={'name': 'bob'}))
        self.assertEqual(response.status_code, 200)

    def test_view_returns_correct_greeting(self):
        #response = self.client.get('', {'name': 'bob'})
        response = self.client.get(reverse('greeting', kwargs={'name': 'bob'}))
        html = response.content.decode('utf8')
        self.assertIn('Hello bob!', html)


class FulldateViewTest(TestCase):
    def test_view_url_exists_at_correct_location(self):
        response = self.client.get('/date/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('fulldate'))
        self.assertEqual(response.status_code, 200)

    def test_view_returns_correct_date(self):
        current_date = date.today().strftime('%d.%m.%Y')
        response = self.client.get('/date/')
        html = response.content.decode('utf8')
        self.assertIn(current_date, html)


class YearViewTest(TestCase):
    def test_view_url_exists_at_correct_location(self):
        response = self.client.get('/date/year/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('year'))
        self.assertEqual(response.status_code, 200)

    def test_view_returns_correct_year(self):
        current_year = date.today().year
        response = self.client.get('/date/year/')
        html = response.content.decode('utf8')
        self.assertIn(str(current_year), html)


class DayViewTest(TestCase):
    def test_view_url_exists_at_correct_location(self):
        response = self.client.get('/date/day/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('day'))
        self.assertEqual(response.status_code, 200)

    def test_view_returns_correct_day(self):
        current_day = date.today().strftime('%d')
        response = self.client.get('/date/day/')
        html = response.content.decode('utf8')
        self.assertIn(current_day, html)


class MonthViewTest(TestCase):
    def test_view_url_exists_at_correct_location(self):
        response = self.client.get('/date/month/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('month'))
        self.assertEqual(response.status_code, 200)

    def test_view_returns_correct_month(self):
        current_month = date.today().strftime('%m')
        response = self.client.get('/date/month/')
        html = response.content.decode('utf8')
        self.assertIn(current_month, html)
