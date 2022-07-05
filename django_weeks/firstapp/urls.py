from django.urls import path

from . import views

urlpatterns = [
    path('', views.hellodjango, name='hellodjango'),
    path('hello_world/', views.hello_world, name='hello_world'),
    path('today/', views.today, name='today'),
    path('my_name/', views.my_name, name='my_name'),
    path('calculator/', views.calculator, name='calculator'),
    path('stores/', views.StoreList.as_view()),

    path('date/', views.fulldate, name='fulldate'),
    path('date/year/', views.year, name='year'),
    path('date/day/', views.day, name='day'),
    path('date/month/', views.month, name='month'),
    path('<str:name>/', views.greeting, name='greeting'),
]
