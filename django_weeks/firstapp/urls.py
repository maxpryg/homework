from django.urls import path

from . import views

urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world'),
    path('today/', views.today, name='today'),
    path('my_name/', views.my_name, name='my_name'),
    path('calculator/', views.calculator, name='calculator'),
    path('stores/', views.StoreList.as_view()),
]
