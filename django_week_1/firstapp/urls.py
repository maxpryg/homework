from django.urls import path

from .views import hellodjango, greeting, fulldate, year, day, month

urlpatterns = [
    path('', hellodjango, name='hellodjango'),
    path('date/', fulldate, name='fulldate'),
    path('date/year/', year, name='year'),
    path('date/day/', day, name='day'),
    path('date/month/', month, name='month'),
    path('<str:name>/', greeting, name='greeting'),
]
