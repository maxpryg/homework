from django.urls import path

from . import views

urlpatterns = [
    path('', views.hellodjango, name='hellodjango'),
    path('date/', views.fulldate, name='fulldate'),
    path('date/year/', views.year, name='year'),
    path('date/day/', views.day, name='day'),
    path('date/month/', views.month, name='month'),
    path('<str:name>/', views.greeting, name='greeting'),
]
